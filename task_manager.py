from repository import TaskRepository
from models import Tarefa
from os import system, name


class TaskManager:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def listar_tarefas(self):
        tarefas = self.repository.get_tarefas()  # Atualiza a lista de tarefas

        print("\n--- Lista de Tarefas ---")
        for i, tarefa in enumerate(tarefas):
            status = "[ ]" if tarefa.status == "Pendente" else "[X]"
            print(f"{i + 1} - {status} - {tarefa.descricao}")
        print("\n")

    def criar_tarefa(self):
        self.listar_tarefas()
        descricao = input("Qual a descricao da tarefa? \n")
        self.repository.criar_tarefa(descricao)

    def editar_tarefa(self):
        self.listar_tarefas()
        idx_tarefa = int(
            input("Digite o numero da tarefa que deseja editar, ou 0 para cancelar: \n")
        )

        if idx_tarefa == 0:
            return

        # Verifica se o numero da tarefa a editar eh valido
        tarefas = self.repository.get_tarefas()
        while idx_tarefa - 1 not in range(len(tarefas)):
            idx_tarefa = int(input("Digite um numero de tarefa valido!"))

        nova_desc = input("Digite a nova descricao da tarefa: \n")
        id_tarefa = tarefas[idx_tarefa - 1].id

        self.repository.atualizar_tarefa(id_tarefa, nova_desc)
        system("cls") if name == "nt" else system("clear")  # Limpa o console

    def mudar_status(self):
        self.listar_tarefas()

        idx_tarefa = int(
            input(
                "Digite o numero da tarefa que deseja mudar o status, ou 0 para cancelar: \n"
            )
        )

        if idx_tarefa == 0:
            return

        # Verifica se o numero da tarefa a editar eh valido
        tarefas = self.repository.get_tarefas()
        while idx_tarefa - 1 not in range(len(tarefas)):
            idx_tarefa = int(input("Digite um numero de tarefa valido!"))

        tarefa_status = (
            "Pendente" if tarefas[idx_tarefa - 1].status == "Concluído" else "Concluído"
        )
        id_tarefa = tarefas[idx_tarefa - 1].id
        print(id_tarefa)

        self.repository.atualizar_status(id_tarefa, tarefa_status)
        system("cls") if name == "nt" else system("clear")  # Limpa o console

    def excluir_tarefa(self):
        self.listar_tarefas()

        idx_tarefa = int(
            input(
                "Digite o numero da tarefa que deseja excluir, ou 0 para cancelar: \n"
            )
        )

        if idx_tarefa == 0:
            return

        # Verifica se o numero da tarefa a editar eh valido
        tarefas = self.repository.get_tarefas()
        while idx_tarefa - 1 not in range(len(tarefas)):
            idx_tarefa = int(input("Digite um numero de tarefa valido!"))

        confirmacao = ""
        while confirmacao.lower() not in ["s", "n"]:
            confirmacao = input(
                f"Tem certeza que deseja excluir a tarefa {idx_tarefa}? [s/n]: "
            )

        if confirmacao == "s":
            id_tarefa = tarefas[idx_tarefa - 1].id
            self.repository.excluir_tarefa(id_tarefa)
            system("cls") if name == "nt" else system("clear")  # Limpa o console

        else:
            system("cls") if name == "nt" else system("clear")  # Limpa o console
            self.excluir_tarefa()
