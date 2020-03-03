import Functions
import Constants
import datetime


class Section:

    def __init__(self, child_obj):

        self.child_obj = child_obj

        # Dictionary: main_attrib_dict
        #     Key: Section            -->     PEP 112RB
        #     Key: Title              -->     Electricity & Magnet
        #     Key: CallNumber         -->     11527
        #     Key: MinCredit          -->     3
        #     Key: MaxCredit          -->     3
        #     Key: MaxEnrollment      -->     30
        #     Key: CurrentEnrollment  -->     6
        #     Key: Status             -->     O
        #     Key: StartDate          -->     2019-01-22Z
        #     Key: EndDate            -->     2019-05-20Z
        #     Key: Instructor1        -->     Name
        #     Key: Term               -->     2019S

        # Dictionary: meeting_dict: count =   0
        #     Key: Day                -->     T
        #     Key: StartTime          -->     4:00:00Z
        #     Key: EndTime            -->     5:50:00Z
        #     Key: Site               -->     Castle Point
        #     Key: Building           -->     B
        #     Key: Room               -->     430
        #     Key: Activity           -->     RCT

        # Dictionary: requirement_dict: count = 0
        #     Key: Control            -->     RQ
        #     Key: Argument           -->
        #     Key: Value1             -->     PEP 111
        #     Key: Operator           -->
        #     Key: Value2             -->

        dictionaries = self.get_dictionaries()
        self.main_attrib_dict = dictionaries[0]
        self.meeting_dict_list = dictionaries[1]
        self.requirement_dict_list = dictionaries[2]

        self.section = self.get_section()
        self.call_number = self.get_call_number()
        self.activity = self.get_activity()
        self.room = self.get_room()
        self.min_credit = self.get_min_credit()
        self.max_credit = self.get_max_credit()

        self.time_dict = self.get_time_dict()

    def get_dictionaries(self):
        main_attrib_dict = {}
        meeting_dict_list = []
        requirement_dict_list = []
        for element in self.child_obj.iter():
            if element.tag == "Course":
                main_attrib_dict = Functions.attrib_list_to_dict(element.attrib)
            elif element.tag == "Meeting":
                meeting_dict = Functions.attrib_list_to_dict(element.attrib)
                meeting_dict_list.append(meeting_dict)
            elif element.tag == "Requirement":
                requirement_dict = Functions.attrib_list_to_dict(element.attrib)
                requirement_dict_list.append(requirement_dict)
            else:
                print("Different Element Tag: " + element.tag)
        return main_attrib_dict, meeting_dict_list, requirement_dict_list

    def get_section(self):
        return self.main_attrib_dict["Section"]

    def get_call_number(self):
        return self.main_attrib_dict["CallNumber"]

    def get_subject_name(self):
        return Functions.string_to_alternating_letter_to_num(self.section)[0]

    def get_course_name(self):
        return ''.join(Functions.string_to_alternating_letter_to_num(self.section)[0:2])

    def get_activity(self):
        for meeting_dict in self.meeting_dict_list:
            if "Activity" in meeting_dict:
                return meeting_dict["Activity"]
        return None

    def get_room(self):
        for meeting_dict in self.meeting_dict_list:
            if "Room" in meeting_dict:
                return meeting_dict["Room"]
        return None

    def get_min_credit(self):
        if "MinCredit" in self.main_attrib_dict:
            return self.main_attrib_dict["MinCredit"]
        return None

    def get_max_credit(self):
        if "MaxCredit" in self.main_attrib_dict:
            return self.main_attrib_dict["MaxCredit"]
        return None

    def get_start_time(self, start_time_key):
        for meeting_dict in self.meeting_dict_list:
            if start_time_key in meeting_dict:
                return meeting_dict[start_time_key]
        return None

    def get_end_time(self, end_time_key):
        for meeting_dict in self.meeting_dict_list:
            if end_time_key in meeting_dict:
                return meeting_dict[end_time_key]
        return None

    def format_times(self, start_time_key, end_time_key):
        start_time = self.get_start_time(start_time_key)
        end_time = self.get_end_time(end_time_key)

        if start_time is not None or end_time is not None:
            start = [int(x) for x in start_time.split(":")[:2]]
            end = [int(x) for x in end_time.split(":")[:2]]
            if start[0] < Constants.minimum_section_start:
                start_time = str(start[0] + 12) + ":" + (2-len(str(start[1]))) * "0" + str(start[1])
                end_time = str(end[0] + 12) + ":" + (2-len(str(end[1]))) * "0" + str(end[1])
            else:
                start_time = (2 - len(str(start[0]))) * "0" + str(start[0]) + ":" + (
                            2 - len(str(start[1]))) * "0" + str(start[1])
                end_time = (2-len(str(end[0]))) * "0" + str(end[0]) + ":" + (2-len(str(end[1]))) * "0" + str(end[1])
            start_time = datetime.time(hour=int(start_time.split(":")[0]), minute=int(start_time.split(":")[1]))
            end_time = datetime.time(hour=int(end_time.split(":")[0]), minute=int(end_time.split(":")[1]))

        return [start_time, end_time]

    def get_time_dict(self):

        time_dict = {}

        day_key = "Day"
        start_time_key = "StartTime"
        end_time_key = "EndTime"

        for meeting_dict in self.meeting_dict_list:
            if day_key in meeting_dict:
                if start_time_key in meeting_dict and end_time_key in meeting_dict:
                    for letter in meeting_dict[day_key]:

                        time_dict[letter] = self.format_times(start_time_key, end_time_key)

        return time_dict

    def to_string(self, key_length=10, value_length=20):
        ret_str = Functions.dict_to_string(self.main_attrib_dict, "main_attrib_dict", key_length=key_length,
                                           value_length=value_length) + "\n"
        for i, meeting_dict in enumerate(self.meeting_dict_list):
            ret_str += Functions.dict_to_string(meeting_dict, "meeting_dict: count = " + str(i), key_length=key_length,
                                                value_length=value_length) + "\n"
        for i, requirement_dict in enumerate(self.requirement_dict_list):
            if i != 0:
                ret_str += "\n"
            ret_str += Functions.dict_to_string(requirement_dict, "requirement_dict: count = " + str(i),
                                                key_length=key_length, value_length=value_length)
        return "Section: " + self.section + "\n" + Functions.tab_after_new_lines(ret_str)


def is_section_list_valid(section_list):
    # returns True if section_list has no conflicts

    for i, section in enumerate(section_list):
        check_section_list = section_list[:i] + section_list[i + 1:]
        for day_key in section.time_dict:
            for check_section in check_section_list:
                if day_key in check_section.time_dict:
                    if Functions.has_overlap(start1=section.time_dict[day_key][0],
                                             end1=section.time_dict[day_key][1],
                                             start2=check_section.time_dict[day_key][0],
                                             end2=check_section.time_dict[day_key][1]):
                        return False
    return True


def iter_list_to_section_list(iter_list, section_list_list):
    new_section_list = []
    for i, section_list in enumerate(section_list_list):
        new_section_list.append(section_list[iter_list[i]])
    return new_section_list
