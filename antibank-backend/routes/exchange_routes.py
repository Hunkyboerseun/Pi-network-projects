from fastapi import APIRouter

router = APIRouter(tags=["Exchange"])

# Temporary fixed rates (will replace with real rates from API)
exchange_rates = {
    "PI_to_ZAR": 60,
    "PI_to_USD": 3.1,
    "PI_to_EUR": 2.8
}

@router.get("/rates")
def get_rates():
    return exchange_rates

@router.post("/convert")
def convert_pi_to_fiat(pi_amount: float, currency: str):
    key = f"PI_to_{currency}"
    if key not in exchange_rates:
        return {"error": "Unsupported currency"}

    fiat_amount = pi_amount * exchange_rates[key]
    return {
        "pi_amount": pi_amount,
        "currency": currency,
        "fiat_amount": fiat_amount
    }
