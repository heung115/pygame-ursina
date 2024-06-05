from ursina import *
from pathlib import Path

model_path = Path("asset/room/loungeSofa.obj")


class LoungeSofa(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=(5),
            position=(4, 0, -2),
            collider="box",
            texture_scale=(10, 10),
            rotation=(0, 0, 0)
        )