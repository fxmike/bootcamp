class Product:

    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return f"{self.nazwa}({self.id}), cena: {self.cena:.2f}"

    def print_info(self):
        print(f"Produkt: {self.nazwa!r}, id: {self.id}, cena: {self.cena} PLN")




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
        result = "Produkty w koszyku:\n"
        for product, quantity in self._products.items():
            result += f"- {product} x {quantity}\n"
        result += f"W sumie: {self.count_total_price():.2f}"
        return result

    @classmethod
    def from_products(cls, given_products):
        basket = cls()
        for product in given_products:
            basket.add_product(product, 1)
        return basket


if __name__ == "__main__":
    basket = Basket()
    product = Product(1, "Woda", 10.99)
    product2 = Product(2, "Chleb", 3.24)
    basket.add_product(product,5)
    basket.add_product(product2,2)
    # print(basket._products)
    basket.count_total_price()
    print(basket.generate_report())

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

def test_basket_one_product_report():
    b = Basket()
    p = Product(1, "Woda", 10.0)
    b.add_product(p, 3)
    expected = """Produkty w koszyku:
- Woda(1), cena: 10.00 x 3
W sumie: 30.00"""
    assert b.generate_report() == expected

def test_basket_multiple_product_report():
    b = Basket()
    p1 = Product(1, "Pierogi", 10.0)
    p2 = Product(2, "Choinka", 20.0)
    p3 = Product(3, "Prezenty", 30.0)
    b.add_product(p1, 10)
    b.add_product(p2, 1)
    b.add_product(p3, 4)
    assert len(b.generate_report().splitlines()) == 2 + 3

def test_basket_from_products():
    p1 = Product(1, "Pierogi", 10.0)
    p2 = Product(2, "Choinka", 20.0)
    p3 = Product(3, "Prezenty", 30.0)
    b = Basket.from_products([p1, p2, p3])
    assert len(b.generate_report().splitlines()) == 2 + 3