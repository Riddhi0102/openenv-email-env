print("SERVER FILE LOADED")
from fastapi import FastAPI
from env.environment import EmailEnv

app = FastAPI()

# Initialize the environment globally
env = EmailEnv()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/reset")
def reset_get():
    global env
    # Re-initialize the environment and return the state
    env = EmailEnv()
    return env.state()

@app.post("/reset")
def reset_post():
    global env
    # Re-initialize the environment and return the state
    env = EmailEnv()
    return env.state()

@app.post("/step")
def step(action: dict):
    # Note: Ensure your EmailEnv.step() can handle a dictionary 
    # or wrap it in your Action model inside environment.py
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def get_state():
    return env.state()