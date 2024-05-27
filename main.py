from ursina import *

app = Ursina()

from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from pathlib import Path

from player import Player

from ursina.prefabs.first_person_controller import FirstPersonController

from lock import Lock
from room.room import setup_room
from lighting_setup import setup_lighting
from room.chair import Chair
from escape_item.lock_01 import Lock1
from escape_item.escape_item_setting import setup_escape_item

app = Ursina()

player = Player()
# application.asset_folder = Path("asset")
Entity.default_shader = basic_lighting_shader
setup_lighting()
# player = FirstPersonController(y=2, origin_y=-0.5)
# setting Enttity
setup_room()
setup_escape_item()


# editor_camera = EditorCamera()s

# lock = Lock(position=(3, 1, 3), scale=(10), rotation=(0, 0, 0))
inventory_slots = []

# player.inventory.create_ui()


# def update():
#     # 테스트를 위해 'u' 키를 누를 때 잠금 시도
#     if held_keys["u"]:
#         lock.unlock(1)  # 올바른 열쇠 번호로 잠금 해제


app.run()
