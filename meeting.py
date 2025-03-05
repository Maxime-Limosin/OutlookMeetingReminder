from dataclasses import dataclass
from exchangelib.ewsdatetime import EWSDateTime

@dataclass
class Meeting:
    title:str = ""
    start: EWSDateTime = None
    end: EWSDateTime = None
    isCancelled: bool = False
    organizer: str = ""
        
    def getDay(self)-> str:
        return self.start.strftime('%a %d/%m')
    
    def getStart(self) -> str:
        return self.start.strftime('%Hh%M')
        
    def getEnd(self) -> str:
        return self.end.strftime('%Hh%M')