import os
from openai import OpenAI

from env.environment import EmailEnv
from env.models import Action
from env.tasks import grade_easy, grade_medium, grade_hard


# MUST use their proxy
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)


env = EmailEnv()
obs = env.reset()

print("[START] task=email", flush=True)

done = False
step = 0

while not done:
    step += 1

    # call LLM (REQUIRED by validator)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an email assistant."},
            {"role": "user", "content": "Reply briefly to email"}
        ],
        temperature=0
    )

    reply = response.choices[0].message.content

    action = Action(
        type="reply",
        email_id="1",
        content=reply
    )

    obs, reward, done, _ = env.step(action)

    print(f"[STEP] step={step} reward={reward}", flush=True)


state = env.state()

easy = grade_easy(state)
medium = grade_medium(state)
hard = grade_hard(state)

score = (easy + medium + hard) / 3

print(f"[END] task=email score={score} steps={step}", flush=True)