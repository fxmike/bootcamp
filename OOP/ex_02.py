class Employee:

    def __init__(self, name, surr, perh):
        self.name = name
        self.surr = surr
        self.perh = perh
        self._salary_to_pay = 0    #enkapsulacja - zmienne z podkreślnikiem to są zmienne niewywoływalne dla klasy

    def register_time(self, time):
        if time <= 8:
            self._salary_to_pay += self.perh * time
        else:
            self._salary_to_pay += (8 * self.perh) +\
                        ((time - 8) * self.perh * 2)

    def pay_salary(self):
        result = self._salary_to_pay
        self._salary_to_pay = 0
        return result

if __name__ == "__main__":
    empl = Employee('Jan', 'Kowalski', 100.00)
    empl.register_time(5)
    print(empl.pay_salary())
    print(empl.pay_salary())
    empl.register_time(10)
    empl.register_time(10)
    print(empl.pay_salary())