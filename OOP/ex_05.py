class CashMachine:

    def __init__(self):
        self._atm_state = []  #lista, posiadanych banknotów
        self._atm_withrdaw = []

    def is_available(self):
        return bool(len(self._atm_state))

    def put_money(self,lst):
        for bills in lst:
            if bills in (50, 100 ,200):
                self._atm_state.append(bills)
        return self._atm_state
        # self._atm_state.extend(lst)   -> inna opcja zamiast for

    def withdraw_money(self,amount):
        amt_diff = amount
        print(amt_diff)
        print()
        self._atm_state.sort(reverse=True)

        for money in self._atm_state:
            print(money)
            index_mon = self._atm_state.index(money)
            if money <= amt_diff:
                result = amt_diff - money
                print(result, end=" ")
                self._atm_withrdaw.append(money)
                amt_diff -= result
                # self._atm_state.remove(money)
                self._atm_state.pop(index_mon)

            else:
                continue

        return "Wypłacono banknoty: ", self._atm_withrdaw, "W bankomacie pozostały nominały: ", self._atm_state


if __name__ == "__main__":
    cash_machine = CashMachine()
    cash_machine.is_available()
    cash_machine.put_money([100, 100, 100])
    cash_machine.is_available()
    print(cash_machine.withdraw_money(300))

def test_cash_machine_init():
    machine = CashMachine()
    assert machine.is_available() == False

def test_cash_machine_put_money():
    machine = CashMachine()
    machine.put_money([50, 100])
    assert machine.is_available()
