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
        manager.listar_tarefas()
        print("\n--- Opções ---")
        print("1. Adicionar Tarefa")
        print("2. Mudar Status da Tarefa")
        print("3. Mudar Descricao da Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair do programa")

        choice = input("Selecione uma opção: ")

        if choice == "1":
            system("cls") if name == "nt" else system("clear")
            manager.criar_tarefa()
            system("cls") if name == "nt" else system("clear")

        elif choice == "2":
            system("cls") if name == "nt" else system("clear")
            manager.mudar_status()

        elif choice == "3":
            system("cls") if name == "nt" else system("clear")
            manager.editar_tarefa()

        elif choice == "4":
            system("cls") if name == "nt" else system("clear")
            manager.excluir_tarefa()

        elif choice == "5":
            system("cls") if name == "nt" else system("clear")
            print("Até mais!")
            break

        else:
            system("cls") if name == "nt" else system("clear")


if __name__ == "__main__":
    main()
