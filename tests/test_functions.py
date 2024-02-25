import pytest

from classes.operations import Operation
from utils import functions


@pytest.fixture
def coll_dict_test():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'},
            {}
            ]


def test_load_json_file(coll_dict_test):
    assert functions.load_json_file("tests/src/test_operations_2_entry.json") == coll_dict_test


@pytest.fixture
def coll_operation_test():
    return_list = [Operation("441945886", "2019-08-26T10:50:58.294041", "EXECUTED",
                             {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589"),
                   Operation("710136990", "2018-08-17T03:57:28.607101", "CANCELED",
                             {'amount': '66906.45', 'currency': {'name': 'USD', 'code': 'USD'}},
                             "Перевод организации", "Maestro 1913883747791351", "Счет 11492155674319392427"),
                   Operation("893507143", "2018-02-03T07:16:28.366141", "EXECUTED",
                             {'amount': '90297.21', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             "Открытие вклада", "Внесение денежных средств на счет", "Счет 37653295304860108767")]
    return return_list


def test_load_operations(coll_operation_test):
    assert print(functions.load_operations("tests/src/test_operations_4_entry.json")) == print(coll_operation_test)


def test_recent_transactions(coll_operation_test):
    assert print(functions.recent_transactions(coll_operation_test)) == print(coll_operation_test)


def test_withdraw_operations(coll_operation_test):
    text_test = "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n\n" \
                "03.02.2018 Открытие вклада\nВнесение денежных средств на счет -> Счет **8767\n90297.21 руб."
    assert functions.withdraw_operations(coll_operation_test, 2) == text_test


@pytest.mark.parametrize('account, expected', [
    ("Visa Classic 4195191172583802", "Visa Classic 4195 19** **** 3802"),
    ("Maestro 3364923093037194", "Maestro 3364 92** **** 7194"),
    ("Счет 96292138399386853355", "Счет **3355"),
    ("Внесение денежных средств на счет", "Внесение денежных средств на счет")

])
def test_convert_secret_account(account, expected):
    assert functions.convert_secret_account(account) == expected


@pytest.mark.parametrize('date_operation, expected', [
    ("2019-12-03T04:27:03.427014", "03.12.2019"),
    ("2019-04-19T12:02:30.129240", "19.04.2019"),
    ("2018-06-12T07:17:01.311610", "12.06.2018")

])
def test_convert_date_operation(date_operation, expected):
    assert functions.convert_date_operation(date_operation) == expected


@pytest.mark.parametrize('state, expected', [
    ("EXECUTED", True),
    ("CANCELED", False),
    (" ", False),
    (None, False),
    ("", False)

])
def test_check_is_executed(state, expected):
    assert functions.check_is_executed(state) == expected


