import tkinter as tk
import math
from basic_ops import add, subtract, multiply, divide, mod
from advanced_math import sin_func, cos_func, power, sqrt_func, floor_func, ceil_func
from memory import Memory

class CalculatorUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        self.window.geometry("320x400")
        self.memory = Memory()

        self.entry = tk.Entry(self.window, width=20, font=("Arial", 20), borderwidth=3, relief="sunken")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
            ('0',4,0), ('%',4,1), ('/',4,2), ('=',4,3),
            ('sin',5,0), ('cos',5,1), ('pow',5,2), ('sqrt',5,3),
            ('floor',6,0), ('ceil',6,1), ('MC',6,2), ('MR',6,3),
            ('M+',7,0), ('C',7,1)
        ]
        for (text, r, c) in buttons:
            tk.Button(self.window, text=text, width=7, height=2, command=lambda t=text: self.on_click(t)).grid(row=r, column=c)

    def on_click(self, char):
        try:
            if char == '=':
                expr = self.entry.get()
                result = eval(expr)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            elif char == 'C':
                self.entry.delete(0, tk.END)
            elif char == 'sin':
                self.entry.insert(tk.END, f" = {sin_func(float(self.entry.get()))}")
            elif char == 'cos':
                self.entry.insert(tk.END, f" = {cos_func(float(self.entry.get()))}")
            elif char == 'pow':
                self.entry.insert(tk.END, "**")
            elif char == 'sqrt':
                self.entry.insert(tk.END, f" = {sqrt_func(float(self.entry.get()))}")
            elif char == 'floor':
                self.entry.insert(tk.END, f" = {floor_func(float(self.entry.get()))}")
            elif char == 'ceil':
                self.entry.insert(tk.END, f" = {ceil_func(float(self.entry.get()))}")
            elif char == 'M+':
                self.memory.memory_add(float(self.entry.get()))
            elif char == 'MC':
                self.memory.memory_clear()
            elif char == 'MR':
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.memory.memory_recall())
            else:
                self.entry.insert(tk.END, char)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Ошибка")

    def run(self):
        self.window.mainloop()
