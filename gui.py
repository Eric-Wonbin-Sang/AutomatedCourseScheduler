from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager

from Stevens import Stevens
from ScheduleFiles import ScheduleCreator, ScheduleTests

from GUIElements import SelectorGroup, SelectorLayout, LayoutFactory, AppScreen, PageOne, PageTwo
from General import Functions, Constants


class ACSApp(App):

    def __init__(self):

        super().__init__()

        self.stevens = Stevens.Stevens(term_key="2020F")

        self.screen_manager = ScreenManager()

        self.screen_one = AppScreen.AppScreen(name="one", child_widget=PageOne.PageOne(acs_app=self, stevens=self.stevens))
        self.screen_two = AppScreen.AppScreen(name="two", child_widget=PageTwo.PageTwo(acs_app=self, stevens=self.stevens))

    def build(self):

        Functions.add_to_layout(
            self.screen_manager,
            self.screen_one,
            self.screen_two
        )

        return self.screen_manager


scalar = 1.1
Window.size = (int(500 * scalar), int(700 * scalar))
ACSApp().run()
