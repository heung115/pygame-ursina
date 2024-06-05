from ursina import *
from pathlib import Path

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
