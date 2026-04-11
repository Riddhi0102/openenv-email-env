from typing import Any, Dict
from .models import Action


class EmailEnv:

    def __init__(self):
        self.sent_emails = []
        self.current_task = "easy"

    def reset(self, task: str = "easy"):
        self.current_task = task
        self.sent_emails = []
        return {}

    def step(self, action: Action):
        if action.type == "reply":
            self.sent_emails.append(action.content)

        reward = 0.0

        if self.current_task == "easy":
            done = len(self.sent_emails) >= 1
        elif self.current_task == "medium":
            done = len(self.sent_emails) >= 2
        else:
            done = len(self.sent_emails) >= 3

        return {}, reward, done, {}

    def state(self) -> Dict[str, Any]:
        return {
            "sent_emails": self.sent_emails,
            "task": self.current_task
        }