from ursina import *
from pathlib import Path

model_path = Path("asset/escape_item/lock_1.obj")


class Lock1(Entity):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), scale=1, lock_num=0):
        super().__init__(
            model=str(model_path),
            position=position,
            rotation=rotation,
            collider="box",
            scale=scale,
        )
        self.lock_num = lock_num
        self.is_locked = True

    def unlock(self, key_number):
        if self.is_locked:  # 자물쇠가 잠겨 있을 경우에만 확인
            if key_number == self.lock_num:
                self.is_locked = False  # 열쇠 번호가 맞으면 잠금 해제
                print("Lock has been unlocked!")  # 잠금 해제 메시지 출력
                self.disable()
            else:
                print(
                    "Wrong key! Lock is still locked."
                )  # 열쇠 번호가 틀리면 여전히 잠금 상태

        else:
            print("Lock is already unlocked.")  # 이미 잠금이 해제된 상태임을 알림
