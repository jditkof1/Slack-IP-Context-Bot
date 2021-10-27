# Slack-IP-Context-Bot
Coding challenge for ThreatQuotient

Written by: Jacob Ditkoff

All API keys have been hidden to avoid being public-facing.

NOTES: 
  - This app was written in the PyCharm IDE on Mac, so the virtual environment was set up automatically. 
  - To run this locally, you'll need to open up a network port to allow for slack to connect to your machine. If you're using linux, you can open up a port in the terminal like so:
        $ sudo ufw allow 3000     --this is to open up port 3000 in your firewall
        $ sudo ufw status         --this is to see if port 3000 is listed and allowing access
  - If you're running on Mac, you may need to host this app externally through a source like AWS or Heroku, for example.
  - To open up a port on Windows, follow this tutorial and use port 3000: https://www.howtogeek.com/394735/how-do-i-open-a-port-on-windows-firewall/ 
        
If you're running everything from the command line, you'll need to set up a virtual environment manually. 

Steps to run locally: 
  1) Create a channel called #test-channel, or if you want to have the app running in a currently existing channel, edit line 20 within ipbot_main.py to:           ip_bot = IPBot("#type-your-channel-name-here") 
  2) from the Slack API Control Panel (https://api.slack.com/apps), click Create New App
  3) Enter IPBot for the name, and pick a workspace you'd like to have the bot running in. Then hit Create App
  4) Head to the OAuth & Permissions tab on the left side of the page. Under the Scopes section, click Add an OAuth Scope underneath Bot Token Scopes.
  5) Select which permissions you'd like IPBot to have. I selected:
        - channels:history
        - channels:join
        - channels:read
        - chat:write
        - im:read
  6) Scroll up and click Install App to Workspace
  7) Once you've allowed it to be installed to your chosen workspace, copy down your Bot User OAuth Access Token.
  8) After copying down your Bot Token, return to the Basic Information tab and scroll down to App Credentials. Click on Show next to the Signing Secret and copy that down as well.
  9) Next, open up the code hosted in this repo and navigate your terminal to it.
  10) When you're within the virtual environment (Using an IDE like PyCharm will set this up automatically for you), type into your terminal:
        $ export SLACK_TOKEN="paste your bot user oauth access token here"
  9) You can test that the environment has this variable by typing: 'echo $SLACK_TOKEN' into your terminal.
  10) Next, type into your terminal:
        $ export SLACK_EVENTS_TOKEN="paste your Signing Secret here"
  11) You can test that the environment has this variable by typing: 'echo $SLACK_EVENTS_TOKEN' into your terminal.
  12) Now run the app by typing into your terminal:
        $ python3 ipbot_main.py
  14) Once you've opened up a port locally on your machine, then return to the Slack API Control Panel and head to the Event Subscriptions tab.
  15) Enable Events and type in your IPv4 address with '/slack/events' tacked on the end of it. To find your public IPv4 address, you can use: https://whatismyipaddress.com/.  
  16) After passing Slack's challenge request, you can create new Bot User Events. 
  17) Type in 'message.channels' to add an event for when a message is posted in a channel. 
  18) You'll have to reinstall your app if any permissions have been changed. 
  19) Once the app has been reinstalled, you should now be able to see it running in your channel. Type in an IP and you should see a response with information on that IP.
