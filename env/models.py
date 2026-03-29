from pydantic import BaseModel
from typing import List, Dict, Optional, Literal


class Email(BaseModel):
    id: str
    sender: str
    subject: str
    body: str
    urgency: int
    requires_reply: bool


class Observation(BaseModel):
    inbox: List[Email]
    drafted_responses: Dict[str, str]
    step_count: int


class Action(BaseModel):
    type: Literal["reply", "archive", "escalate"]
    email_id: str
    content: Optional[str] = None