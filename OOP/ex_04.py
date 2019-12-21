class Product:

    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"Produkt: {self.nazwa!r}, id: {self.id}, cena: {self.cena} PLN")

    def __repr__(self):
        return self.nazwa


class Basket:

    def __init__(self):
        self._products = {}


    def add_product(self, produkt, qty):
        if produkt in self._products:
            #key == produkt
            self._products[produkt] += qty
        else:
            self._products[produkt] = qty

    def count_total_price(self):
        total_price = 0
        for product, quantity in self._products.items():
            total_price += product.cena * quantity
        return total_price

    def generate_report(self):
        pass

if __name__ == "__main__":
    basket = Basket()
    product = Product(1, "Woda", 10.99)
    basket.add_product(product,5)
    print(basket._products)
    basket.count_total_price()
    basket.generate_report()

def test_basket_empty_price():
    b = Basket()
    assert b.count_total_price() == 0

def test_basket_one_product_price():
    b = Basket()
    p = Product(1, "Woda", 10.0)
    b.add_product(p, 3)
    assert b.count_total_price() == 3 * 10

def test_basket_multiple_products_price():
    b = Basket()
    woda = Product(1, "Woda", 10.0)
    chleb = Product(2, "Chleb", 20.0)
    b.add_product(woda, 3)
    b.add_product(chleb, 1)
    b.add_product(woda, 1)
    assert b.count_total_price() == 4 * 10 + 1 * 20
