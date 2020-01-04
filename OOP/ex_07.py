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

class PremiumEmployee(Employee):

    def give_bonus(self,amount):
        print(f'{self._salary_to_pay + amount:.2f}')

if __name__ == "__main__":
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000)
    employee.pay_salary()
    print(employee.pay_salary())