import pyautogui
import tkinter as tk
from threading import Thread, Event
import time

/**
* Classe para realizar testes menores do mouse, como movimentacao entre outros.
*/
class MouseMoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fix")
        self.master.geometry("300x150")

        self.running = Event()

        self.label = tk.Label(master, text="Iniciar procedimento.", wraplength=250)
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="Iniciar", command=self.start)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Parar", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Fechar", command=self.close)
        self.quit_button.pack(pady=5)

    def move_mouse(self):
        while self.running.is_set():
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 1, y + 1)  # Move 1 pixel para não gerar desconforto
            pyautogui.moveTo(x, y)
            time.sleep(10)

    def start(self):
        self.running.set()
        self.worker = Thread(target=self.move_mouse, daemon=True)
        self.worker.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        self.running.clear()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def close(self):
        self.running.clear()
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()
