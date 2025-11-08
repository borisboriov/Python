import threading
import time

# ========== ЗАДАНИЕ 1 ==========
print("=== ЗАДАНИЕ 1: Квадраты и кубы ===\n")

def squares():
    for i in range(1, 11):
        print(f"Квадрат {i} = {i ** 2}")

def cubes():
    for i in range(1, 11):
        print(f"Куб {i} = {i ** 3}")

# Создаём 2 потока
thread1 = threading.Thread(target=squares)
thread2 = threading.Thread(target=cubes)

# Запускаем
thread1.start()
thread2.start()

# Ждём завершения
thread1.join()
thread2.join()

print("\n=== ЗАДАНИЕ 1 ЗАВЕРШЕНО ===\n")

# ========== ЗАДАНИЕ 2 ==========
print("=== ЗАДАНИЕ 2: Числа с задержкой ===\n")

def print_numbers():
    for i in range(1, 11):
        print(f"Число: {i}")
        time.sleep(1)

# Создаём 3 потока без цикла
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers)
t3 = threading.Thread(target=print_numbers)

# Запускаем
t1.start()
t2.start()
t3.start()

# Ждём все потоки
t1.join()
t2.join()
t3.join()

print("\n=== ЗАДАНИЕ 2 ЗАВЕРШЕНО ===")
