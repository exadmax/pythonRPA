# coding: utf-8
"""Utility class for launching OS applications and interacting with their
windows using ``pyautogui`` and ``pygetwindow``.

This module exposes :class:`AppAutomator` which provides helpers for starting
an application, locating its window and interacting with on-screen elements via
image recognition. It relies on ``pyautogui`` for user input emulation and
``pygetwindow`` for window detection. These libraries may not work on all
operating systems or desktop environments and typically require a graphical
session.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pyautogui

try:
    import pygetwindow as gw
except Exception:  # pragma: no cover - optional dependency might be missing
    gw = None


class AppAutomator:
    """Launch and automate desktop applications."""

    def __init__(self) -> None:
        pyautogui.FAILSAFE = True

    def launch(self, executable: str | Path, *args: str) -> subprocess.Popen:
        """Start an application asynchronously.

        Parameters
        ----------
        executable:
            Path to the program to run.
        *args:
            Extra command line arguments.
        """
        path = str(executable)
        return subprocess.Popen([path, *args])

    def find_window(self, title: str):
        """Return the first window whose title contains ``title``.

        Raises ``RuntimeError`` if ``pygetwindow`` is not available.
        """
        if gw is None:
            raise RuntimeError("pygetwindow is required for window detection")
        windows = gw.getWindowsWithTitle(title)
        return windows[0] if windows else None

    def focus_window(self, window) -> None:
        """Focus the provided window using ``pygetwindow``."""
        if window:
            window.activate()

    def click_image(self, image_path: str, confidence: float = 0.8) -> bool:
        """Locate ``image_path`` on screen and click its center if found."""
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            return True
        return False

    def write(self, text: str, interval: float = 0.05) -> None:
        """Type ``text`` using the keyboard with an optional delay."""
        pyautogui.write(text, interval=interval)
