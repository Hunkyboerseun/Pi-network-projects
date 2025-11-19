from pydantic import BaseModel

class Deposit(BaseModel):
    amount: float

class Withdraw(BaseModel):
    amount: float
