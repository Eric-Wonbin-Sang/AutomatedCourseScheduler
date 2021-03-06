from kivy.uix.button import Button

from ScheduleFiles import ScheduleCreator


class StartButton(Button):

    def __init__(self, acs_app, stevens, selector_group):

        super().__init__(
            text="Start Schedule Creation",
            size_hint=(.6, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        self.acs_app = acs_app
        self.stevens = stevens
        self.selector_group = selector_group

    def on_press(self):
        section_list_list = []
        for selector_layout in self.selector_group.children[1:]:
            section_list_list += selector_layout.get_section_list_list()

        schedule_list = ScheduleCreator.get_schedule_list(section_list_list=section_list_list)

        for i, schedule in enumerate(schedule_list):
            print("{})\t{}".format(i + 1, schedule.url))
        print("------------------")
        self.acs_app.schedule_list = schedule_list
        self.acs_app.screen_two.child_widget.schedule_arrow_group.schedule_indicator_label.update()

        if schedule_list:
            self.acs_app.screen_two.child_widget.schedule_layout.update_schedule(schedule_list[0])

        self.acs_app.screen_manager.current = "two"
