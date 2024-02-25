import json
from classes.operations import Operation


def load_json_file(path_to_file):
    """
    Считываем файл формата json с операциями, возвращаем значения в виде словаря

    :param path_to_file: путь до файла, который считываем
    :return: данные из JSON представленных в виде списка словарей
    """
    with open(path_to_file, "rt", encoding="utf-8") as file_operation:
        return json.loads(file_operation.read())


def load_operations(path_to_file):
    """
    Считываем файл формата json с операциями, возвращаем список экземпляров класса Операции

    :param path_to_file: путь до файла, который считываем
    :return: список экземпляров класса Операции
    """
    return_list = []
    for input_dict in load_json_file(path_to_file):

        # Проверка на нулевые (пустые) словари из-за возможного присутствия ошибок во входном считываемом файле.
        if len(input_dict) > 0:
            # Проверка на операции открытия нового вклада, замена значения откуда совершен перевод.
            if "from" in input_dict:
                value_from = input_dict["from"]
            else:
                value_from = "Внесение денежных средств на счет"

            return_list.append(
                Operation(input_dict["id"], input_dict["date"], input_dict["state"], input_dict["operationAmount"],
                          input_dict["description"], value_from, input_dict["to"]))

    return return_list


def recent_transactions(input_operations_list):
    """
    Возвращает последние операции с сортировкой.
    Сверху списка находятся самые последние операции (по дате).

    :param input_operations_list: Список с экземплярами класса "Операции"
    :return: возвращает список с отсортированным экземплярами класса "Операции" по дате операции, по убыванию.
    """
    return sorted(input_operations_list, key=lambda x: x.date_operation, reverse=True)


def withdraw_operations(input_operations_list, number_operation):
    """
    Выводит информацию об операции в заданном формате

    :param input_operations_list: Список с экземплярами класса "Операции"
    :param number_operation: количество возвращаемых экземпляров
    :return: возвращаем собранный текст для вывода
    """
    return_text = ""
    for operation in recent_transactions(input_operations_list):
        if check_is_executed(operation.state) and number_operation > 0:
            return_text = return_text + convert_date_operation(operation.date_operation) + " " + operation.description \
                          + "\n" + convert_secret_account(operation.from_account) + " -> " \
                          + convert_secret_account(operation.to_account) + "\n" + operation.operation_amount["amount"] \
                          + " " + operation.operation_amount["currency"]["name"] + "\n\n"
            number_operation = number_operation - 1

    return return_text[:-2]


def convert_secret_account(account):
    """
    Маскируем информацию о счета/карте:
    - Номер карты замаскирован и не отображается целиком в формате: XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
    - Номер счета замаскирован и не отображается целиком в формате: **XXXX (видны только последние 4 цифры номера счета).
    - Фразу "Внесение денежных средств", если это открытие вклада

    :return: Возвращает скрытый номер счета/карты
    """

    if account[:4].lower() == "счет":
        return account[:account.rfind(' ')] + " **" + account[-4:]
    elif account[-4:].lower() == "счет":
        return account
    else:
        return account[:account.rfind(' ')] + " " + account[-16:-12] + " " + account[-12:-10] + "** **** " + account[-4:]


def convert_date_operation(date_operation):
    """
    Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).

    :return: Возвращает дату в заданном формате.
    """
    return date_operation[8:10] + "." + date_operation[5:7] + "." + date_operation[0:4]


def check_is_executed(state):
    """
    Проверяет успешная ли операция.

    :return: Возвращает Истину, если операция Успешная.
    """
    if state == "EXECUTED":
        return True
    else:
        return False