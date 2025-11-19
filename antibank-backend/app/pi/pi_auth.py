import base64
import json
import hmac
import hashlib
from fastapi import HTTPException

def verify_pi_payment(payload: dict, secret_key: str):
    expected_signature = payload.get("signature")
    if not expected_signature:
        raise HTTPException(status_code=400, detail="Missing signature")

    raw_data = json.dumps(payload["payment"]).encode("utf-8")

    signed = hmac.new(
        secret_key.encode("utf-8"),
        raw_data,
        hashlib.sha256
    ).hexdigest()

    if signed != expected_signature:
        raise HTTPException(status_code=403, detail="Invalid signature")

    return True
