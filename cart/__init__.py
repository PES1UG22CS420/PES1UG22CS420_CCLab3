import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []
            
    items=[]
    items_dict={}
    for cart_detail in cart_details:
        content=cart_detail['contents']
        items.extend(eval(content))
    i2=[]
    unique_items = set(items)  # Collect all unique items.
    products_info = {item: products.get_product(item) for item in unique_items}
    i2 = [products_info.get(i, items_dict.get(i)) for i in items]
    return i2


""" def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []
    
    items = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        evaluated_contents = json.loads(contents)  
        for content in evaluated_contents:
            items.append(content)
    
    i2 = []
    for i in items:
        temp_product = products.get_product(i)
        i2.append(temp_product)
    return i2 """



def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


