from display_image.display_image import DisplayImage


class Image_02(DisplayImage):
    def __init__(self):
        super().__init__("asset/image/image_02.png", scale=1)
        self.enabled = True
