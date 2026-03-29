from env.environment import EmailEnv
from env.models import Action
from env.tasks import grade_easy, grade_medium, grade_hard

env = EmailEnv()
obs = env.reset()

done = False

while not done:
    action = Action(
        type="reply",
        email_id="1",
        content="ok"
    )

    obs, reward, done, _ = env.step(action)

state = env.state()

print("Easy score:", grade_easy(state))
print("Medium score:", grade_medium(state))
print("Hard score:", grade_hard(state))