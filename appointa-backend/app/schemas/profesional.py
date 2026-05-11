from datetime import datetime, date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ProfesionalBase(BaseModel):
    specialty: str = Field(..., min_length=2)
    license_number: Optional[str] = None
    experience_years: Optional[int] = Field(None, ge=0)
    bio: Optional[str] = None
    consultation_fee: Optional[Decimal] = Field(None, ge=0)


class ProfesionalCreate(ProfesionalBase):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=2)
    phone: Optional[str] = None


class ProfesionalUpdate(ProfesionalBase):
    full_name: Optional[str] = Field(None, min_length=2)
    phone: Optional[str] = None


class ProfesionalResponse(ProfesionalBase):
    id: int
    email: str
    full_name: str
    phone: Optional[str]
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
