from dataclasses import dataclass
from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


@dataclass
class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, name={self.name}, description={self.description})"
