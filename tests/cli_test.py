"""Модуль тестирования эмулятора командной оболочки VFS.

Содержит набор автоматизированных тестов для проверки корректности работы
интерактивного режима (REPL) на первом этапе разработки. Тестирование
выполняется с использованием фреймворка pytest.

Тестируемый компонент:
    Функция cli() — основной цикл обработки команд пользователя.

Методы тестирования:
    - Параметризация тестовых сценариев (pytest.mark.parametrize)
      для проверки различных вариантов пользовательского ввода.
    - Мокирование стандартного ввода (monkeypatch) для имитации
      интерактивного взаимодействия без ручного ввода данных.
    - Перехват стандартного вывода (capsys) для верификации
      результатов выполнения команд.

Тестируемые сценарии:
    - Выполнение команды ls с аргументами.
    - Выполнение команды cd с аргументами.
    - Обработка неизвестных команд (rm, pwd) с выводом сообщения об ошибке.
    - Корректное завершение работы эмулятора по команде exit.
"""

import pytest

def cli():
    com_list = ["ls", "cd", "exit"]
    while True:
        line = input("VFS> ").split()
        if line[0] not in com_list:
            print("Error")
        elif line[0] == "ls":
            print(*line)
        elif line[0] == "cd":
            print(*line)
        elif line[0] == "exit":
            break

@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("ls -a", "ls -a"),
        ("cd /tmp", "cd /tmp"),
        ("rm -rf /", "Error"),  
        ("pwd", "Error"),       
    ],
    ids=["ls", "cd", "unknown_rm", "unknown_pwd"]
)
def test_cli_commands(monkeypatch, capsys, user_input, expected_output):
    inputs = iter([user_input, "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    cli()
    
    captured = capsys.readouterr()
    assert expected_output in captured.out