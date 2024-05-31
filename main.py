from ursina import *

app = Ursina()

from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from pathlib import Path
import time
from player import Player

from ursina.prefabs.first_person_controller import FirstPersonController

from room.room import setup_room
from lighting_setup import setup_lighting
from room.chair import Chair
from escape_item.lock_01 import Lock1
from escape_item.escape_item_setting import setup_escape_item
from menu.main_menu import main_menu_ui


player = Player()
main_menu_ui()  # main_menu 활성화
player.inventory.disable_ui()
player.on_disable()
application.blender_paths["default"] = (
    "/Applications/Blender.app/Contents/MacOS/Blender"
)
application.fonts_folder = Path("asset/fonts")
Entity.default_shader = basic_lighting_shader
setup_lighting()

# setting Enttity
setup_room()
setup_escape_item()


def update():
    # 키 입력에 따라 인벤토리의 아이템 사용
    if held_keys["1"]:
        player.inventory.use_item(0)
    if held_keys["2"]:
        player.inventory.use_item(1)
    if held_keys["3"]:
        player.inventory.use_item(2)
    if held_keys["4"]:
        player.inventory.use_item(3)
    if held_keys["5"]:
        player.inventory.use_item(4)
    if held_keys["k"]:
        player.inventory.disable_ui()
    if held_keys["l"]:
        player.inventory.enable_ui()


app.run()
