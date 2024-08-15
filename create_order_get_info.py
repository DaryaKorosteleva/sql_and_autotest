import data
import configuration
import requests

def post_create_order(order_data):
    url = configuration.URL + configuration.CREATE_ORDERS
    response = requests.post(url=url, json=order_data)
    return response


def save_track():
    order_track = post_create_order(data.create_orders)
    order_track_number = order_track.json()["track"]
    return order_track_number


def get_order_by_track():
    track = save_track()
    return requests.get(configuration.URL + configuration.GET_ORDERS + str(track))

