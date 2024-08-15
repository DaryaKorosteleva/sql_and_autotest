import data
import create_order_get_info

#Коростелева Дарья, 20-ая когорта - Финальный проект. Инженер по тестированию плюс

def test_create_order():
    response_created_orders = create_order_get_info.post_create_order(data.create_orders)
    assert response_created_orders.status_code == 201


def test_get_info():
    response_get_info = create_order_get_info.get_order_by_track()
    assert response_get_info.status_code == 200
