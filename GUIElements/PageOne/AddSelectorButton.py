from kivy.uix.button import Button

from GUIElements.PageOne import SelectorLayout
from General import Functions


class AddSelectorButton(Button):

    def __init__(self, stevens, selector_group):

        super().__init__(
            text="+",
            size_hint=(.2, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_group = selector_group

    def on_press(self):
        self.selector_group.remove_widget(self)
        Functions.add_to_layout(
            self.selector_group,
            SelectorLayout.SelectorLayout(selector_group=self.selector_group,
                                          stevens=self.stevens,
                                          spec_course_name=""),
            self
        )
