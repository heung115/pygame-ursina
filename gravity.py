from ursina import Entity
from ursina import raycast, Vec3, scene


class AutoGravityEntity(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gravity = -0.05  # 중력 값 설정
        self.collider = "box"  # 박스 형태의 충돌체 설정

    def update(self):
        # 바닥면에서 레이캐스트 시작: 엔티티의 크기에 따라 조정
        ray_start_position = self.world_position + Vec3(0, -self.scale_y / 2, 0)

        # 레이캐스트를 사용하여 바닥 충돌 검사
        hit_info = raycast(
            ray_start_position,
            direction=Vec3(0, -1, 0),
            distance=abs(self.gravity) + 0.1,
            traverse_target=scene,
        )

        if hit_info.hit:
            # 레이캐스트가 무언가를 감지하면 y 위치를 충돌 지점 바로 위로 조정
            self.y = hit_info.world_point.y + self.scale_y / 2
        else:
            # 충돌이 없을 경우 중력 적용
            self.y += self.gravity

        if self.y < 0:  # 최소 높이 제한으로 땅을 더 이상 뚫지 않도록 설정
            self.y = 0
