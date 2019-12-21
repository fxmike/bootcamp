class ElectricCar:

    def __init__(self, rang):
        self.rang = rang
        self._starting_val = rang

    def drive(self, dist):
        result = dist
        self.rang -= dist
        if self.rang <= 0:
            return f"{result}, Charge Your battery, currently Your car's range equals {self.rang}!"
        else:
            return result

    def charge(self):
        self.rang = self._starting_val

if __name__ == "__main__":
    car = ElectricCar(100)
    print(car.rang)
    print(car.drive(50))
    print(car.drive(50))
    car.charge()
    print(car.rang)

#TODO