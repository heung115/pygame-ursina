from ursina import *
from pathlib import Path

model_path = Path("asset/room/bookcaseOpenLow.obj")


class BookCase(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=position,
            collider="box",
            texture_scale=(10, 10),
            rotation=rotation,
        )
