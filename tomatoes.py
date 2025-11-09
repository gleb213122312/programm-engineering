class Tomato:
    states = ('отсутствует', 'цветение', 'зеленый', 'красный')

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        current_pos = Tomato.states.index(self._state)
        if current_pos < len(Tomato.states) - 1:
            self._state = Tomato.states[current_pos + 1]
        print(f"Томат {self._index} перешёл на стадию: {self._state}")

    def is_ripe(self):
        return self._state == Tomato.states[-1]

    def __repr__(self):
        return f"Tomato(index={self._index}, state='{self._state}')"


class TomatoBush:
    def __init__(self, amount):
        self.tomatoes = [Tomato(i + 1) for i in range(amount)]
        print(f"Создан куст с {amount} томатами.")

    def grow_all(self):
        print("Куст растёт вместе с томатами...")
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        result = all(tomato.is_ripe() for tomato in self.tomatoes)
        print(f"Проверка зрелости всех томатов: {result}")
        return result

    def give_away_all(self):
        count = len(self.tomatoes)
        self.tomatoes = []
        print(f"Урожай собран! С куста убрано {count} томатов.")


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} работает: поливает, рыхлит, удобряет...")
        self._plant.grow_all()

    def harvest(self):
        print(f"{self.name} пробует собрать урожай...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай успешно собран!")
        else:
            print("Рано! Есть неспелые томаты. Нужно ещё поухаживать.")

    @staticmethod
    def knowledge_base():
        print("СПРАВКА ПО САДОВОДСТВУ:")
        print("Чтобы вырастить помидоры, нужно регулярно ухаживать за кустом.")
        print("Стадии: отсутствует -> цветение -> зеленый -> красный.")
        print("Садовник может собирать урожай только когда все томаты созреют.")


if __name__ == "__main__":
    Gardener.knowledge_base()
    print("-" * 50)

    bush = TomatoBush(amount=3)
    print("Нанимаем садовника Алексея.")
    g = Gardener(name="Алексей", plant=bush)
    print("-" * 50)

    g.work()
    g.work()
    print("-" * 50)

    g.harvest()
    print("-" * 50)

    g.work()
    print("-" * 50)

    g.harvest()
    if not bush.tomatoes:
        print("На кусте нет томатов")
    else:
        print("На кусте остаются томаты:", bush.tomatoes)
