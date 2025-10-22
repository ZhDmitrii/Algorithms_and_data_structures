class Node:
    def __init__(self, value):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f"Node({self.value})"


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        visited = set()
        result = []

        def _dfs(node):
            if node in visited:
                return
            result.append(node)
            visited.add(node)
            for neighbour in node.outbound:
                _dfs(neighbour)

        _dfs(self._root)
        return result

    def bfs(self):
        visited = set()
        result = []
        queue = [self._root]

        if self._root is None:
            return []

        while queue:
            node = queue.pop(0)

            if node in visited:
                continue

            result.append(node)
            visited.add(node)

            for neighbour in node.outbound:
                if neighbour not in visited:
                    queue.append(neighbour)

        return result


# Определение вершин
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

# Связываем вершины
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

# Создаём граф, начиная с вершины "a"
g = Graph(a)

# Запускаем обход в глубину
res = g.dfs()

# Вывод результата
print(f"Обход в глубину:")
for n in res:
    print(n)
print("-" * 30)

# Запускаем обход в ширину
res = g.bfs()

# Вывод результата
print(f"Обход в ширину:")
for n in res:
    print(n)
print("-" * 30)

a = Node("a")
b = Node("b")
c = Node("c")
a.point_to(b)
b.point_to(c)

g = Graph(a)

# Запускаем обход в глубину
res = g.dfs()

# Вывод результата
print(f"Обход в глубину:")
for n in res:
    print(n)
print("-" * 30)

# Запускаем обход в ширину
res = g.bfs()

# Вывод результата
print(f"Обход в ширину:")
for n in res:
    print(n)
print("-" * 30)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
c.point_to(e)

g = Graph(a)

# Запускаем обход в глубину
res = g.dfs()

# Вывод результата
print(f"Обход в глубину:")
for n in res:
    print(n)
print("-" * 30)

# Запускаем обход в ширину
res = g.bfs()

# Вывод результата
print(f"Обход в ширину:")
for n in res:
    print(n)
print("-" * 30)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")
k = Node("k")
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)

# Запускаем обход в глубину
res = g.dfs()

# Вывод результата
print(f"Обход в глубину:")
for n in res:
    print(n)
print("-" * 30)

# Запускаем обход в ширину
res = g.bfs()

# Вывод результата
print(f"Обход в ширину:")
for n in res:
    print(n)
print("-" * 30)
