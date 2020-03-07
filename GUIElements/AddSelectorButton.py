from kivy.uix.button import Button

from GUIElements import Selector


class AddSelectorButton(Button):

    def __init__(self, stevens, selector_layout):

        super().__init__(
            text="Add Selector",
            size_hint=(.4, .1),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_layout = selector_layout

    def on_press(self):
        self.selector_layout.add_widget(Selector.Selector(self.selector_layout, stevens=self.stevens))
