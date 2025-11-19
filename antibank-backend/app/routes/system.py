from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/routes")
def list_routes():
    return {
        "routes": [
            "/", 
            "/balance",
            "/transactions/deposit",
            "/transactions/withdraw",
            "/transactions/",
            "/system/routes"
        ]
    }
