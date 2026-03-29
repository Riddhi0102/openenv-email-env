from .models import Email, Observation, Action


class EmailEnv:

    def __init__(self):
        self.reset()

    def reset(self):

        self.inbox = [
            Email(
                id="1",
                sender="boss@company.com",
                subject="Urgent meeting",
                body="Join immediately",
                urgency=5,
                requires_reply=True
            )
        ]

        self.responses = {}
        self.step_count = 0

        return self.state()

    def state(self):
        return Observation(
            inbox=self.inbox,
            drafted_responses=self.responses,
            step_count=self.step_count
        )

    def step(self, action: Action):

        reward = 0
        done = False

        self.step_count += 1

        if action.type == "reply":
            self.responses[action.email_id] = action.content
            reward = 1.0

        if self.step_count >= 3:
            done = True

        return self.state(), reward, done, {}