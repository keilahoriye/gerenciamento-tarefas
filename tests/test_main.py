from types import SimpleNamespace
from unittest.mock import Mock

import main


def _setup_main_dependencies(monkeypatch):
    create_engine_mock = Mock(return_value="fake-engine")
    metadata_mock = SimpleNamespace(create_all=Mock())
    base_mock = SimpleNamespace(metadata=metadata_mock)

    repo_instance = object()
    task_repository_mock = Mock(return_value=repo_instance)

    manager_instance = Mock()
    task_manager_mock = Mock(return_value=manager_instance)

    monkeypatch.setattr(main, "create_engine", create_engine_mock)
    monkeypatch.setattr(main, "Base", base_mock)
    monkeypatch.setattr(main, "TaskRepository", task_repository_mock)
    monkeypatch.setattr(main, "TaskManager", task_manager_mock)
    monkeypatch.setattr(main, "system", lambda *_: 0)
    monkeypatch.setattr(main, "name", "nt")

    return {
        "create_engine": create_engine_mock,
        "metadata": metadata_mock,
        "task_repository": task_repository_mock,
        "task_manager": task_manager_mock,
        "manager": manager_instance,
    }


def _run_main_with_inputs(monkeypatch, inputs):
    controls = _setup_main_dependencies(monkeypatch)
    values = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda *_: next(values))

    main.main()
    return controls


def test_opcao_adicionar_tarefa(monkeypatch):
    controls = _run_main_with_inputs(monkeypatch, ["1", "4"])

    controls["create_engine"].assert_called_once_with("sqlite:///tasks.db")
    controls["metadata"].create_all.assert_called_once_with("fake-engine")
    controls["task_repository"].assert_called_once_with("fake-engine")
    controls["task_manager"].assert_called_once()
    controls["manager"].criar_tarefa.assert_called_once()
    controls["manager"].listar_tarefas.assert_not_called()
    controls["manager"].mudar_status.assert_not_called()


def test_opcao_listar_tarefas(monkeypatch):
    controls = _run_main_with_inputs(monkeypatch, ["2", "4"])

    controls["manager"].listar_tarefas.assert_called_once()
    controls["manager"].criar_tarefa.assert_not_called()
    controls["manager"].mudar_status.assert_not_called()


def test_opcao_mudar_status(monkeypatch):
    controls = _run_main_with_inputs(monkeypatch, ["3", "4"])

    controls["manager"].mudar_status.assert_called_once()
    controls["manager"].criar_tarefa.assert_not_called()
    controls["manager"].listar_tarefas.assert_not_called()


def test_opcao_invalida_nao_chama_acoes(monkeypatch):
    controls = _run_main_with_inputs(monkeypatch, ["x", "4"])

    controls["manager"].criar_tarefa.assert_not_called()
    controls["manager"].listar_tarefas.assert_not_called()
    controls["manager"].mudar_status.assert_not_called()
