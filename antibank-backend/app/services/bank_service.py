from app.database import db

def deposit(amount: float):
    db["balance"] += amount
    db["transactions"].append({"type": "deposit", "amount": amount})
    return db["balance"]

def withdraw(amount: float):
    if amount > db["balance"]:
        return None
    db["balance"] -= amount
    db["transactions"].append({"type": "withdraw", "amount": amount})
    return db["balance"]

def get_balance():
    return db["balance"]

def get_transactions():
    return db["transactions"]
