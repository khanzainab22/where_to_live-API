from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models.city import City, CityMetric
router = APIRouter(prefix="/cities", tags=["Cities"])
@router.get("/")
def list_cities(session: Session = Depends(get_session)):
    return session.exec(select(City)).all()

 
@router.get("/{city_id}")
def get_city(city_id: int, session: Session= Depends(get_session)):
    city = session.get(City, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City nahi mili")
    return city
 
@router.post("/")
def add_city():
    return {"message": "add city - TODO (admin only)"}
 
@router.put("/{city_id}")
def update_city(city_id: int):
    return {"message": f"update city {city_id} - TODO"}
 
@router.get("/{city_id}/history")
def city_history(city_id: int, session: Session = Depends(get_session)):
    statement = select(CityMetric).where(CityMetric.city_id == city_id)
    return session.exec(statement).all()