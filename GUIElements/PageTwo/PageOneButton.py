from kivy.uix.button import Button


class PageOneButton(Button):

    def __init__(self, acs_app):

        super().__init__(
            text="Go back",
            size_hint=(.2, None),
            size=(30, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.acs_app = acs_app

    def on_press(self):
        self.acs_app.screen_manager.current = "one"
