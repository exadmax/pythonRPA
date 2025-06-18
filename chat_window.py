import os
import subprocess
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from typing import List


class ChatGPTCommander:
    """Simple GUI app that sends user prompts to ChatGPT and executes the
    returned commands.

    The OpenAI API key must be provided via the ``OPENAI_API_KEY``
    environment variable.
    """

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("ChatGPT Commander")
        self.history = ScrolledText(master, wrap="word", height=20, width=60)
        self.history.pack(padx=10, pady=10)

        self.prompt = tk.Entry(master, width=60)
        self.prompt.pack(padx=10, pady=(0, 10))
        self.prompt.bind("<Return>", lambda _: self.send())

        tk.Button(master, text="Enviar", command=self.send).pack(pady=(0, 10))

    def append_history(self, text: str) -> None:
        self.history.configure(state=tk.NORMAL)
        self.history.insert(tk.END, text + "\n")
        self.history.configure(state=tk.DISABLED)
        self.history.see(tk.END)

    def send(self) -> None:
        message = self.prompt.get().strip()
        if not message:
            return
        self.append_history(f"Usuário: {message}")
        self.prompt.delete(0, tk.END)
        Thread(
            target=self.handle_message, args=(message,), daemon=True
        ).start()

    def handle_message(self, message: str) -> None:
        try:
            response = self.ask_chatgpt(message)
            self.append_history(f"ChatGPT: {response}")
            commands = self.parse_commands(response)
            if commands:
                self.append_history("Executando comandos:")
                self.run_commands(commands)
        except Exception as exc:  # pragma: no cover - runtime feedback only
            self.append_history(f"Erro: {exc}")

    def ask_chatgpt(self, prompt: str) -> str:
        import openai  # local import to avoid hard dependency during tests

        openai.api_key = os.environ.get("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return completion["choices"][0]["message"]["content"].strip()

    @staticmethod
    def parse_commands(text: str) -> List[str]:
        return [line.strip() for line in text.splitlines() if line.strip()]

    def run_commands(self, commands: List[str]) -> None:
        for cmd in commands:
            self.append_history(f"$ {cmd}")
            try:
                result = subprocess.check_output(cmd, shell=True, text=True)
                if result:
                    self.append_history(result)
            except subprocess.CalledProcessError as exc:
                self.append_history(exc.output)


if __name__ == "__main__":
    root = tk.Tk()
    ChatGPTCommander(root)
    root.mainloop()
