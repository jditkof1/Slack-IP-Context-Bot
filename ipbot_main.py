import os
import logging
import re
from flask import Flask
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter
from class_ipbot import IPBot


# Initialize a Flask app to host the events adapter
app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event ingestion.
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))


def format_message(channel, ip_address):
    ip_bot = IPBot("#test-channel")

    final_message = ip_bot.create_message(ip_address)

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**final_message)


# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):
    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = (event.get("text")).lower()
    regexp = "(?:1?\d?\d|2[0-4]\d|25[0-5])(?:.(?:1?\d?\d|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])"
    ip_address = (re.search(regexp, text)).group(0)

    # Check and see if the activation phrase was in the text of the message.
    if ip_address:
        channel_id = event.get("channel")

        # Run format_message and send the results to the specified channel
        return format_message(channel_id, ip_address)


if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    app.run(host='0.0.0.0', port=3000)
