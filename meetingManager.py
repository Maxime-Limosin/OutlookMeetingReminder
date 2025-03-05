from exchangelib import Credentials, Account, Configuration, DELEGATE
from exchangelib.ewsdatetime import UTC_NOW
from datetime import timedelta

from typing import List
from meeting import Meeting


class MeetingManager:
    email: str = ""
    password: str = ""
    server: str = ""
    account: Account = None
    isUserAutetified: bool = False

    def __init__(self, email: str, password: str, server: str):
        self.email = email
        self.password = password
        self.server = server
        
        self.autentifyUser()

    def autentifyUser(self) -> bool:
        if self.email == "" and self.password == "":
            self.isUserAutetified = False
            return False
        
        try:
            credentials = Credentials(self.email, self.password)
            config = Configuration(server=self.server, credentials=credentials)

            # Connect to the account with the configuration
            self.account = Account(
                self.email, 
                config=config, 
                autodiscover=False, 
                access_type=DELEGATE
            )
            self.isUserAutetified = True
            
        except Exception as e:
            self.isUserAutetified = False
            print(f"Failed to authenticate: {e}")
            print(self.email, self.password)
            
        finally:        
            return self.isUserAutetified

    def getMeetings(self) -> List[Meeting]:
        if not self.isUserAutetified:
            return None        
        
        meetings = []
        
        for item in self.account.calendar.filter(start__gte=UTC_NOW()):
            startTimeFr = item.start + timedelta(hours=1) # Convert UTC into UTC+1
            endTimeFr = item.end + timedelta(hours=1)  
            organizer = item.organizer.name
            
            m = Meeting(item.subject, startTimeFr, endTimeFr, item.is_cancelled, organizer)
            meetings.append(m)
            
        return meetings

    def getMeetingsWithinDays(self, days: int = 1) -> List[Meeting]:
        meetings = self.getMeetings()
        now = UTC_NOW()
        
        if meetings == None:
            return None
        
        return [m for m in meetings if (m.start - now).days > days]