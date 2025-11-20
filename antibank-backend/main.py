from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers (if you have them)
try:
    from routes.pi_routes import router as pi_routes
except:
    pi_routes = None

try:
    from routes.fiat_routes import router as fiat_routes
except:
    fiat_routes = None

# -------------------------------------------------------
# CREATE APP FIRST (must come BEFORE include_router)
# -------------------------------------------------------

app = FastAPI(
    title="ANTIBANK Backend",
    description="Backend service for Antibank + Pi Network Integration",
    version="1.0.0"
)

# -------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------
# ROUTES
# -------------------------------------------------------

# Only include routers if they exist
if pi_routes:
    app.include_router(pi_routes, prefix="/pi")

if fiat_routes:
    app.include_router(fiat_routes, prefix="/fiat")

# -------------------------------------------------------
# ROOT PATH
# -------------------------------------------------------

@app.get("/")
def home():
    return {"status": "OK", "service": "ANTIBANK backend running"}

