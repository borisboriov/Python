class Product:

    def __init__(self, name: str, price: float, stock: int = 0) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if stock < 0:
            raise ValueError("Количество на складе не может быть отрицательным")

        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product name: {self.name}, price: {self.price}, stock: {self.stock}"

    # -update_stock(quantity) — метод, который обновляет количество товара на складе. Если количество становится отрицательным,
    # должно выдаваться сообщение об ошибке.
    def update_stock(self, quantity: int) -> None:
        new_stock = self.stock + quantity
        if new_stock < 0:
            raise ValueError(f"Stock can't be negative: {new_stock}")
        self.stock = new_stock
        print(f"{self.name.upper()} quantity: {self.stock}")
