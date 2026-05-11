from sqlalchemy import String, Text, ForeignKey, Integer, Numeric, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin
from app.models.user import User


class Profesional(Base, TimestampMixin):
    __tablename__ = "profesionales"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    specialty: Mapped[str] = mapped_column(String(100))  # Especialidad
    license_number: Mapped[str | None] = mapped_column(String(50), nullable=True)  # Matrícula
    experience_years: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    consultation_fee: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    
    user: Mapped["User"] = relationship(backref="profesional")
