from General import Functions, MultiBaseNumber


class Schedule:

    def __init__(self, section_list):

        self.section_list = section_list
        self.credit_sum = self.section_list_to_credit_count()
        # self.url = self.get_url(term.code)

    def section_list_to_credit_count(self):
        return sum([int(x.max_credit) for x in self.section_list])

    def get_url(self, term_key):
        return "http://sitscheduler.com/#" + term_key + "=" + ",".join([x.call_number for x in self.section_list])

    def __str__(self):
        return "{}, {}".format(len(self.section_list), [section.section for section in self.section_list])


def get_schedule_list(section_list_list):

    base_list = [len(section_list) for section_list in section_list_list]
    multi_base_number = MultiBaseNumber.MultiBaseNumber(base_list=base_list)

    schedule_list = []
    for i in range(Functions.multiply_list(multi_base_number.base_list)):
        new_section_list = []
        for choice_i, section_list in enumerate(section_list_list):
            new_section_list.append(section_list[multi_base_number.value_list[choice_i]])
        if is_valid_section_list(new_section_list):
            schedule_list.append(Schedule(section_list=new_section_list))
        multi_base_number.iterate()
    return schedule_list


def is_valid_section_list(section_list):

    def has_overlap(start1, end1, start2, end2):
        # startA is before stopB and stopA is after StartB
        return not (end1 < start2 or start1 > end2)

    for i, section in enumerate(section_list):
        remaining_section_list = section_list[:i] + section_list[i + 1:]
        for day_key in section.time_dict:
            for check_section in remaining_section_list:
                if day_key in check_section.time_dict:
                    if has_overlap(
                            start1=section.start_time, end1=section.end_time,
                            start2=check_section.start_time, end2=check_section.end_time):
                        return False
    return True
