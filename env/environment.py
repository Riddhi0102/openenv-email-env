from typing import Any, Dict
from .models import Action


class EmailEnv:

    def __init__(self):
        self.sent_emails = []

    # REQUIRED
    def reset(self):
        self.sent_emails = []
        return {}

    # REQUIRED
    def step(self, action: Action):
        if action.type == "reply":
            self.sent_emails.append(action.content)

        reward = 0.0
        done = len(self.sent_emails) >= 3

        return {}, reward, done, {}

    # REQUIRED
    def state(self) -> Dict[str, Any]:
        return {
            "sent_emails": self.sent_emails
        }

    # IMPORTANT — validator reads this
    @staticmethod
    def tasks():
        return [
            {
                "name": "easy",
                "grader": "env.tasks:grade_easy"
            },
            {
                "name": "medium",
                "grader": "env.tasks:grade_medium"
            },
            {
                "name": "hard",
                "grader": "env.tasks:grade_hard"
            }
        ]