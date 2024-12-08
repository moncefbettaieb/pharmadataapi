from sqlalchemy import Table, Column, Integer, String, MetaData
from app.db.base import Base

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("email", String, unique=True, index=True),
    Column("hashed_password", String, nullable=False),
    Column("subscription_level", String, default="free", nullable=False),
    Column("quota", Integer, default=100, nullable=False),
    Column("usage", Integer, default=0, nullable=False)
)
