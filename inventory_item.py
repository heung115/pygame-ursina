from ursina import *
from gravity import AutoGravityEntity
from abc import ABC, abstractmethod
from player import Player
from CommonMeta import CommonMeta

player = Player()


class InventoryItem(Entity, ABC, metaclass=CommonMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def input(self, item):
        if item == "right mouse down" and mouse.hovered_entity == self:
            print(f"{self.name} collected by player.")
            player.inventory.add_item(self)
            self.disable()

    @abstractmethod
    def use(self):
        pass
