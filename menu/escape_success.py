from ursina import *


def escape_success_ui(escape_time_seconds, show_success_menu=False):
    success_menu = Entity(parent=camera.ui,  enabled=show_success_menu)

    background = Entity(
        parent=success_menu,
        model='quad',
        texture='asset/UI/escape-room_2000.jpg',
        scale=(2, 1),
    )

    success_message = Text(
        parent=success_menu,
        text="Escape Success!",
        origin=(0, 0),
        position=(0, 0.1),
        scale=3,
        color=color.lime,
    )

    time_message = Text(
        parent=success_menu,
        text=f"Time: {escape_time_seconds}s",
        origin=(0, 0),
        position=(0, 0.2),
        scale=1.5,
        color=color.black,
    )

    # 게임 종료 버튼
    quit_button = Button(
        parent=success_menu,
        text="Quit",
        origin=(0, 0),
        position=(0, -0.1),
        scale=(0.3, 0.1),
        on_click=quit_game,
    )

# 게임 종료
def quit_game():
    application.quit()
