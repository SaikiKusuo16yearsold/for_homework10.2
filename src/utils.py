import json
import os

import requests
from dotenv import load_dotenv

API_KEY = os.getenv("api_keys")
load_dotenv()


def dictionaries_financial_transaction_data(path_to_file):
    """"
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
     с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
     функция возвращает пустой список.
    """
    try:
        with open(path_to_file, "r", encoding="UTF-8") as file:
            data = json.load(file)
    except Exception:
        return []
    else:
        return data


def returns_transaction_amount(transaction):
    """"
    Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    возвращает тип float. Если транзакция была в USD или EUR, идет обращение к внешнему API для получения текущего
     курса валют и конвертации суммы операции в рубли.
    """
    currency_for_transaction = transaction["operationAmount"]["currency"]["code"]
    url = f"https://v6.exchangerate-api.com/v6/0504d3f7601436eb90528abf/latest/{currency_for_transaction}"
    response = requests.get(url, headers={"apikey": API_KEY})
    response_data = response.json()
    return float(transaction["operationAmount"]["amount"]) * response_data["conversion_rates"]["RUB"]
