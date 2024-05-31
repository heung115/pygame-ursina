from ursina import *
from player import Player

player = Player()


class Lock(Entity):
    def __init__(
        self, model, position=(0, 0, 0), rotation=(0, 0, 0), scale=1, lock_num=0
    ):
        if not model:
            raise ValueError("Model must be provided")

        super().__init__(
            model=model,
            position=position,
            rotation=rotation,
            scale=scale,
            color=color.black,
            collider="box",
        )
        self.lock_num = lock_num
        self.is_locked = True

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
            self.disable()
            self.display_message(3)

    def display_message(self, duration=1):
        message = Text(test="Unlocked.", x=0, y=0, scale=2, color=color.white)
        invoke(message.disable, delay=duration)
