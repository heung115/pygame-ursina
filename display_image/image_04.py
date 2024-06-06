from display_image.display_image import DisplayImage


class Image_04(DisplayImage):
    def __init__(self):
        super().__init__("asset/image/image_04.jpeg", scale=0.5)
        self.enabled = True
