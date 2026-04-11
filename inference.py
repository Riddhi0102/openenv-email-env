from env.environment import EmailEnv
from env.models import Action
from env.tasks import grade_easy, grade_medium, grade_hard


def main():
    task = "email_env"

    print(f"[START] task={task}", flush=True)

    env = EmailEnv()
    obs = env.reset()

    done = False
    step = 0
    total_reward = 0

    while not done:
        action = Action(
            type="reply",
            email_id="1",
            content="ok"
        )

        obs, reward, done, _ = env.step(action)

        step += 1
        total_reward += reward

        print(f"[STEP] step={step} reward={reward}", flush=True)

    state = env.state()

    easy = grade_easy(state)
    medium = grade_medium(state)
    hard = grade_hard(state)

    final_score = (easy + medium + hard) / 3

    print(
        f"[END] task={task} score={final_score} steps={step}",
        flush=True
    )


if __name__ == "__main__":
    main()