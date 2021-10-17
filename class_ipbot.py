import os
import requests


class IPBot:
    IP_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Info on your posted IP Address... \n\n"
            ),
        },
    }

    def __init__(self, channel):
        self.channel = channel

    def _get_IP_info(self, ip_address):

        api_key = os.environ.get("APIKEY")
        url = 'https://virustotal.com/vtapi/v2/url/report'
        params = {'apikey': api_key,        # Virustotal API key exported to OS for security reasons
                  'resource': 'https://' + ip_address}
        r = requests.get(url, params=params)
        initial_response = r.json()
        formatted_response = f"""
            IP Address: {initial_response['url']}
            Date IP address was last scanned: {initial_response['scan_date']}
            Total number of scans: {initial_response['total']}
            Positive detections: {initial_response['positives']}
            Individual scans: {initial_response['scans']}
            """
        return formatted_response

    def create_message(self, ip_address):
        return \
            {
                "channel": self.channel,
                "blocks":
                    [
                        self.IP_BLOCK,
                        *self._get_IP_info(ip_address),
                    ],
            }

