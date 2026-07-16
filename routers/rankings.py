from fastapi import APIRouter
 
router = APIRouter(prefix="/rankings", tags=["Rankings"])
 
@router.get("/")
def overall_rankings():
    return {"message": "overall rankings - TODO"}
 
@router.get("/state/{state}")
def state_rankings(state: str):
    return {"message": f"rankings for {state} - TODO"}
 
@router.get("/compare")
def compare_cities(city1: str, city2: str):
 return {"message": f"compare {city1} vs {city2} - TODO"}
 