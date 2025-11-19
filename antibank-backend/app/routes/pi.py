from fastapi import APIRouter, Depends
from app.pi.pi_auth import verify_pi_payment
from app.services.bank_service import deposit
import os

router = APIRouter(prefix="/pi", tags=["Pi Network"])

PI_APP_SECRET = os.getenv("PI_APP_SECRET", "test_secret")

@router.post("/payment-complete")
def pi_payment_complete(payload: dict):
    verify_pi_payment(payload, PI_APP_SECRET)

    amount = float(payload["payment"]["amount"])
    deposit(amount)

    return {
        "status": "success",
        "credited_amount": amount
    }
