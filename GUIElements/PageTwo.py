from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager

from Stevens import Stevens
from ScheduleFiles import ScheduleCreator, ScheduleTests

from GUIElements import SelectorGroup, SelectorLayout, LayoutFactory, AppScreen, PageOne
from General import Functions, Constants


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
        self.loading_image_path = "Images/loading.gif"
        self.loading_image = self.get_loading_image()

        self.add_components()

    def get_loading_image(self):
        return Image(
            source=self.loading_image_path,
            size_hint=(1, None)
        )

    def add_components(self):
        Functions.add_to_layout(
            self,
            self.loading_image
        )
