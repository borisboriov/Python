documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def find_doc(doc_number: str) -> str | None:
    """
    Находит владельца документа по его номеру.

    Args:
        doc_number (str): Номер документа

    Returns:
        str | None: Имя владельца или None, если документ не найден
    """
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return None


def check_directory(doc_number: str) -> str | None:
    """
    Находит номер полки, где хранится документ.

    Args:
        doc_number (str): Номер документа

    Returns:
        str | None: Номер полки или None, если документ не найден
    """
    for shelf, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            return shelf
    return None


if __name__ == '__main__':
    command = input('Введите команду:\n')

    if command == 'p':
        doc_number = input('Введите номер документа:\n')
        owner = find_doc(doc_number)

        if owner:
            print(f'Владелец документа: {owner}')
        else:
            print('Документ не найден')

    elif command == 's':
        doc_number = input('Введите номер документа:\n')
        shelf = check_directory(doc_number)

        if shelf:
            print(f'Документ хранится на полке: {shelf}')
        else:
            print('Документ не найден в базе')
