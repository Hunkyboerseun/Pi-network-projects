from fastapi import APIRouter

router = APIRouter(tags=["Fiat Wallet"])

# In-memory demo wallet (replace with PostgreSQL later)
fiat_wallet = {"USD": 0.00, "ZAR": 0.00, "EUR": 0.00}

@router.get("/balance")
def wallet_balance():
    return fiat_wallet

@router.post("/load")
def load_fiat(currency: str, amount: float):
    if currency not in fiat_wallet:
        return {"error": "Unsupported currency"}

    fiat_wallet[currency] += amount
    return {"status": "loaded", "currency": currency, "amount": amount}

@router.post("/pay")
def pay_merchant(currency: str, amount: float):
    if currency not in fiat_wallet:
        return {"error": "Unsupported currency"}
    if fiat_wallet[currency] < amount:
        return {"error": "Insufficient funds"}

    fiat_wallet[currency] -= amount
    return {"status": "paid", "currency": currency, "amount": amount}
