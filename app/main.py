from fastapi import FastAPI
from agents.linkedin_agent import generate_post

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is running"}

@app.post("/agent")
def run_agent(data: dict):
    user_input = data["input"]
    output = generate_post(user_input)
    return {"result": output}