from ursina import *


class TurnImage(Entity):
    def __init__(self, image_path, scale, position, parent):
        super().__init__(
            parent=parent,
            model="quad",
            position=position,
            texture=load_texture(image_path),
            scale=scale,
        )
        self.enabled = False  # 초기에는 이미지 비활성화

    def show_image(self):
        self.enabled = True  # 이미지 활성화

    def hide_image(self):
        self.enabled = False  # 이미지 비활성화
