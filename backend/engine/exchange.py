import requests
import os
import time

class ExchangeEngine:
    def __init__(self):
        self.rates = {"PI_USD": 0.30}  # placeholder: dynamic later

    def get_rate(self, currency):
        if currency == "USD":
            return self.rates["PI_USD"]
        else:
            return self.convert_from_usd(currency)

    def convert_from_usd(self, currency):
        # public forex API
        url = f"https://open.er-api.com/v6/latest/USD"
        data = requests.get(url).json()
        if "rates" not in data:
            return None
        return data["rates"].get(currency, None)

    def pi_to_fiat(self, pi_amount, currency):
        rate = self.get_rate(currency)
        return pi_amount * rate

    def fiat_to_pi(self, fiat_amount, currency):
        rate = self.get_rate(currency)
        return fiat_amount / rate

exchange_engine = ExchangeEngine()
