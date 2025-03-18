import os.path
from pathlib import Path
from typing import List

from config import Config
from meetingManager import MeetingManager
from meeting import Meeting
from chatMessageSender import ChatMessageSender

YAML_FILE_NAME = 'conf.yml'
PROJECT_FOLDER = 'MeetingReminder'

def main():
    confFilePath: str = ''
    meetings: List[Meeting] = []
    
    # Check if yaml file is in the same folder
    if os.path.isfile(YAML_FILE_NAME):
        confFilePath = YAML_FILE_NAME
    else:
        confFilePath = Path.home() / PROJECT_FOLDER / YAML_FILE_NAME # Otherwise, look in the home of the user, in the project folder	
    
    # Load user settings from the yaml file
    config = Config(confFilePath)
    email = config.outlookEmail 
    password = config.outlookPassword
    outlookServerAddress =  config.outlookServerAddress
    
    # Create an object to retrived meetings from the email server
    meetingManager = MeetingManager(email, password, outlookServerAddress)
    meetings = meetingManager.getMeetingsWithinDays()
    
    # Create an object to interact with SynologyChat
    chatMessageSender = ChatMessageSender(config.synologyWebhookToken)
    
    if meetings == None or len(meetings) == 0:
        return
    
    message: str = ""
    if len(meetings) == 1: # If there's only one meeting
        message = f"Réunion '{m.title}', le {m.getDay()}, de {m.getStart()} à {m.getEnd()}, organisée par {m.organizer}"
        
    else: # If there's some meetings
        for m in meetings:
            message += f"* Réunion *{m.title}* le {m.getDay()}, de {m.getStart()} à {m.getEnd()}, organisée par {m.organizer}\n"
            
    chatMessageSender.sendChatMessage(message) # Can only send one message at a time, so I added all them up into one string

if __name__ == "__main__":
    main()
