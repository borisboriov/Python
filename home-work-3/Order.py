from Product import Product


class Order:
    products = dict

    def __init__(self, products: dict[Product, int]) -> None:
        self.products = products

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

    # . Реализуйте возможность удаления товаров из заказа.
    # -Добавьте метод remove_product(product, quantity) в класс Order, который будет удалять указанное количество товара из заказа.
    # Если количество товара в заказе становится равным нулю, удалите товар из словаря products.
    def remove_product(self, product: Product, quantity: int) -> None:
        ordered_qty = self.products[product]
        if quantity > ordered_qty:
            raise ValueError(f"Cannot remove {quantity}; only {ordered_qty} in order")

        new_qty = ordered_qty - quantity
        if new_qty == 0:
            del self.products[product]
        else:
            self.products[product] = new_qty

        product.update_stock(quantity)