from pydantic import BaseModel

class SubscriptionUpdate(BaseModel):
    level: str

class SubscriptionStatus(BaseModel):
    subscription_level: str
    usage: int
    quota: int
    remaining: int
