import os
import requests
import json


class IPBot:
    IP_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Info on your posted IP Address... \n\n"
        },
    }

    def __init__(self, channel):
        self.channel = channel

    def _get_IP_info(self, ip_address):
        api_key = os.environ.get("APIKEY")
        virustotal_url = 'https://virustotal.com/vtapi/v2/url/report'
        params = {'apikey': api_key,  # Virustotal API key exported to OS for security reasons
                  'resource': 'https://' + ip_address}
        r = requests.get(virustotal_url, params=params)
        initial_response = r.json()

        formatted_string = "No response from VirusTotal.\n"

        if initial_response['response_code'] == 0:
            formatted_string = ip_address + " is not in VirusTotal's IP database."

        if initial_response['response_code'] == 1:
            formatted_string = f"""
                IP Address: {initial_response['url']}
                Date IP address was last scanned: {initial_response['scan_date']}
                Total number of scans: {initial_response['total']}
                Positive detections: {initial_response['positives']}
                """

        formatted_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": formatted_string
            },
        }
        return formatted_block

    def create_message(self, ip_address):
        return \
            {
                "channel": self.channel,
                "blocks":
                    [
                        self.IP_BLOCK,
                        self._get_IP_info(ip_address),
                    ],
            }
