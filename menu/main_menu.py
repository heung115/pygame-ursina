from ursina import *
from player import Player

player = Player()


def main_menu_ui():
    main_menu = Entity(parent=camera.ui, enabled=True)

    background = Entity(
        parent=main_menu,
        model="quad",
        texture="asset/UI/escape-room_2000.jpg",
        scale=(2, 1),
    )

    start_button = Button(
        text="Game Start",
        scale=(0.3, 0.1),
        position=(0, 0.05),
        parent=main_menu,
        on_click=lambda: start_game(main_menu),
    )

    close_button = Button(
        text="Game Close",
        scale=(0.3, 0.1),
        position=(0, -0.1),
        parent=main_menu,
        on_click=quit_game,
    )

    return main_menu


def start_game(main_menu):
    main_menu.disable()
    player.inventory.enable_ui()
    player.on_enable()
    mouse.locked = True
    mouse.visible = False


def quit_game():
    application.quit()
