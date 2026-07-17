from fastapi import FastAPI
from sqlmodel import SQLModel
from sqlalchemy.exc import OperationalError
 
from database import engine
 
# Import models so SQLModel registers them
from models.city import City, CityMetric
from models.user import User
from models.comparison import SavedComparison
 
from routers import cities, auth, rankings, ai, comparisons
 
app = FastAPI()
 
 
@app.on_event("startup")
def on_startup():
    try:
        SQLModel.metadata.create_all(engine)
        print("Database Connected Successfully!")
    except OperationalError as e:
        print("Database Connection Failed:", e)
 
 
@app.get("/")
def home():
    return {"message": "Welcome to the WHERE TO LIVE 1.0"}
 
 
app.include_router(cities.router)
app.include_router(auth.router)
app.include_router(rankings.router)
app.include_router(ai.router)
app.include_router(comparisons.router)
 