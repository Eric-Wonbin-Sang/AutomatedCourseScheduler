import datetime

from ScheduleFiles import ScheduleTests

from General import Constants, Functions


class Section:

    activity_dict = {
        "LEC": "Lecture",
        "PRA": "Practice",
        "QUZ": "Quiz",
        "L/L": "Lecture / Lab",
        "RCT": "Recitation",
        "SEM": "Seminar",
        "LAB": "Lab",
        "None": "None"
    }

    def __init__(self, parent_course, xml):

        self.xml = xml

        self.main_attrib_dict, self.meeting_dict_list, self.requirement_dict_list = self.get_dictionaries()

        self.section = self.main_attrib_dict.get("section")
        self.title = self.main_attrib_dict.get("title")
        self.call_number = self.main_attrib_dict.get("call_number")
        self.activity = str(Functions.find_first_occurrence_in_dicts("activity", *self.meeting_dict_list))
        self.room = Functions.find_first_occurrence_in_dicts("room", *self.meeting_dict_list)
        self.min_credit = self.main_attrib_dict.get("min_credit")
        self.max_credit = self.main_attrib_dict.get("max_credit")

        self.subject_id, self.course_id, self.id = self.get_subject_course_section_id_list()
        self.parent_course = parent_course

        self.day_list = Functions.find_first_occurrence_in_dicts("day", *self.meeting_dict_list)

        self.start_time, self.end_time = self.get_times()
        self.time_dict = self.get_time_dict()

    def get_dictionaries(self):

        main_attrib_dict = {}
        meeting_dict_list = []
        requirement_dict_list = []

        for element in self.xml.iter():
            if element.tag == "Course":
                main_attrib_dict = Functions.clean_dict(element.attrib)
            elif element.tag == "Meeting":
                meeting_dict_list.append(Functions.clean_dict(element.attrib))
            elif element.tag == "Requirement":
                requirement_dict_list.append(Functions.clean_dict(element.attrib))
            else:
                print("Different Element Tag: " + element.tag)

        return main_attrib_dict, meeting_dict_list, requirement_dict_list

    def get_subject_course_section_id_list(self):

        data_list = Functions.string_to_alternating_letter_to_num(self.section)

        subject_identifier = data_list[0]
        course_identifier = data_list[1]
        section_identifier = "".join(data_list[2:])

        return subject_identifier, course_identifier, section_identifier

    def get_times(self):

        start_time = Functions.find_first_occurrence_in_dicts("start_time", *self.meeting_dict_list)
        end_time = Functions.find_first_occurrence_in_dicts("end_time", *self.meeting_dict_list)

        if (self.subject_id + self.course_id).replace(" ", "").lower() in ScheduleTests.test_schedule_0:
            print("{}: \t{} - {}\t{}".format(
                (self.subject_id + self.course_id + self.id).replace(" ", "").lower(),
                start_time,
                end_time,
                self.day_list
            )
            )

        if type(start_time) == str and type(end_time) == str:
            split_start_time = str(start_time).split(":")
            split_end_time = str(end_time).split(":")

            start_time = [int(split_start_time[0]), int(split_start_time[1])]
            end_time = [int(split_end_time[0]), int(split_end_time[1])]

            if start_time[0] < Constants.minimum_section_start:
                start_time[0] += 12
                end_time[0] += 12

            if (self.subject_id + self.course_id).replace(" ", "").lower() in ScheduleTests.test_schedule_0:
                print("\t", start_time[0], start_time[1], "\t | ", end_time[0], end_time[1])

            if start_time[0] > 24:
                start_time[0] -= 12
                if (self.subject_id + self.course_id).replace(" ", "").lower() in ScheduleTests.test_schedule_0:
                    print("\ttime changed")
            if end_time[0] > 24:
                end_time[0] -= 12
                if (self.subject_id + self.course_id).replace(" ", "").lower() in ScheduleTests.test_schedule_0:
                    print("\ttime changed")

            start_time = datetime.time(start_time[0], start_time[1])
            end_time = datetime.time(end_time[0], end_time[1])

            if (self.subject_id + self.course_id).replace(" ", "").lower() in ScheduleTests.test_schedule_0:
                print("\t", start_time.strftime('%I:%M %p'), " | ", end_time.strftime('%I:%M %p'))

        return start_time, end_time

    def get_time_dict(self):
        if self.day_list != "TBA" and self.start_time and self.end_time:
            return {day: (self.start_time, self.end_time) for day in self.day_list}
        return {}

    def __str__(self, **kwargs):
        header = "Section: {}".format(self.id)
        if kwargs.get("print_section_dicts"):
            ret_str = Functions.dict_to_string(self.main_attrib_dict, "main_attrib_dict")
            for i, meeting_dict in enumerate(self.meeting_dict_list):
                ret_str += "\n" + Functions.dict_to_string(meeting_dict, "meeting_dict: count = " + str(i))
            for i, requirement_dict in enumerate(self.requirement_dict_list):
                ret_str += "\n" + Functions.dict_to_string(requirement_dict, "requirement_dict: count = " + str(i))
            return header + "\n" + Functions.tab_string(ret_str)
        return header
