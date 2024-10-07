class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

town_car = TownCar(60, "черный", "Городская машина")
town_car.go()
town_car.turn("налево")
town_car.stop()

police_car = PoliceCar(80, "белый", "Полицейская машина")
police_car.go()
police_car.turn("направо")
police_car.stop()