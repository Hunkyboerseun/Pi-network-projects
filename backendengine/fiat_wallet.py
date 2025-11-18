import time
import json

class FiatWallet:
    def __init__(self):
        self.wallets = {}   # user_id → wallet balance

    def create_wallet(self, user_id):
        if user_id not in self.wallets:
            self.wallets[user_id] = 0.0
        return {"status": "created", "balance": self.wallets[user_id]}

    def add(self, user_id, amount):
        self.wallets[user_id] += float(amount)
        return {"balance": self.wallets[user_id]}

    def deduct(self, user_id, amount):
        amount = float(amount)
        if self.wallets[user_id] < amount:
            return {"error": "insufficient_funds"}
        self.wallets[user_id] -= amount
        return {"balance": self.wallets[user_id]}

    def balance(self, user_id):
        return {"balance": self.wallets.get(user_id, 0.0)}

fiat_wallet = FiatWallet()
