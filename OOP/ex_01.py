class Product:

    def __init__(self,id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"Produkt: {self.nazwa!r}, id: {self.id}, cena: {self.cena} PLN")



def test_product_init():
    product = Product(1, "Woda", 10.99)
    assert product.id == 1
    assert product.nazwa == "Woda"
    assert product.cena == 10.99

def test_print_info(capsys):                #trik na testowanie funkcji, które robią wydruk
    product = Product(1, "Woda", 10.99)
    product.print_info()
    captured = capsys.readouterr()
    assert captured.out == "Produkt: 'Woda', id: 1, cena: 10.99 PLN\n"

if __name__ == "__main__":
    product = Product(1, "Woda", 10.99)
    product.print_info()