from ursina import *

app = Ursina()

from ursina.shaders import basic_lighting_shader
from pathlib import Path
from player import Player

from room.room import setup_room
from lighting_setup import setup_lighting
from escape_item.escape_item_setting import setup_escape_item

# import menu
from menu.main_menu import main_menu_ui
from menu.pause_menu import pause_menu_ui


player = Player()
main_menu_ui()  # main_menu 활성화
player.inventory.disable_ui()
player.on_disable()

application.blender_paths["default"] = (
    "/Applications/Blender.app/Contents/MacOS/Blender"
)

application.fonts_folder = Path("asset/fonts")
# Entity.default_shader = basic_lighting_shader
setup_lighting()

# setting Enttity
item_entity = setup_escape_item()
setup_room(item_entity)
pause_state = False


def update():
    global pause_state
    if held_keys["1"]:
        # player.update_hand_entity(player.inventory.get_itme(0))
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
    if held_keys["p"]:
        print(player.inventory.list_items())
    if held_keys["escape"] and not pause_state:
        pause_state = True
        pause_menu_ui(True)
        mouse.locked = False
        mouse.visible = True


app.run()
