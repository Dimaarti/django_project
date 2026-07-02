import random


class UniqueQueue:
    LIFO = "LIFO"

    def __init__(self, strategy=LIFO):
        self.strategy = strategy
        self.storage = []
        self.unique_check = set()
        if self.strategy not in self.LIFO:
            raise ValueError("Strategy must be LIFO")

    def add(self, item):
        # Проверяем значение на уникальность, если его нет, добавляем
        if item not in self.unique_check:
            self.storage.append(item)
            self.unique_check.add(item)

    def remove(self):
        if self.strategy == self.LIFO:
            # Если очередь пустая, то ошибка
            if not self.unique_check:
                raise IndexError("Queue is empty")
            # Если очередь не пустая, то удаляем последний элемент
            elif self.storage:
                item = self.storage.pop()
                # И удаляем этот же элемент из множества
                self.unique_check.remove(item)
                return item

    def length(self):
        return len(self.storage)

    def last_item(self):
        return self.storage[-1]

    def random_item(self):
        return self.storage[random.randint(0, len(self.storage) - 1)]



if __name__ == "__main__":
    queue = UniqueQueue()


