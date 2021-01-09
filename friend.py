import datetime

from typing import List, Optional, Tuple, Dict
from pydantic import BaseModel

class Friend(BaseModel):
    #id: int
    name: str
    birthdate: datetime.date
    allergies: Optional[str]
    pronouns: Optional[str]
    avatar: Optional[str]
    optional1: Optional[Dict[str,List[str]]]
    optional2: Optional[Dict[str,List[str]]]
    optional3: Optional[Dict[str,List[str]]]
    optional4: Optional[Dict[str,List[str]]]
