from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader


class ImageButton(ButtonBehavior, Image):

    def __init__(self, image_path, sound_path):
        super(ImageButton, self).__init__(source=image_path, allow_stretch=True)

        self.image_path = image_path
        self.sound_path = sound_path

    def on_press(self):
        SoundLoader.load(self.sound_path).play()
