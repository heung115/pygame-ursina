from display_image.display_image import DisplayImage


class Image_01(DisplayImage):
    def __init__(self):
        super().__init__("asset/image/image_01.jpeg", scale=0.5)
        self.enabled = True
