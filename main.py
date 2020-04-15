from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from StevensFiles import Stevens

from GUIElements import AppScreen
from GUIElements.PageTwo import PageTwo
from GUIElements.PageOne import PageOne
from General import Functions


class ACSApp(App):

    def __init__(self):

        super().__init__()

        self.stevens = Stevens.Stevens(term_key="2020F")
        self.schedule_list = []

        self.screen_manager = ScreenManager()

        self.screen_one = AppScreen.AppScreen(name="one",
                                              child_widget=PageOne.PageOne(acs_app=self, stevens=self.stevens))
        self.screen_two = AppScreen.AppScreen(name="two",
                                              child_widget=PageTwo.PageTwo(acs_app=self, stevens=self.stevens))

    def build(self):

        Functions.add_to_layout(
            self.screen_manager,
            self.screen_one,
            self.screen_two
        )

        return self.screen_manager


def main():

    scalar = 110
    window_width_ratio = 5
    window_height_ratio = 7

    Window.size = (int(window_width_ratio * scalar), int(window_height_ratio * scalar))
    ACSApp().run()


main()
