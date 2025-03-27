from src.utils.file_reader import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_excel
from src.utils.operation_filters import filter_operations_by_status, sort_operations_by_date
from src.utils.operation_search import search_operations_by_description
from src.utils.operation_counter import count_operations_by_categories


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ").strip()
    if choice == "1":
        file_path = "data/transactions.json"
        operations = read_transactions_from_json(file_path)
        print(f"Для обработки выбран JSON-файл: {file_path}")
    elif choice == "2":
        file_path = "data/transactions.csv"
        operations = read_transactions_from_csv(file_path)
        print(f"Для обработки выбран CSV-файл: {file_path}")
    elif choice == "3":
        file_path = "data/transactions_excel.xlsx"
        operations = read_transactions_from_excel(file_path)
        print(f"Для обработки выбран XLSX-файл: {file_path}")
    else:
        print("Неверный выбор.")
        return

    # Добавьте остальную логику фильтрации, сортировки и вывода результатов
    # (см. полный код из предыдущего ответа)
    ...