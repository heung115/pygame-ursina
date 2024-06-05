from ursina import *
from menu.text_texture import create_text_texture
from player import Player

player = Player()


def pause_menu_ui(show_pause_menu=False):
    pause_menu = Entity(parent=camera.ui, enabled=show_pause_menu)
    player.inventory.disable_ui()

    background = Entity(
        parent=pause_menu,
        model="quad",
        texture="asset/UI/pause_menu.png",
        scale=(2, 1),
    )

    background2 = Entity(
        parent=pause_menu,
        model="quad",
        color=color.rgba(255, 255, 255, 0.2),
        scale=(1.5, 0.8),
    )

    pause_text_texture = create_text_texture("Pause", 256)
    pause_text_texture_path = "menu/pause_text.png"
    pause_text_texture.save(pause_text_texture_path)

    pause_text_entity = Entity(
        parent=pause_menu,
        model="quad",
        texture=pause_text_texture_path,
        scale=(0.3, 0.3),
        position=(-0.3, 0),
    )

    # 게임으로 돌아가기 버튼
    resume_button = Button(
        parent=pause_menu,
        text="Resume",
        scale=(0.3, 0.1),
        origin=(0, 0),
        position=(0.3, 0.1),
        on_click=lambda: resume_game(pause_menu),
    )

    # 게임 종료 버튼
    quit_button = Button(
        parent=pause_menu,
        text="Quit",
        scale=(0.3, 0.1),
        origin=(0, 0),
        position=(0.3, -0.1),
        on_click=quit_game,
    )

    return pause_menu


# 게임으로 돌아가기
def resume_game(pause_menu):
    pause_menu.disable()  # pause_menu 비활성화
    player.inventory.enable_ui()
    player.on_enable()
    # mouse.locked = True
    # mouse.visible = False # 마우스 감추기


# 게임 종료
def quit_game():
    application.quit()
