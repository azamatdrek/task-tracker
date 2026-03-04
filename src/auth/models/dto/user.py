from sqlalchemy import  String
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy.orm import  DeclarativeBase



class User(DeclarativeBase):
    username: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,

    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,

    )
    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=False,

    )
    display_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=False,

    )