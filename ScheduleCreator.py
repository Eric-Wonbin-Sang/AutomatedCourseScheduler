from General import MultiBaseNumber


def get_schedule_list(section_list_list):

    base_list = [len(section_list)for section_list in section_list_list]
    multi_base_number = MultiBaseNumber.MultiBaseNumber(base_list=base_list)

    print(multi_base_number)
