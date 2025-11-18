from .models import state
import random

def simulate(days: int, btc_influence: float, volatility: float):
    results = []

    for day in range(days):
        btc_factor = (random.random() - 0.5) * btc_influence
        random_factor = (random.random() - 0.5) * volatility

        price_change = btc_factor + random_factor
        state.pi_price = max(0.1, state.pi_price * (1 + price_change))

        supply_change = int(abs(price_change * 50000))
        state.pi_supply += supply_change

        results.append({
            "day": day,
            "price": round(state.pi_price, 4),
            "supply": state.pi_supply
        })

    return results
