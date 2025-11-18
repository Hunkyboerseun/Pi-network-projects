import uuid
import time
from integration.pi_network import pi_network
from engine.exchange import exchange_engine
from engine.fiat_wallet import fiat_wallet

class MerchantFlow:
    def __init__(self):
        self.invoices = {}

    def create_invoice(self, user_id, amount_fiat, currency="USD"):
        invoice_id = str(uuid.uuid4())
        pi_amount = exchange_engine.fiat_to_pi(amount_fiat, currency)

        self.invoices[invoice_id] = {
            "invoice_id": invoice_id,
            "user_id": user_id,
            "fiat_amount": amount_fiat,
            "currency": currency,
            "pi_amount": pi_amount,
            "status": "pending"
        }
        return self.invoices[invoice_id]

    def verify_payment(self, invoice_id, payment_id):
        result = pi_network.verify_payment(payment_id)
        if "status" in result and result["status"] == "completed":
            self.invoices[invoice_id]["status"] = "paid"
            return result
        return {"error": "not_paid"}

    def finalize(self, invoice_id):
        data = self.invoices[invoice_id]
        fiat_wallet.add(data["user_id"], data["fiat_amount"])
        return {"status": "success"}

merchant_flow = MerchantFlow()
