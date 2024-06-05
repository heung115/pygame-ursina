from ursina import *
from pathlib import Path

# pathlib을 사용하여 모델 경로 설정
model_path = Path("asset/room/ceilingFan.obj")


class Ceiling_Fan(Entity):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), scale=1):
        super().__init__(
            model=str(model_path),
            position=position,
            rotation=rotation,
            collider="box",
            scale=scale,
        )
