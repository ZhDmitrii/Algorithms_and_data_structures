class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: str) -> None:
        self.items.append(item)

    def pop(self) -> str:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пустой.")

    def peek(self) -> str:
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пустой.")

def is_checking(seq: str) -> bool:
    parenthesis_map = {")":"(", "]":"[", "}":"{"}
    open_parentheses = ["(", "[", "{"]
    close_parentheses = [")", "]", "}"]

    stack = Stack()

    for i in seq:
        if i in open_parentheses:
            stack.push(i)
        elif i in close_parentheses:
            if stack.is_empty() or stack.peek() != parenthesis_map[i]:
                return False
            stack.pop()

    return stack.is_empty()


seq_in = input("Введите скобочную последовательность: ")

result = is_checking(seq_in)

if result:
    print("Последовательность правильная.")
else:
    print("Последовательность неправильная.")
