from ursina import Entity


class InventoryItem(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_collect(self, player):
        print(f"{self.name} collected by player.")
        if hasattr(player, "inventory"):
            player.inventory.add_item(self)
            self.disable()
