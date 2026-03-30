print("SERVER FILE LOADED")
from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action  # <--- IMPORTANT: Import your Action model

app = FastAPI()
env = EmailEnv()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/reset")
@app.post("/reset")
def reset():
    global env
    env = EmailEnv()
    return env.state()

@app.post("/step")
def step(action_data: dict):
    global env
    try:
        # Convert the dictionary from curl into the Action class object
        action_obj = Action(**action_data) 
        
        # Pass the object to the environment
        obs, reward, done, info = env.step(action_obj)
        
        return {
            "observation": obs,
            "reward": reward,
            "done": done,
            "info": info
        }
    except Exception as e:
        return {"error": str(e), "tip": "Ensure JSON matches Action model fields"}

@app.get("/state")
def get_state():
    return env.state()