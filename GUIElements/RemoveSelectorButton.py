from kivy.uix.button import Button


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
