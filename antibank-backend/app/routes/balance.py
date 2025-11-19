from fastapi import APIRouter
from app.services.bank_service import get_balance

router = APIRouter(prefix="/balance", tags=["Balance"])

@router.get("/")
def balance():
    return {"balance": get_balance()}
