from fastapi import FastAPI, HTTPException
from logic import normalize_username

app = FastAPI()

@app.post("/normalize-username")
def normalize(username: str):
    result = normalize_username(username)
    if result is None:
        raise HTTPException(status_code=400, detail= "Invalid Username")
    return {"Normalized Username: ": result}