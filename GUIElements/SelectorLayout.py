from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from GUIElements.SelectorPopup import SelectorPopup


class SelectorLayout(BoxLayout):

    def __init__(self, selector_group, stevens):
        super().__init__(
            orientation='horizontal',
            size_hint=(1, .2),
            pos_hint={'center_x': .5, 'center_y': .5},
            spacing=15,
            padding=10
        )

        self.selector_group = selector_group
        self.stevens = stevens

        self.selector_button = SelectorButton(stevens=self.stevens)
        self.remove_button = RemoveSelectorButton(self, self.selector_group)

        self.add_elements()

    def add_elements(self):
        self.add_widget(self.selector_button)
        self.add_widget(self.remove_button)

    def get_section_list_list(self):

        section_id_list_list = []
        for grid_layout in self.selector_button.selector_popup.section_layout.children:
            for i in range(int(len(grid_layout.children)/2)):
                scroll_view = grid_layout.children[i]
                for box_layout in scroll_view.children:
                    all_choice_layout = box_layout.children[-1]
                    choice_layout_list = box_layout.children[:-1]
                    if all_choice_layout.is_selected():
                        section_id_list_list.append([choice_layout.get_text() for choice_layout in choice_layout_list])
                    else:
                        section_id_list = []
                        for choice_layout in choice_layout_list:
                            if choice_layout.is_selected():
                                section_id_list.append(choice_layout.get_text())
                        section_id_list_list.append(section_id_list)

        section_list_list = []
        if self.selector_button.selector_popup.curr_course:
            for section_id_list in section_id_list_list:
                section_list = []
                for section in self.selector_button.selector_popup.curr_course.section_list:
                    if section.id in section_id_list:
                        section_list.append(section)
                section_list_list.append(section_list)
        return section_list_list


class RemoveSelectorButton(Button):

    def __init__(self, selector_layout, selector_group):
        super().__init__(
            text="Remove",
            size_hint=(.2, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.selector_layout = selector_layout
        self.selector_group = selector_group

    def on_press(self):
        if self.selector_group.children:
            self.selector_group.remove_widget(self.selector_layout)


class SelectorButton(Button):

    def __init__(self, stevens):

        super().__init__(
            text="No Course Selected",
            size_hint=(.4, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.stevens = stevens
        self.selector_popup = SelectorPopup(selector_button=self, stevens=self.stevens)

    def on_press(self):
        self.selector_popup.open()
