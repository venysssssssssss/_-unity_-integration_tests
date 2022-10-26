from MenuRepository import MenuRepository
from Order import Order
from Menu import Menu


def test_get_user_input():
    result = "Oi OLA 3".split(" ")
    assert len(result) == 3
    assert result[0].isnumeric() == False
    assert result[1].isupper() == True
    assert result[2].isnumeric() == True


def test_get_total_price():
    menu_repository = MenuRepository()
    xsalada = Menu(2, "X-Salada", 4.50)
    menu_repository.set_menu_item(xsalada)
    order = Order(1, 5)

    assert xsalada.price * order.quantity == 22.50