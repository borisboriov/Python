# Задание 1. Копирование содержимого одного файла в другой
# Создайте программу, которая копирует содержимое файла source.txt в новый файл destination.txt.

with open("/Users/boris/PycharmProjects/Python/files/source.txt", "r") as source_file:
    with open("/Users/boris/PycharmProjects/Python/files/destination.txt", "w") as destination_file:
        destination_file.write(source_file.read())

# Задание 2. Подсчёт стоимости заказа из файла
# Напишите программу, которая считывает файл prices.txt, содержащий информацию о товарах: название,
# количество и цену, и подсчитывает общую стоимость заказа.

result = 0
with open("/Users/boris/PycharmProjects/Python/files/prices.txt", "r") as prices_file:
    for line in prices_file:
        new_line  = list(line.split())
        result += int(new_line[1]) * int(new_line[2])

print(f"total price =  {result}")

# Задание 3. Подсчёт количества слов в файле
# Напишите программу, которая подсчитывает количество слов в текстовом файле text_file.txt и выводит результат на экран.

result = 0
with open("/Users/boris/PycharmProjects/Python/files/text_file.txt", "r") as text_file:
    for line in text_file:
        lines = str(line.replace("—", ""))
        list_words = lines.split()
        result += len(list_words)
print(f"words count =  {result}")


# Задание 4. Копирование уникального содержимого одного файла в другой
# Создайте программу, которая считывает строки из файла input.txt, сохраняет только уникальные строки и записывает их в новый файл unique_output.txt.

unique_values = set()
with open("/Users/boris/PycharmProjects/Python/files/input.txt", "r") as text_file:
    for line in text_file:
        unique_values.add(line.strip())

with open("/Users/boris/PycharmProjects/Python/files/unique_output.txt", "w") as unique_output_file:
    for line in unique_values:
        unique_output_file.write(line + "\n")