from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

from GUIElements import Selector


class AddSelectorButton(Button):

    def __init__(self, stevens, selector_layout):

        super().__init__(
            text="+",
            size_hint=(.2, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_layout = selector_layout

    def on_press(self):
        self.selector_layout.remove_widget(self)
        self.selector_layout.add_widget(Selector.Selector(self.selector_layout, stevens=self.stevens))
        self.selector_layout.add_widget(self)


class StartButton(Button):

    def __init__(self, stevens, selector_layout):

        super().__init__(
            text="Start Schedule Creation",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        # self.selector_layout = selector_layout

    def on_press(self):

        # section_list = []
        # for selector_object in self.selector_layout.children:
        #     section_list += selector_object.get_section_list()
        #
        # for section in section_list:
        #
        #     print(section.section)

        print("-----------------")


# class ImageButton(ButtonBehavior, Image):
#
#     def __init__(self, image_path, sound_path):
#         super(ImageButton, self).__init__(source=image_path, allow_stretch=True)
#
#         self.image_path = image_path
#         self.sound_path = sound_path
#
#     def on_press(self):
#         SoundLoader.load(self.sound_path).play()
