from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from pathlib import Path

from player import Player
from lock import Lock
from room.room import setup_room
from lighting_setup import setup_lighting
from room.chair import Chair

app = Ursina()

# application.asset_folder = Path("asset")
Entity.default_shader = basic_lighting_shader
#
setup_room()

player = Player()

setup_lighting()

# editor_camera = EditorCamera()s

lock = Lock(position=(3, 1, 3), scale=(10), rotation=(0, 0, 0))
chair = Chair(position=(-3, 0, 0), rotation=(0, 0, 0), scale=5)

inventory_slots = []


def update_inventory_ui():
    for i, slot in enumerate(inventory_slots):
        if i < len(player.inventory.items):
            slot.text = player.inventory.items[i]
        else:
            slot.text = ""


def create_inventory_ui():
    for i in range(player.inventory.capacity):
        btn = Button(
            parent=camera.ui,
            text=str(i + 1),
            color=color.light_gray,
            highlight_color=color.cyan,
            pressed_color=color.lime,
            position=(0.1 * i - 0.45, -0.4),
            scale_x=0.08,
            scale_y=0.1,
            icon="white_cube",
        )
        inventory_slots.append(btn)


create_inventory_ui()


app.run()
