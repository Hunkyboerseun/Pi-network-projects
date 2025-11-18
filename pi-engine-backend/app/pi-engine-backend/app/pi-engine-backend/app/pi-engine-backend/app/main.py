from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import state
from .simulate import simulate

app = FastAPI(title="Pi Financial Engine", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Pi Engine API running"}

@app.get("/api/rates")
def get_rates():
    return {
        "pi_price": state.pi_price,
        "pi_supply": state.pi_supply
    }

@app.post("/api/simulate")
def simulate_endpoint(days: int = 30, btc_influence: float = 0.05, volatility: float = 0.03):
    return simulate(days, btc_influence, volatility)
