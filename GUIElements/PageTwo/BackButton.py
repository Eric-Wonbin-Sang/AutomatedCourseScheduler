from kivy.uix.button import Button
from kivy.uix.label import Label

from General import Functions


class BackButton(Button):

    def __init__(self, acs_app, page_two):

        super().__init__(
            text="<",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.acs_app = acs_app
        self.page_two = page_two

    def on_press(self):
        if self.acs_app.schedule_list:

            Functions.clear_layout(self.page_two.schedule_layout)

            self.page_two.curr_schedule_index += -1
            label = Label(text=self.acs_app.schedule_list[self.page_two.curr_schedule_index])

            Functions.add_to_layout(
                self.page_two.schedule_layout,
                label
            )
