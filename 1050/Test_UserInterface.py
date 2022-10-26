from pytest import MonkeyPatch
from City import City
from CityRepository import CityRepository
from UserInterface import UserInterface


def test_get_user_input(monkeypatch: MonkeyPatch):
    # Arrange
    city_repository = CityRepository()
    user_interface = UserInterface(city_repository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: "71")
    result = user_interface.get_user_input()

    # Assert
    assert result == 71
    assert type(result) == int

def test_get_ddd_by_user_input(monkeypatch: MonkeyPatch):
    #Arrange
    city_repository = CityRepository()
    user_interface = UserInterface(city_repository)

    #Act
    monkeypatch.setattr("builtins.input", lambda _: 31)
    city_repository.add_city_in_list(City(31, "Belo Horizonte"))
    resultTrue = user_interface.get_ddd_by_user()

    #Assert
    assert resultTrue == "Belo Horizonte"
    assert type(resultTrue) == str