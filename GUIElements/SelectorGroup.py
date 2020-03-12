from kivy.uix.boxlayout import BoxLayout

from GUIElements import LayoutFactory


class SelectorGroup(LayoutFactory.make_layout(BoxLayout)):
    def __init__(self):
        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=10,
            background_color=(209, 209, 209)
        )
