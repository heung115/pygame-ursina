from ursina import *
from pathlib import Path

model_path_close = Path("asset/escape_item/safe_close.obj")
model_path_open = Path("asset/escape_item/safe_open.obj")


class SafeBox(Entity):
    def __init__(self, position, scale, rotation, key_to_show):
        super().__init__(
            model=str(model_path_close),
            scale=scale,
            position=(-5.5, 1.9, 9),
            collider="box",
            texture_scale=(10, 10),
            rotation=rotation,
            color=color.dark_gray,
        )
        self.is_locked = True
        self.key_to_show = key_to_show

    def input(self, key):
        if key == "right mouse down" and mouse.hovered_entity == self:
            if self.is_locked:
                self.show_password_screen()
                mouse.locked = False
                mouse.visible = True

    def show_password_screen(self):
        self.password_input = InputField(
            default_value="",
            limit_content_to="1234567890",
            max_lines=1,
            # scale=(0.5,0.05),
            position=window.center,
        )

        self.submit_button = Button(
            text="Submit",
            scale=(0.2, 0.05),
            position=(0, -0.2),
            on_click=self.check_password,
        )

    def check_password(self):
        if self.password_input.text == "1234":
            self.unlock()

        else:
            self.password_input.disable()
            self.submit_button.disable()
            print("Fail!")

            mouse.locked = True
            mouse.visible = False

    def unlock(self):
        self.is_locked = False
        self.password_input.disable()
        self.submit_button.disable()
        print("SafeBox is unlocked!")

        self.model = str(model_path_open)
        self.key_to_show.enabled = True

        mouse.locked = True
        mouse.visible = False
