from ursina import *
from pathlib import Path

model_path = Path("asset/room/bookcaseOpen.obj")


class bookcase2(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=(-10,0,-1),
            collider="box",
            texture_scale=(10, 10),
            rotation=rotation,
        )
