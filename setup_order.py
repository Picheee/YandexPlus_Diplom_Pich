import config
import data
import requests


def post_new_order(order_body):  # функция POST-запрос  на создание заказа
    return requests.post(config.URL + config.ORDER_CREATE_PATH, json=order_body)


def getting_order_data(track):
    return requests.get(config.URL + config.GET_ORDER_DATA_PATH, params=track)