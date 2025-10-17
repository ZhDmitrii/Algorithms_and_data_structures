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
        # Стек для обхода в глубину
        stack = [self._root]
        # Хранение вершин, которые уже посещены
        visited = []

        while stack:
            # Берём последнюю вершину из стека
            node = stack.pop()
            # Если вершина ещё не посещалась
            if node not in visited:
                # Помечаем её как посещённую
                visited.append(node)

                for neighbor in node.outbound:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited


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
result = g.dfs()

# Вывод результата
for n in result:
    print(n)
print("-"*30)

a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)

g = Graph(a)

# Запускаем обход в глубину
result = g.dfs()

# Вывод результата
for n in result:
    print(n)
print("-"*30)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
c.point_to(e)

g = Graph(a)

# Запускаем обход в глубину
result = g.dfs()

# Вывод результата
for n in result:
    print(n)
print("-"*30)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
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
result = g.dfs()

# Вывод результата
for n in result:
    print(n)
print("-"*30)