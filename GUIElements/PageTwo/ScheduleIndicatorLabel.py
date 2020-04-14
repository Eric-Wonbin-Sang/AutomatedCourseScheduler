from General import Kiveasy


class ScheduleIndicatorLabel(Kiveasy.Label):

    def __init__(self, page_two):

        self.page_two = page_two

        super().__init__(
            text=self.label_text()
        )

    def update(self):
        self.text = self.label_text()

    def label_text(self):
        return "Schedule #{}".format(self.page_two.curr_schedule_index + 1)
