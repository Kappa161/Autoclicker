import  time, threading
import tkinter as tk
from tkinter import ttk


import pyautogui

pyautogui.FAILSAFE = False

class ClickerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Автокликер")
        self.window.resizable(False, False)
        self.window.configure(bg="#1e1e2e")
        
        self.running = False
        self.thread = threading.Thread(target=self.click_loop, daemon=True)
        self.thread.start()
        
        #  ----Стиль----
        style = ttk.Style()
        style.theme_use("clam")
        
        #  ----Заголовок----
        title = tk.Label(self.window, text="🖱 Автокликер",
                         font=("Segoe UI", 18, "bold"),
                         bg="#1e1e2e", fg="#cdd6f4")
        title.pack(pady=(15, 5))
    
        self.status = tk.Label(self.window, text="Остановлен",
                               font=("Segoe UI", 11),
                               bg="#1e1e2e", fg="#f38ba8")
        self.status.pack(pady=(0, 10))
        
        #  ----Выбор кнопки мыши----
        row1 = tk.Frame(self.window, bg="#1e1e2e")
        row1.pack(pady=5)
        tk.Label(row1, text="Кнопка мыши:", bg="#1e1e2e",
                 fg="#cdd6f4", font=("Segou UI", 10)).pack(side="left", padx=5)
        self.mouse_button = tk.StringVar(value="left")
        for text, val in [("Левая", "left"),("Правая", "right")]:
            tk.Radiobutton(row1, text=text, variable=self.mouse_button,
                           value=val, bg="#1e1e2e", fg="#cdd6f4",
                           selectcolor="#313244", activebackground="#1e1e2e",
                           font=("Segoe UI", 10)).pack(side="left", padx=5)
        
        #  ----Задержка----
        row2 = tk.Frame(self.window, bg="#1e1e2e")
        row2.pack(pady=5)
        tk.Label(row2, text="Интервал, сек:", bg="#1e1e2e",
                 fg="#cdd6f4", font=("Segoe UI", 10)).pack(side="left", padx=5)
        self.delay = tk.StringVar(value="0.5")
        entry = tk.Entry(row2, textvariable=self.delay, width=8,
                         justify="center", bg="#313244", fg="#cdd6f4",
                         insertbackground="#cdd6f4", relief="flat")
        entry.pack(side="left", padx=5)
        
        #  ----Кнопки управления----
        row3 = tk.Frame(self.window, bg="#1e1e2e")
        row3.pack(pady=15)
        self.toggle_btn = tk.Button(row3, text="▶  Старт", width=10,
                                    font=("Segoe UI", 11, "bold"),
                                    bg="#a6e3a1", fg="#1e1e2e",
                                    activebackground="#94e2d5",
                                    activeforeground="#1e1e2e",
                                    bd=0, cursor="hand2",
                                    command=self.toggle)
        self.toggle_btn.pack(side="left", padx=5)
        
        tk.Button(row3, text="✕  Выход", width=10,
                  bg="#f38ba8", fg="#1e1e2e",
                  activebackground="#eba0ac",
                  activeforeground="#1e1e2e",
                  bd=0, cursor="hand2",
                  command=self.quit_app).pack(side="left", padx=5)
        
        #  ----Счетчик кликов----
        self.counter = tk.Label(self.window, text="Кликов: 0",
                                font=("Segoe UI", 10),
                                bg="#1e1e2e", fg="#9399b2")
        self.counter.pack(pady=(0, 15))
        
        self.click_count = 0
        self.window.protocol("WM_DELETE_WINDOW", self.quit_app)
    
    def toggle(self):
        self.running = not self.running
        if self.running:
            self.status.config(text="Работает", fg="#a6e3a1")
            self.toggle_btn.confing(text="⏸  Пауза", bg="#f9e2af")
        else:
            self.status.config(text="Остановлен", fg="#f38ba8")
            self.toggle_btn.config(text="▶  Старт", bg="#a6e3a1")
    
    def quit_app(self):
        self.running = False
        self.window.destroy()
    
    def click_loop(self):
        while True:
            if self.running:
                try:
                    d = max(0.001, float(self.delay.get().replace(",", ".")))
                except ValueError:
                    d = 0.
                pyautogui.click(button=self.mouse_button.get())
                self.click_count += 1
                self.counter.config(text=f"Кликов: {self.click_count}")
                time.sleep(d)
            else:
                time.sleep(0.1)

app = ClickerApp()
app.window.mainloop()
