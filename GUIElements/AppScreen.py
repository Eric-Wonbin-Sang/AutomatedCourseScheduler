from kivy.uix.screenmanager import Screen

from General import Functions


class AppScreen(Screen):

    def __init__(self, **kwargs):

        self.child_widget = kwargs.get("child_widget")

        super().__init__(**Functions.remove_from_dict(kwargs, "child_widget"))

        self.add_widget(self.child_widget)
