import requests
import sys

BASE = "http://localhost:7860"

def main():
    task = "email_env"

    print(f"[START] task={task}", flush=True)

    # reset
    r = requests.post(f"{BASE}/reset")
    obs = r.json()

    done = False
    step = 0
    total_reward = 0

    while not done and step < 5:
        action = {
            "type": "reply",
            "email_id": "1",
            "content": "Confirmed"
        }

        r = requests.post(f"{BASE}/step", json=action)
        data = r.json()

        reward = data["reward"]
        done = data["done"]

        step += 1
        total_reward += reward

        print(f"[STEP] step={step} reward={reward}", flush=True)

    print(
        f"[END] task={task} score={total_reward} steps={step}",
        flush=True
    )


if __name__ == "__main__":
    main()