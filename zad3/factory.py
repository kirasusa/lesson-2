class Toy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.type}"


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Животное")


class CartoonCharacterToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color, "Персонаж мультфильма")


class ToyFactory:
    def _purchase_materials(self):
        print("Закупка сырья...")

    def _sew(self):
        print("Пошив...")

    def _paint(self):
        print("Окраска...")

    def _create_toy(self, toy_class, name, color):
        self._purchase_materials()
        self._sew()
        self._paint()
        return toy_class(name, color)

    def create_toy(self, name, color, type):
        toy_classes = {
            "Животное": AnimalToy,
            "Персонаж мультфильма": CartoonCharacterToy
        }

        if type in toy_classes:
            return self._create_toy(toy_classes[type], name, color)
        else:
            raise ValueError("Неправильный тип игрушки")


factory = ToyFactory()
toy1 = factory.create_toy("Заяц", "Серый", "Животное")
toy2 = factory.create_toy("Копатыч", "Оранжевый", "Персонаж мультфильма")

print(toy1)
print(toy2)
