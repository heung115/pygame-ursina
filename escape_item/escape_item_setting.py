from ursina import *
from escape_item.lock_01 import Lock1
from escape_item.key_01 import Key1


def setup_escape_item():

    lock = Lock1(position=(0, 0, 0), rotation=(0, 0, 0), scale=1, lock_num=1)
    key = Key1(position=(5, 5, 5), rotation=(0, 0, 0), scale=0.05, key_num=1)
    print()
