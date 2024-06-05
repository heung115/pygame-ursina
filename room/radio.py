from ursina import *
from pathlib import Path

model_path = Path("asset/room/radio.obj")


class Radio(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=(5),
            position=(7, 1.2, -4),
            collider="box",
            texture_scale=(10, 10),
            rotation=(0, 180, 0),
        )
        self.is_turn_on = False
        self.bg_music = Audio(
            "asset/background_music.mp3", loop=True, autoplay=True, volume=0.01
        )
        self.radio_music = Audio("asset/radio_music_morsecode.mp3", autoplay=False)

    def input(self, key):
        if key == "right mouse down" and mouse.hovered_entity == self:
            self.play_radio()

    def play_radio(self):
        if self.is_turn_on:
            self.stop_radio()
        else:
            self.start_radio()

    def start_radio(self):
        self.is_turn_on = True
        self.bg_music.pause()
        self.radio_music.play()

    def stop_radio(self):
        self.radio_music.stop()
        self.bg_music.resume()
        self.is_turn_on = False

    def radio_music_end(self):
        if self.is_turn_on:
            self.bg_music.resume()
            self.is_turn_on = False

    def update(self):
        if self.is_turn_on and not self.radio_music.playing:
            self.radio_music_end()
