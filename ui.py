import tkinter as tk
from tkinter import ttk
from basic_ops import add, subtract, multiply, divide
from advanced_math import sin_func, cos_func, sqrt_func, power
from memory import Memory


class CalculatorUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Калькулятор")
        self.root.geometry("400x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.bg_color = "#2b2b2b"
        self.display_bg = "#3c3f41"
        self.button_bg = "#4e5052"
        self.button_hover = "#5c5f61"
        self.accent = "#ff9800"
        self.text_color = "#ffffff"

        self.memory = Memory()

        self.expression = ""

        self.display = tk.Entry(
            self.root,
            font=("Consolas", 22, "bold"),
            bg=self.display_bg,
            fg=self.text_color,
            bd=0,
            justify="right",
            insertbackground=self.text_color
        )
        self.display.pack(fill="x", ipady=20, padx=10, pady=15)

        self.create_buttons()

    def create_buttons(self):
        btns = [
            ["MC", "MR", "M+", "C"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["sin", "cos", "√", "^"]
        ]

        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(padx=10, pady=10)

        for r, row in enumerate(btns):
            for c, char in enumerate(row):
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Consolas", 18, "bold"),
                    bg=self.button_bg,
                    fg=self.text_color,
                    activebackground=self.button_hover,
                    activeforeground=self.accent,
                    width=5, height=2,
                    relief="flat",
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")

    def on_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Ошибка"
        elif char == "MC":
            self.memory.memory_clear()
        elif char == "MR":
            self.expression += str(self.memory.memory_recall())
        elif char == "M+":
            try:
                self.memory.memory_add(float(self.expression))
            except:
                pass
        elif char == "sin":
            try:
                self.expression = str(sin_func(float(self.expression)))
            except:
                self.expression = "Ошибка"
        elif char == "cos":
            try:
                self.expression = str(cos_func(float(self.expression)))
            except:
                self.expression = "Ошибка"
        elif char == "√":
            try:
                self.expression = str(sqrt_func(float(self.expression)))
            except:
                self.expression = "Ошибка"
        elif char == "^":
            self.expression += "**"
        else:
            self.expression += str(char)

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def run(self):
        self.root.mainloop()
