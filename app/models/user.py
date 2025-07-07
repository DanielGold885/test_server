from sqlalchemy import Column, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(9), primary_key=True, index=True)                # Israeli ID is 9 digits
    name = Column(String(100), nullable=False)                          # Reasonable name length
    phone = Column(String(15), nullable=False)                          # E.164 format
    address = Column(String(200), nullable=False)                       # Street/address

