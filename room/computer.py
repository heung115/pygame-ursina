from ursina import *
from pathlib import Path

model_path = Path("asset/room/computerScreen.obj")


class Computer(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=position,
            collider="box",
            texture_scale=(6, 6),
            rotation=rotation,
        )
