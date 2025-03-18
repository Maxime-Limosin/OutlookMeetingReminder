import requests
import warnings
from typing import Dict

# Suppress InsecureRequestWarning that happens because of the verify=False
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Define the URL and token to our server
BERTHA_URL = 'https://bertha31.synology.me:5001/webapi/entry.cgi'

class ChatMessageSender:
    url: str = ""
    params: Dict[str, str] = None
    headers: Dict[str, str] = None
    
    def __init__(self, token):
        self.url = BERTHA_URL
        
        self.params = {
            'api': 'SYNO.Chat.External',
            'method': 'incoming',
            'version': '2',
            'token': token
        }
        
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'  # Ensuring the content type matches the curl request
        }
        
    def sendChatMessage(self, message: str) -> bool:   
        payload = '{"text": "' +  message + '"}'

        
        response = requests.post(self.url,
                                 params=self.params,
                                 data={'payload': payload},
                                 headers=self.headers,
                                 verify=False) # Don't verify as the server doesn't have SSL certificate up to date
    
        #print("Message sended", response.status_code)
        return response.status_code == 200
    