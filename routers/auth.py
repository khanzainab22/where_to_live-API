from fastapi import APIRouter
 
router = APIRouter(prefix="/auth", tags=["Auth"])
 
@router.post("/signup")
def signup():
    return {"message": "signup - TODO"}
 
@router.post("/login")
def login():
    return {"message": "login - TODO"}
 
@router.get("/profile")
def profile():
    return {"message": "protected profile - TODO"}