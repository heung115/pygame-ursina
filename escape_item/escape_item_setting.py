from ursina import *
from escape_item.lock_01 import Lock1
from escape_item.key_01 import Key1
from escape_item.book import Book
from escape_item.key_safe_box import Key_safe_box
from escape_item.frame import Frame
from room.computer import Computer

from escape_item.remote_control import RemoteControl
from display_image.image_01 import Image_01
from display_image.image_02 import Image_02
from display_image.image_03 import Image_03


def setup_image():
    image01 = Image_01()
    image01.hide_image()

    image02 = Image_02()
    image03 = Image_03()

    return {
        "image01": image01,
        "image02": image02,
        "image03": image03,
    }


def setup_escape_item():

    images = setup_image()

    lock = Lock1(position=(0.5, 2.6, -9.7), rotation=(0, 90, 0), scale=0.7, lock_num=1)
    key_safe_box = Key_safe_box(
        position=(-5.5, 2.3, 8.2), rotation=(0, 0, 0), scale=0.005, key_num=1
    )
    key_safe_box.enabled = False

    key03 = RemoteControl(
        position=(4, 5.3, 9), rotatison=(0, 0, 0), scale=0.006, key_num=3, name="R.C"
    )
    lock = Lock1(
        position=(5.9, 2.3, 8.95),
        rotation=(0, -90, 0),
        scale=0.6,
        lock_num=2,
        give_item=key03,
    )
    key02 = Key1(
        position=(4, 2.3, 9), rotation=(0, 0, 0), scale=0.006, key_num=2, name="key02"
    )

    book = Book(
        position=(-3.5, 1.93, 9),
        rotation=(0, 0, 0),
        scale=10,
        image=images["image01"],
    )

    frame = Frame(position=(9.8, 2, -1), rotation=(180, -90, 180), scale=2)
    images["image02"].parent = frame
    images["image02"].position = (0, 1.5, -0.05)
    images["image02"].scale = (3, 1.5)

    computer = Computer(position=(6.5, 2, 9), scale=(5), rotation=(0, 20, 0))
    images["image03"].parent = computer
    images["image03"].position = (0.195, 0.17, 0.048)
    images["image03"].rotation = (7.5, 0, 0)
    images["image03"].scale = (0.37, 0.23)

    return {
        "lock": lock,
        "key02": key02,
        "key_safe_box": key_safe_box,
        "book": book,
        "frame": frame,
    }
