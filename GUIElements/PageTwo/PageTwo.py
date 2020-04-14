from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

from GUIElements import LayoutFactory
from General import Functions


class PageTwo(LayoutFactory.make_layout(BoxLayout)):

    def __init__(self, acs_app, stevens):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(255, 255, 255),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.acs_app = acs_app
        self.stevens = stevens

        self.schedule_arrow_group = self.get_schedule_arrow_group()

        self.add_components()

    def get_schedule_arrow_group(self):

        schedule_arrow_group = LayoutFactory.make_layout(BoxLayout)(
            orientation="horizontal",
            spacing=15,
            padding=10,
            size_hint=(1, 1),
            background_color=(255, 255, 255),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        back_button = Button(
            text="<",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        forward_button = Button(
            text=">",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        Functions.add_to_layout(
            schedule_arrow_group,
            back_button,
            forward_button
        )

        return schedule_arrow_group

    def add_components(self):
        Functions.add_to_layout(
            self,
            self.schedule_arrow_group
        )
