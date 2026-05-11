from datetime import datetime, date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ClienteBase(BaseModel):
    dni: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    city: Optional[str] = None
    notes: Optional[str] = None


class ClienteCreate(ClienteBase):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=2)
    phone: Optional[str] = None


class ClienteUpdate(ClienteBase):
    full_name: Optional[str] = Field(None, min_length=2)
    phone: Optional[str] = None


class ClienteResponse(ClienteBase):
    id: int
    email: str
    full_name: str
    phone: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
