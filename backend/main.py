from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ANTIBANK Backend API")

# -------------------------
# MODELS
# -------------------------

class Deposit(BaseModel):
    amount: float

class Withdraw(BaseModel):
    amount: float

# -------------------------
# TEMPORARY IN-MEMORY DATABASE
# -------------------------

db = {
    "balance": 0.0
}

# -------------------------
# ROUTES
# -------------------------

@app.get("/")
def home():
    return {"message": "Welcome to ANTIBANK Backend API"}

@app.get("/balance")
def get_balance():
    return {"balance": db["balance"]}

@app.post("/deposit")
def deposit_money(data: Deposit):
    db["balance"] += data.amount
    return {"status": "success", "new_balance": db["balance"]}

@app.post("/withdraw")
def withdraw_money(data: Withdraw):
    if data.amount > db["balance"]:
        return {"status": "error", "message": "Insufficient funds!"}
    db["balance"] -= data.amount
    return {"status": "success", "new_balance": db["balance"]}

@app.get("/routes")
def list_routes():
    return {
        "available_routes": [
            "/",
            "/balance",
            "/deposit",
            "/withdraw",
            "/routes"
        ]
    }
