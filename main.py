from sqlalchemy import create_engine
from models import Base
from repository import TaskRepository
from task_manager import TaskManager
from os import system, name


def main():
    engine = create_engine("sqlite:///tasks.db")
    Base.metadata.create_all(engine)

    repo = TaskRepository(engine)
    manager = TaskManager(repo)
    system("cls") if name == "nt" else system("clear")  # Limpa o console

    while True:
        print("\n--- Lista de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Mudar Status da Tarefa")
        print("4. Sair do programa")

        choice = input("Selecione uma opção: ")

        if choice == "1":
            system("cls") if name == "nt" else system("clear")
            manager.criar_tarefa()
            system("cls") if name == "nt" else system("clear")
            print("Tarefa adicionada com sucesso!")

        elif choice == "2":
            system("cls") if name == "nt" else system("clear")
            manager.listar_tarefas()

        elif choice == "3":
            system("cls") if name == "nt" else system("clear")
            manager.mudar_status()

        elif choice == "4":
            system("cls") if name == "nt" else system("clear")
            print("Até mais!")
            break


if __name__ == "__main__":
    main()
