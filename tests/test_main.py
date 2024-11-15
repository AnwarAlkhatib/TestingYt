import pytest
from unittest import mock

from main import add, devide, play_random, ProductionClass

# TestParametrisieren
@pytest.mark.parametrize('input1, input2, expected', [(1,4,5),(1,7,8)])
def test_add(input1, input2, expected):
    result = add(input1, input2)
    assert result == expected


def test_devide():
    result = devide(10, 2)
    assert result == 5
    # Der Test besteht nur, wenn die Ausnahme tatsächlich auftritt.
    with pytest.raises(ZeroDivisionError):
        10  / 0

# @mock.patch Funktion ersetzt immer ein kompletes funktion (randint) oder Komplestes Objekt  
@mock.patch("main.randint", return_value=7)
def test_play_random(monkeypatch):
    result = play_random()
    assert result == "großer"


def test_ProductionClass():
    instanz = ProductionClass()
    instanz.something = mock.MagicMock()
    # "instanz.method()" soll aufgerufen werden, damit statt "somethin()" funktion, der mock objekt aufgerufen wird
    instanz.method()
    instanz.something.assert_called_once_with(1, 2, 3)





