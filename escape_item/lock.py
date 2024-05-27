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

    def input(self, key):
        if key == "right mouse down" and mouse.hovered_entity == self:

            if player.inventory.has_item("key"):
                self.unlock(player.inventory.items["key"])
            else:
                print("No key in inventory.")
                self.display_message("No key in inventory.")

    def unlock(self, key_number):
        if self.is_locked:
            if key_number == self.lock_num:
                self.is_locked = False
                print("Lock has been unlocked!")
                self.disable()
            else:
                print("Wrong key! Lock is still locked.")
        else:
            print("Lock is already unlocked.")


# class CustomLock(Lock):
#     def __init__(self, model, **kwargs):
#         super().__init__(model, **kwargs)
