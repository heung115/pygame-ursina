from ursina import *

def pause_menu_ui(show_pause_menu=False):
    pause_menu = Entity(parent=camera.ui, enabled=show_pause_menu)

    background = Entity(
        parent=pause_menu,
        model='quad',
        texture='asset/UI/pause_menu.png',
        scale=(2, 1),
    )

    background2 = Entity(
        parent=pause_menu,
        model='quad',
        color=color.rgba(255, 255, 255, 0.2),
        scale=(1.5, 0.8),
    )

    pause_text = Text(
        parent=pause_menu,
        text='Pause',
        scale= 4,
        origin=(0, 0),
        position=(-0.3, 0),
        color=color.light_gray,
    )

    # 게임으로 돌아가기 버튼
    resume_button = Button(
        parent=pause_menu,
        text='Resume',
        scale=(0.3, 0.1),
        origin=(0, 0),
        position=(0.3, 0.1),
        on_click= lambda: resume_game(pause_menu)
    )

    # 게임 종료 버튼
    quit_button = Button(
        parent=pause_menu,
        text='Quit',
        scale=(0.3, 0.1),
        origin=(0, 0),
        position=(0.3, -0.1),
        on_click=quit_game
    )

    return pause_menu

# 게임으로 돌아가기
def resume_game(pause_menu):
    pause_menu.disable() # pause_menu 비활성화
    mouse.locked = True
    mouse.visible = False # 마우스 감추기

# 게임 종료
def quit_game():
    application.quit()