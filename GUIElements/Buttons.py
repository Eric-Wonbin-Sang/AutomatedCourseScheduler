from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

from GUIElements import Selector
from GUIElements.SelectorPopup import SelectorPopup


class AddSelectorButton(Button):

    def __init__(self, stevens, selector_layout):

        super().__init__(
            text="+",
            size_hint=(.1, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_layout = selector_layout

    def on_press(self):
        self.selector_layout.remove_widget(self)
        self.selector_layout.add_widget(Selector.Selector(self.selector_layout, stevens=self.stevens))
        self.selector_layout.add_widget(self)


class RemoveSelectorButton(Button):

    def __init__(self, selector, selector_layout):
        super().__init__(
            text="Remove",
            size_hint=(.2, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.selector = selector
        self.selector_layout = selector_layout

    def on_press(self):
        if self.selector_layout.children:
            self.selector_layout.remove_widget(self.selector)


class PopupCloseButton(Button):

    def __init__(self, pop_up):

        super().__init__(
            text="Close popup",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.pop_up = pop_up

    def on_press(self):
        self.pop_up.dismiss()


class SelectorButton(Button):

    def __init__(self, stevens):

        super().__init__(
            text="Selector Button",
            size_hint=(.4, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_popup = SelectorPopup(self.stevens)

    def on_press(self):
        self.selector_popup.open()


class StartButton(Button):

    def __init__(self, stevens, selector_layout):

        super().__init__(
            text="Start Schedule Creation",
            size_hint=(.6, .1),
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


class ImageButton(ButtonBehavior, Image):

    def __init__(self, image_path, sound_path):
        super(ImageButton, self).__init__(source=image_path, allow_stretch=True)

        self.image_path = image_path
        self.sound_path = sound_path

    def on_press(self):
        SoundLoader.load(self.sound_path).play()
