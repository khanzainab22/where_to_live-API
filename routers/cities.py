from fastapi import APIRouter
router = APIRouter(prefix="/cities", tags=["Cities"])
@router.get("/")
def list_cities():
    return {"message": "list all cities - TODO"}
 
@router.get("/{city_id}")
def get_city(city_id: int):
    return {"message": f"get city {city_id} - TODO"}
 
@router.post("/")
def add_city():
    return {"message": "add city - TODO (admin only)"}
 
@router.put("/{city_id}")
def update_city(city_id: int):
    return {"message": f"update city {city_id} - TODO"}
 
@router.get("/{city_id}/history")
def city_history(city_id: int):
    return {"message": f"metrics history for city {city_id}"}