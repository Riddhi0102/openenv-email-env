import os
from openai import OpenAI

from env.environment import EmailEnv
from env.models import Action
from env.tasks import grade_easy, grade_medium, grade_hard


# REQUIRED ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

TASK_NAME = "email"
BENCHMARK = "openenv-email"
MAX_STEPS = 5


def log_start():
    print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}", flush=True)


def log_step(step, action, reward, done, error):
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True
    )


def main():
    client = OpenAI(
        base_url=API_BASE_URL,
        api_key=API_KEY
    )

    env = EmailEnv()

    rewards = []
    steps = 0
    success = False
    score = 0.0

    log_start()

    try:
        obs = env.reset()
        done = False

        while not done and steps < MAX_STEPS:
            steps += 1

            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": "Reply briefly to email"},
                        {"role": "user", "content": "Write short professional reply"}
                    ],
                    temperature=0,
                    max_tokens=50,
                )

                reply = response.choices[0].message.content.strip()

            except Exception as e:
                reply = "ok"

            action = Action(
                type="reply",
                email_id="1",
                content=reply
            )

            obs, reward, done, _ = env.step(action)

            reward = float(reward or 0.0)
            rewards.append(reward)

            log_step(
                step=steps,
                action="reply",
                reward=reward,
                done=done,
                error=None
            )

        state = env.state()

        easy = grade_easy(state)
        medium = grade_medium(state)
        hard = grade_hard(state)

        score = (easy + medium + hard) / 3
        score = max(0.0, min(1.0, score))

        success = score > 0

    except Exception as e:
        success = False

    finally:
        log_end(success, steps, score, rewards)


if __name__ == "__main__":
    main()