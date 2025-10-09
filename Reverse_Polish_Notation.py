class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст.")

def calculate_rpn(expressions):
    stack = Stack()
    operators = {"+", "-", "*", "/"}

    for token in expressions.split():
        if token not in operators:
            stack.push(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                stack.push(a / b)
    return stack.pop()

expression = input("Введите выражение в обратной польской записи "
                   "(числа и операторы разделяйте пробелами):")
try:
    result = calculate_rpn(expression)
    print(f"Результат: {result}")
except Exception as e:
    print(f"Ошибка при вычислении: {e}")