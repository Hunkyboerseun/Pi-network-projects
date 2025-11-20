import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "routes"))
from fastapi import FastAPI
from app.routes.balance import router as balance_routes
from app.routes.transactions import router as transaction_routes
from app.routes.system import router as system_routes

app = FastAPI(title="ANTIBANK Backend API")

app.include_router(balance_routes)
app.include_router(transaction_routes)
app.include_router(system_routes)

@app.get("/")
def home():
    return {"message": "Welcome to ANTIBANK Backend API"}
