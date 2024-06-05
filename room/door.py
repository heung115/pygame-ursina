from ursina import *
from pathlib import Path
from menu.escape_success import escape_success_ui

# from main import escape_success

model_path = Path("asset/room/doorway.obj")


class Door(Entity):
    def __init__(self, position=(0, 0, 0), scale=1):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=position,
            collider="box",
            texture_scale=(10, 10),
        )
        self.is_open = False

    def open(self):
        if not self.is_open:  # 문이 닫혀 있을 경우
            self.is_open = True
            open_rotation = Vec3(0, -90, 0)
            self.animate(
                "rotation_y", open_rotation.y, duration=2, curve=curve.linear
            )  # 2초동안 오픈 애니메이션 적용
            print("Door opened!")
            invoke(self.escape_success, delay=2)

    def escape_success(self):
        escape_success_ui(0, True)  # 탈출 문 오픈 시 escape_success_ui 활성화
        mouse.locked = False
        mouse.visible = True
