from fastapi import APIRouter
from app.models import Deposit, Withdraw
from app.services.bank_service import deposit, withdraw, get_transactions

router = APIRRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/deposit")
def deposit_route(data: Deposit):
    new_balance = deposit(data.amount)
    return {"status": "success", "new_balance": new_balance}

@router.post("/withdraw")
def withdraw_route(data: Withdraw):
    new_balance = withdraw(data.amount)
    if new_balance is None:
        return {"status": "error", "message": "Insufficient funds"}
    return {"status": "success", "new_balance": new_balance}

@router.get("/")
def list_transactions():
    return get_transactions()
