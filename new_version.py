import tkinter as tk

class BombCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("330x430")
        self.configure(bg="#202020")

        self.formula = ""
        self.build_ui()

    def build_ui(self):
        # Поле для ввода чисел
        self.input_field = tk.Entry(self, font=("Courier New", 22), bg="#121212", fg="#00ffcc",
                                    justify="right", insertbackground="white")
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

        # Кнопки
        button_texts = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for i, row in enumerate(button_texts):
            for j, symbol in enumerate(row):
                btn = tk.Button(self, text=symbol, font=("Courier", 18, "bold"),
                                width=5, height=2, bg="#2e2e2e", fg="white",
                                activebackground="#444444",
                                command=lambda val=symbol: self.on_click(val))
                btn.grid(row=i+1, column=j, padx=5, pady=5)

    def on_click(self, char):
        if char == 'C':
            self.formula = ""
        elif char == '=':
            try:
                self.formula = str(self.safe_eval(self.formula))
            except:
                self.formula = "Ошибка"
        else:
            self.formula += char

        self.refresh()

    def refresh(self):
        self.input_field.delete(0, tk.END)
        self.input_field.insert(tk.END, self.formula)

    def safe_eval(self, expr):

        import operator
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        tokens = []
        num = ''
        for ch in expr:
            if ch.isdigit() or ch == '.':
                num += ch
            elif ch in ops:
                if num == '':
                    raise ValueError("Неправильный ввод")
                tokens.append(float(num))
                tokens.append(ch)
                num = ''
        if num != '':
            tokens.append(float(num))


        while len(tokens) > 1:
            a, op, b = tokens[0], tokens[1], tokens[2]
            result = ops[op](a, b)
            tokens = [result] + tokens[3:]
        return tokens[0]

if __name__ == "__main__":
    BombCalculator().mainloop()
