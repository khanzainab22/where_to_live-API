from fastapi import APIRouter
 
router = APIRouter(prefix="/ai", tags=["AI"])
 
@router.post("/summary")
def ai_summary():
    return {"message": "AI comparison summary - TODO"}
 
@router.post("/recommend")
def ai_recommend():
    return {"message": "AI personalized recommendation - TODO"}