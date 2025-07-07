from pydantic import BaseModel, Field, validator
import re

class UserCreate(BaseModel):
    id: str = Field(..., min_length=9, max_length=9, description="Israeli ID")
    name: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)
    address: str = Field(..., min_length=1)

    @validator('id')
    def validate_israeli_id(cls, value):
        if not value.isdigit() or len(value) != 9:
            raise ValueError("ID must be a 9-digit number.")
        return value

    @validator('phone')
    def validate_phone(cls, value):
        if not re.match(r'^\+\d{9,15}$', value):
            raise ValueError("Phone number must be in international format, e.g. +972...")
        return value
