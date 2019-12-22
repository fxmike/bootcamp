class NotEnoughMoney(Exception):
    pass

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
        #TODO raise

        #TODO zweryfikować
        # self._atm_state.extend(lst)   -> inna opcja zamiast for

    def withdraw_money(self,amount):
        #TODO weryfikacja amount
        collected_sum = 0
        collected_bills = []
        self._atm_state.sort(reverse=True)

        for bill in self._atm_state:
            if bill + collected_sum <= amount:
                collected_sum += bill
                collected_bills.append(bill)

        if collected_sum == amount:
            for bill in collected_bills:
                self._atm_state.remove(bill)
        else:
            raise NotEnoughMoney()

        return "Wypłacono banknoty: ", collected_bills, "W bankomacie pozostały nominały: ", self._atm_state


if __name__ == "__main__":
    cash_machine = CashMachine()
    cash_machine.is_available()
    cash_machine.put_money([100, 100, 100])
    cash_machine.is_available()
    try:
        bills = cash_machine.withdraw_money(400)
    except NotEnoughMoney:
        print('Nie ma tyle środków w bankomacie')
        bills = []
    print("wyjęliśmy środki: ", bills)
def test_cash_machine_init():
    machine = CashMachine()
    assert machine.is_available() == False

def test_cash_machine_put_money():
    machine = CashMachine()
    machine.put_money([50, 100])
    assert machine.is_available()
