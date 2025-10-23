from Product import Product


class Order:
    products = dict

    def __init__(self, products: dict[Product, int]) -> None:
        self.products = products
        print(products)

    # -add_product(product, quantity) — метод для добавления товара в заказ. Если товара недостаточно на складе, должно выдаваться сообщение об ошибке;
    def add_product(self, product: Product, quantity: int) -> None:
        if product.stock < quantity:
            raise ValueError(f"Not enough products in stock({product.stock})")

        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

        product.update_stock(-quantity)

    # -calculate_total() — метод для расчёта общей стоимости заказа.
    def calculate_total(self) -> int:
        result = 0
        for product, quantity in self.products.items():
            result += product.price * quantity
        return result
