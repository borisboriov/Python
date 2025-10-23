from Product import Product
from Order import Order


class Store:

    def __init__(self) -> None:
        self.products = []

    def __repr__(self):
        return f"Products in Store = {self.products}"

    # -add_product(product) — метод для добавления товара в магазин;
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    # -list_products() — метод для отображения всех товаров в магазине с их ценами и количеством на складе;
    def list_products(self) -> None:
        print(self.__repr__())

    # -create_order() — метод для создания нового заказа.
    def create_order(self) -> Order:
        return Order({})
