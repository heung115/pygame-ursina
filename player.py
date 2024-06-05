from ursina.prefabs.first_person_controller import FirstPersonController
from inventory import Inventory
from ursina import *


class Player(FirstPersonController):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Player, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, **kwargs):
        if self._initialized:
            return
        super().__init__(**kwargs)
        self.inventory = Inventory(capacity=5)
        self.inventory.create_ui()  # 인벤토리 UI 생성
        self._initialized = True
        self.allow_movement = True
        self.hand_entity = None
        if not hasattr(self, "camera"):
            self.camera = camera

    def update(self):
        if self.allow_movement:
            super().update()

    def on_collect(self, item):
        print(f"Collecting {item.name}")
        if len(self.inventory.items) < self.inventory.capacity:
            self.inventory.add_item(item)
            item.disable()
        else:
            print("Inventory is full")

    def get_view_target(self, distance=100, debug=False):
        direction = self.camera.forward
        origin = self.world_position + Vec3(0, self.camera_pivot.y, 0)

        # 레이캐스트 실행
        hit_info = raycast(origin, direction, distance=distance, debug=debug)

        if hit_info.hit:
            return hit_info.entity
        else:
            return None

    def toggle_movement(self):  # 움직임 허용/비허용 전환 메서드
        self.allow_movement = not self.allow_movement

    # def update_hand_entity(self, item):
    #     if self.hand_entity == None:
    #         item.enable()
    #         self.hand_entity = duplicate(
    #             item,
    #             parent=camera,
    #             rotation=(0, 0, 0),
    #             scale=()
    #             position=Vec3(0.5, 0, 0.5),
    #             origin_z=-0.5,
    #         )
    #         item.disable()
