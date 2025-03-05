from typing import List

from config import Config
from meetingManager import MeetingManager
from meeting import Meeting
from chatmessagesender import ChatMessageSender

YAML_FILE_NAME = 'conf.yml'

def main():
    meetings: List[Meeting] = []
    
    # Load user settings from the yaml file
    config = Config(YAML_FILE_NAME)
    email = config.outlookEmail 
    password = config.outlookPassword
    outlookServerAddress =  config.outlookServerAddress
    
    # Create an object to retrived meetings from the email server
    meetingManager = MeetingManager(email, password, outlookServerAddress)
    meetings = meetingManager.getMeetingsWithinDays()
    
    # Create an object to interact with SynologyChat
    chatMessageSender = ChatMessageSender(config.synologyWebhookToken)
    
    if meetings == None:
        return
    
    for m in meetings:
        message = f"Réunion {m.title}, le {m.getDay()}, de {m.getStart()} à {m.getEnd()}, organisée par {m.organizer}"
        chatMessageSender.sendChatMessage(message)


if __name__ == "__main__":
    main()
