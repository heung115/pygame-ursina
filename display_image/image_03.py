from display_image.display_image import DisplayImage


class Image_03(DisplayImage):
    def __init__(self):
        super().__init__("asset/image/image_03.jpg", scale=0.5)
        self.enabled = True
