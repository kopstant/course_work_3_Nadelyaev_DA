import pytest

from classes.operations import Operation


def test_str_operation():
    test_operation = Operation('441945886', 'EXECUTED', '2019-08-26T10:50:58.294041',
                               {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                               'Перевод организации', 'Maestro 1596837868705199', 'Счет 64686473678894779589')

    assert str(test_operation) == 'Operation = "441945886" | date_operation="EXECUTED"'
