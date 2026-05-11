from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models.user import User
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteResponse, ClienteUpdate
from app.api.deps import get_current_cliente
from app.core.security import get_password_hash

router = APIRouter()


@router.get("/me", response_model=ClienteResponse)
async def get_my_profile(
    current_user: User = Depends(get_current_cliente),
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(Cliente.user_id == current_user.id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente profile not found"
        )
    
    return ClienteResponse(
        id=cliente.id,
        email=current_user.email,
        full_name=current_user.full_name,
        phone=current_user.phone,
        dni=cliente.dni,
        date_of_birth=cliente.date_of_birth,
        address=cliente.address,
        city=cliente.city,
        notes=cliente.notes,
        created_at=current_user.created_at,
        updated_at=current_user.updated_at
    )


@router.put("/me", response_model=ClienteResponse)
async def update_my_profile(
    profile_update: ClienteUpdate,
    current_user: User = Depends(get_current_cliente),
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(Cliente.user_id == current_user.id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente profile not found"
        )
    
    # Update user fields
    if profile_update.full_name is not None:
        current_user.full_name = profile_update.full_name
    if profile_update.phone is not None:
        current_user.phone = profile_update.phone
    
    # Update cliente fields
    if profile_update.dni is not None:
        cliente.dni = profile_update.dni
    if profile_update.date_of_birth is not None:
        cliente.date_of_birth = profile_update.date_of_birth
    if profile_update.address is not None:
        cliente.address = profile_update.address
    if profile_update.city is not None:
        cliente.city = profile_update.city
    if profile_update.notes is not None:
        cliente.notes = profile_update.notes
    
    db.commit()
    db.refresh(current_user)
    db.refresh(cliente)
    
    return ClienteResponse(
        id=cliente.id,
        email=current_user.email,
        full_name=current_user.full_name,
        phone=current_user.phone,
        dni=cliente.dni,
        date_of_birth=cliente.date_of_birth,
        address=cliente.address,
        city=cliente.city,
        notes=cliente.notes,
        created_at=current_user.created_at,
        updated_at=current_user.updated_at
    )


@router.patch("/me", response_model=ClienteResponse)
async def partial_update_my_profile(
    profile_update: ClienteUpdate,
    current_user: User = Depends(get_current_cliente),
    db: Session = Depends(get_db)
):
    return await update_my_profile(profile_update, current_user, db)
