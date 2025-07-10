import sys
import types
import pytest

# Stub pyautogui if not installed
if "pyautogui" not in sys.modules:
    stub = types.SimpleNamespace(
        moveRel=lambda x, y: None, position=lambda: (0, 0), FAILSAFE=True
    )
    sys.modules["pyautogui"] = stub

import mouse


class DummyEvent:
    def __init__(self):
        self.calls = 0

    def is_set(self):
        self.calls += 1
        return self.calls <= 1


def test_move_mouse(monkeypatch):
    moves = []
    monkeypatch.setattr(
        mouse.pyautogui, "moveRel", lambda x, y: moves.append((x, y))
    )
    monkeypatch.setattr(mouse.pyautogui, "position", lambda: (10, 10))
    monkeypatch.setattr(mouse.time, "sleep", lambda s: None)

    app = mouse.MouseMoverApp.__new__(mouse.MouseMoverApp)
    app.running = DummyEvent()
    app.move_mouse()

    assert moves == [(1, 1), (-1, -1)]
    assert mouse.pyautogui.FAILSAFE is False
