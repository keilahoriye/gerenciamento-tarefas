from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(15))

    def __repr__(self):
        return f"<Task(id={self.id}, description='{self.description}', status='{self.status}')>"
