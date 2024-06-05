from ursina import *
from pathlib import Path

model_path_closed_door = Path("asset/room/bookcaseClosedDoors.obj")
model_path_closed_open = Path("asset/room/bookcaseClosed.obj")


class Bookcase_Closed(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path_closed_door),
            scale=scale,
            position=position,
            collider="box",
            texture_scale=(10, 10),
            rotation=rotation,
        )
        self.is_open = False

    def input(self, key):
        if key == "right mouse down" and mouse.hovered_entity == self:
            if not self.is_open:
                self.is_open = True
                self.model = str(model_path_closed_open)
            else:
                self.is_open = False
                self.model = str(model_path_closed_door)
