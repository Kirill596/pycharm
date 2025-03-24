import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")
