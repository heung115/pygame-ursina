from ursina import *


class DisplayImage(Entity):
    def __init__(self, image_path, scale):
        super().__init__(
            parent=camera.ui,
            model="quad",
            texture=load_texture(image_path),
            scale=scale,
        )
        self.enabled = False  # 초기에는 이미지 비활성화

    def show_image(self):
        self.enabled = True  # 이미지 활성화

    def hide_image(self):
        self.enabled = False  # 이미지 비활성화
