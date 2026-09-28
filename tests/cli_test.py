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
        ("rm -rf /", "Error"),  # Неизвестная команда
        ("pwd", "Error"),       # Неизвестная команда
    ],
    ids=["ls", "cd", "unknown_rm", "unknown_pwd"]
)
def test_cli_commands(monkeypatch, capsys, user_input, expected_output):
    inputs = iter([user_input, "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    cli()
    
    captured = capsys.readouterr()
    assert expected_output in captured.out