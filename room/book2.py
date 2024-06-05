from ursina import *
from pathlib import Path

model_path = Path("asset/room/books.obj")


class book2(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=(-9.7,1.5,-0.6),
            collider="box",
            texture_scale=(10, 10),
            rotation=rotation,
        )