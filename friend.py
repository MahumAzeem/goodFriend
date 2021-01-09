import datetime

from typing import List, Optional
from pydantic import BaseModel

class Friend(BaseModel):
    def __init__(self):
        id: int
        first_name: str
        last_name: str
        birthdate: datetime.date
        allergies: Optional[List[str]]
        pronouns: Optional[List[str]]
        avatar: Optional[str]
        optional1: Optional[tuple(str,List[str])]
        optional2: Optional[tuple(str,List[str])]
        optional3: Optional[tuple(str,List[str])]
        optional4: Optional[tuple(str,List[str])]
        
