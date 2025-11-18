import time
import jwt
import os

SECRET = os.getenv("JWT_SECRET", "CHANGE_ME")

class Auth:
    def generate(self, user_id):
        payload = {
            "user_id": user_id,
            "exp": int(time.time()) + 86400
        }
        return jwt.encode(payload, SECRET, algorithm="HS256")

    def verify(self, token):
        try:
            data = jwt.decode(token, SECRET, algorithms=["HS256"])
            return {"valid": True, "user_id": data["user_id"]}
        except:
            return {"valid": False}

auth = Auth()
