from ursina import *
from menu.text_texture import create_text_texture

def escape_success_ui(escape_time_seconds, show_success_menu=False):
    success_menu = Entity(parent=camera.ui,  enabled=show_success_menu)

    background = Entity(
        parent=success_menu,
        model='quad',
        texture='asset/UI/escape-room_2000.jpg',
        scale=(2, 1),
    )

    end_text_texture = create_text_texture('Escape Success!',500)
    end_text_texture_path = 'menu/end_text.png'
    end_text_texture.save(end_text_texture_path)

    end_text_entity = Entity(
        parent=success_menu,
        model='quad',
        texture=end_text_texture_path,
        scale=(1, 1),
        origin=(0, 0),
        position=(0, 0.1),
        color=color.lime
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
