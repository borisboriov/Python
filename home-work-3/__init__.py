from Store import Store
from Product import Product

if __name__ == '__main__':
    # Создаем магазин
    store = Store()

    # Создаем товары
    product1 = Product("Ноутбук", 1000, 2)
    product2 = Product("Смартфон", 500, 4)

    # Добавляем товары в магазин
    store.add_product(product1)
    store.add_product(product2)

    # Список всех товаров
    store.list_products()

    # Создаем заказ
    order = store.create_order()

    # Добавляем товары в заказ
    order.add_product(product1, 2)
    order.add_product(product2, 3)



    # Выводим общую стоимость заказа
    total = order.calculate_total()
    print(f"Общая стоимость заказа: {total}")

    # Проверяем остатки на складе после заказа
    store.list_products()