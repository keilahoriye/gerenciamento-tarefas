from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from models import Tarefa


class TaskRepository:
    def __init__(self, engine: Engine):
        # The repository takes the database engine so it can create sessions
        self.engine = engine

    def criar_tarefa(self, descricao):
        tarefa = Tarefa(descricao=descricao, status="Pendente")

        try:
            session = Session(self.engine)
            session.add(tarefa)
            session.flush()
            session.commit()

        except Exception as e:
            print(f"Erro {e} ao criar tarefa")
            return e

    def get_tarefas(self) -> list[Task]:
        try:
            session = Session(self.engine)
            tarefas = session.scalars(select(Tarefa)).all()
            return list(tarefas)

        except Exception as e:
            print(f"Erro{e} ao listar tarefas")
            return []

        pass

    def get_task_by_id(self, task_id: int):
        """Queries a specific task by its ID."""
        pass

    def atualizar_tarefa(self, id_tarefa: int, nova_desc: str):
        """Finds a task and updates its status."""
        pass

    def atualizar_status(self, id_tarefa: int, novo_status: str):
        pass

    def excluir_tarefa(self, id_tarefa: int):
        """Finds a task and deletes it."""
        pass
