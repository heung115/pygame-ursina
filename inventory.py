from ursina import *


class Inventory:
    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity
        self.ui_slots = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            popup_text = Text(f"Added {item} to inventory.")
            destroy(popup_text, delay=1)
            self.update_ui()
        else:
            print("Inventory is full.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from inventory.")
            self.update_ui()

    def list_items(self):
        return self.items

    def has_item(self, item_name):
        return item_name in [item.name for item in self.items]

    def update_ui(self):
        for i, slot in enumerate(self.ui_slots):
            if i < len(self.items):
                slot.text = self.items[i].name
                slot.icon = self.items[i].icon_path
                slot.texture = self.items[i].icon_path

            else:
                slot.text = ""
                slot.icon = "white_cube"

    def create_ui(self):
        for i in range(self.capacity):
            btn = Button(
                parent=camera.ui,
                text=str(i + 1),
                color=color.white,
                highlight_color=color.cyan,
                pressed_color=color.lime,
                position=(0.1 * i - 0.45, -0.4),
                scale_x=0.08,
                scale_y=0.1,
                icon="white_cube",
                text_origin=(0, 0),
                texture="asset/UI/panel-004.png",
            )
            btn.text_entity.color = color.black
            btn.text_entity.z = -1  # 텍스트를 버튼보다 앞으로 설정
            self.ui_slots.append(btn)

    def use_item(self, index):
        if 0 <= index < len(self.items):
            item = self.items[index]
            if hasattr(item, "use"):
                print(f"item name : {item}.")
                item.use()
                print(f"Used {item.name}.")
            else:
                print(f"No use function for {item.name}.")
        else:
            print("No item in this slot.")

    def enable_ui(self):
        for slot in self.ui_slots:
            slot.enabled = True

    def disable_ui(self):
        for slot in self.ui_slots:
            slot.enabled = False

    def get_itme(self, index):
        return self.items[index]
