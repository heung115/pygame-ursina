from ursina import Entity

model_path = "asset/room/.obj"


class Wall(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model="cube",
            scale=scale,
            position=position,
            rotation=rotation,
            collider="box",
            texture_scale=(10, 3),
        )
