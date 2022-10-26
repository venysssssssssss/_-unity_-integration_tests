from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository


def test_produto_processado_com_preço_total():
    # Arrange
    customer1 = Customer(3, "Maria")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Milk", 43, 17)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 9)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert order.total_price == 387