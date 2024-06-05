from ursina import *
from pathlib import Path

model_path = Path("asset/room/rugRound.obj")


class rug(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=(10),
            position=(-6.5, 0.1, -6.5),
            collider="box",
            texture_scale=(40, 40),
            rotation=(0, 0, 0),
        )