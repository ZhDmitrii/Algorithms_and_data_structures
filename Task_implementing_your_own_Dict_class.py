class MyDict:
    def __init__(self):
        self._items = []

    def __str__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in self._items) + "}"

    def __getitem__(self, key):
        for k, v in self._items:
            if k == key:
                return v
        return None

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self._items):
            if k == key:
                self._items[i] = (key, value)
                return
        self._items.append((key, value))

    def __contains__(self, key):
        return any(k == key for k, _ in self._items)

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self._items):
            if k == key:
                del self._items[i]
                return

    def keys(self):
        return [k for k, _ in self._items]

    def values(self):
        return [v for _, v in self._items]

    def items(self):
        return self._items


my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
