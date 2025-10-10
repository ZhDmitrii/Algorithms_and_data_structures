class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Очередь пуста.")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Пример использования
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Размер очереди:{queue.size()}\n")

while not queue.is_empty():
    item = queue.dequeue()
    print(f"Извлечен элемент:{item}")