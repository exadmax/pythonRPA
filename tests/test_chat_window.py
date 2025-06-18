import pytest

from chat_window import ChatGPTCommander


def test_parse_commands_simple():
    text = "echo hello\nls -l\n"
    commands = ChatGPTCommander.parse_commands(text)
    assert commands == ["echo hello", "ls -l"]


def test_run_commands(tmp_path):
    file = tmp_path / "file.txt"
    commands = [f"echo hi > {file}"]

    app = ChatGPTCommander.__new__(ChatGPTCommander)
    app.append_history = lambda text: None

    app.run_commands(commands)

    assert file.read_text().strip() == "hi"
