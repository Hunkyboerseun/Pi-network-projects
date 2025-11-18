import requests
import time
import os

PI_API_BASE = "https://api.minepi.com"
PI_API_KEY = os.getenv("PI_API_KEY")

class PiNetwork:
    def __init__(self):
        self.api_key = PI_API_KEY

    def _headers(self):
        return {"Authorization": f"Key {self.api_key}"}

    def verify_payment(self, payment_id: str):
        """Verify a Pi payment on-chain"""
        url = f"{PI_API_BASE}/v2/payments/{payment_id}"
        response = requests.get(url, headers=self._headers())
        return response.json()

    def approve(self, payment_id: str):
        """Approve a Pi payment"""
        url = f"{PI_API_BASE}/v2/payments/{payment_id}/approve"
        response = requests.post(url, headers=self._headers())
        return response.json()

    def complete(self, payment_id: str):
        """Complete the payment after merchant receives fiat"""
        url = f"{PI_API_BASE}/v2/payments/{payment_id}/complete"
        response = requests.post(url, headers=self._headers())
        return response.json()

pi_network = PiNetwork()
