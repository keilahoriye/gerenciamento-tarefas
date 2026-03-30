import sql


class ListaTarefas:
    def __init__(self):
        self.tarefas = sql.get_tarefas()

    def listar_tarefas(self):
        self.tarefas = sql.get_tarefas()  # Atualiza a lista de tarefas

        for i, tarefa in enumerate(self.tarefas):
            status = "[ ]" if tarefa.status == "Pendente" else "[X]"
            print(f"{i + 1} - {status} - {tarefa.descricao}")

    def criar_tarefa(self):
        descricao = input("Qual a descricao da tarefa? \n")
        sql.criar_tarefa(descricao)

    def editar_tarefa(self):
        self.listar_tarefas()
        idx_tarefa = int(
            input("Digite o numero da tarefa que deseja editar, ou 0 para cancelar: \n")
        )

        if idx_tarefa == 0:
            return

        # Verifica se o numero da tarefa a editar eh valido
        while idx_tarefa - 1 not in range(len(self.tarefas)):
            idx_tarefa = int(input("Digite um numero de tarefa valido!"))

        nova_desc = input("Digite a nova descricao da tarefa: \n")
        id_tarefa = self.tarefas[idx_tarefa - 1].id

        sql.atualizar_tarefa(id_tarefa, nova_desc)

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
        while idx_tarefa - 1 not in range(len(self.tarefas)):
            idx_tarefa = int(input("Digite um numero de tarefa valido!"))

        tarefa_status = (
            "Pendente"
            if self.tarefas[idx_tarefa].status == "Concluído"
            else "Concluído"
        )
        id_tarefa = self.tarefas[idx_tarefa - 1].id

        sql.atualizar_status(id_tarefa, tarefa_status)

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
        while idx_tarefa - 1 not in range(len(self.tarefas)):
            idx_tarefa = int(input("Digite um numero de tarefa valido!"))

        confirmacao = ""
        while confirmacao.lower() not in ["s", "n"]:
            confirmacao = input(
                f"Tem certeza que deseja excluir a tarefa {idx_tarefa}? [s/n]: "
            )

        if confirmacao == "s":
            id_tarefa = self.tarefas[idx_tarefa - 1].id
            sql.excluir_tarefa(id_tarefa)

        else:
            self.excluir_tarefa()
