from kivy.uix.button import Button


class StartButton(Button):

    def __init__(self, stevens, selector_layout):

        super().__init__(
            text="Start Schedule Creation",
            size_hint=(.4, .1),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_layout = selector_layout

    def on_press(self):

        section_list = []
        for selector_object in self.selector_layout.children:
            section_list += selector_object.get_section_list()

        for section in section_list:

            print(section.section)

        print("-----------------")
