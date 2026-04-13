from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from models import Tarefa


class TaskRepository:
    def __init__(self, engine: Engine):
        self.engine = engine

    def criar_tarefa(self, descricao):
        tarefa = Tarefa(descricao=descricao, status="Pendente")

        with Session(self.engine) as session:
            try:
                session.add(tarefa)
                session.flush()
                session.commit()

            except Exception as e:
                print(f"Erro {e} ao criar tarefa")
                return e

    def get_tarefas(self) -> list[Task]:
        with Session(self.engine) as session:
            try:
                tarefas = session.scalars(select(Tarefa)).all()
                return list(tarefas)

            except Exception as e:
                print(f"Erro{e} ao listar tarefas")
                return []

    def get_tarefa_por_id(self, id_tarefa: int) -> Tarefa | None:
        with Session(self.engine) as session:
            try:
                result = session.execute(select(Tarefa).where(Tarefa.id == id_tarefa))
                session.flush()
                for row in result:
                    return row[0]

            except Exception as e:
                print(f"Erro{e} ao buscar tarefa pelo id {id}")
                return None

    def atualizar_tarefa(self, id_tarefa: int, nova_desc: str):
        with Session(self.engine) as session:
            tarefa = self.get_tarefa_por_id(id_tarefa)
            tarefa.descricao = nova_desc

            try:
                session.add(tarefa)
                session.flush()
                session.commit()

            except Exception as e:
                print(f"Erro {e} ao atualizar tarefa")

    def atualizar_status(self, id_tarefa: int, novo_status: str):
        with Session(self.engine) as session:
            tarefa = self.get_tarefa_por_id(id_tarefa)
            tarefa.status = novo_status

            try:
                session.add(tarefa)
                session.flush()
                session.commit()

            except Exception as e:
                print(f"Erro {e} ao atualizar tarefa")

    def excluir_tarefa(self, id_tarefa: int):
        with Session(self.engine) as session:
            tarefa = self.get_tarefa_por_id(id_tarefa)

            try:
                session = Session(self.engine)
                session.delete(tarefa)
                session.commit()

            except Exception as e:
                print(f"Erro {e} ao deletar tarefa")
