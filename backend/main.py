from security.auth import auth
from engine.fiat_wallet import fiat_wallet
from engine.exchange import exchange_engine
from payments.merchant_flow import merchant_flow
@app.get("/exchange/rate/{currency}")
def get_rate(currency: str):
    return {"rate": exchange_engine.get_rate(currency)}

@app.get("/wallet/{user_id}")
def balance(user_id: str):
    return fiat_wallet.balance(user_id)

@app.post("/wallet/add/{user_id}/{amount}")
def add_to_wallet(user_id: str, amount: float):
    return fiat_wallet.add(user_id, amount)

@app.post("/merchant/invoice/{user_id}/{amount}")
def invoice(user_id: str, amount: float, currency: str = "USD"):
    return merchant_flow.create_invoice(user_id, amount, currency)

@app.post("/merchant/verify/{invoice_id}/{payment_id}")
def verify(invoice_id: str, payment_id: str):
    return merchant_flow.verify_payment(invoice_id, payment_id)

@app.post("/merchant/finalize/{invoice_id}")
def finalize(invoice_id):
    return merchant_flow.finalize(invoice_id)
