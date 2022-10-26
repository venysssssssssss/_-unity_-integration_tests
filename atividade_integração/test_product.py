from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository


def test_produto_processado_com_estoque():
    # Arrange
    customer1 = Customer(3, "Maria")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(4, "Noodle", 50, 20)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 5)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert product1.get_stock() == 15


def test_estoque_baixo():
    product1 = Product(2, "Bean", 10, 85)

    # Act
    product1.down_stock(15)

    # Assert
    assert product1.get_stock() == 70
    assert type(product1.get_stock()) == int