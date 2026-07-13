from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "'WELCOME TO WHERETOLIVE 1.0"}

