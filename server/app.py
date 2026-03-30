from fastapi import FastAPI
from env.environment import EmailEnv

app = FastAPI()
env = EmailEnv()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
def reset():
    global env
    env = EmailEnv()
    return env._get_obs()


@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return env._get_obs()


def main():
    return app


if __name__ == "__main__":
    main()