from Stevens import Stevens

from General import Functions


def main():

    stevens = Stevens.Stevens()

    # for subject in stevens.term.subject_list:
    #     for course in subject.course_list:
    #         for section in course.section_list:
    #             # print(section.__str__(print_section_dicts=True))
    #             print(section.activity, section.section)

    activity_list = []
    for subject in stevens.term.subject_list:
        for course in subject.course_list:
            print(Functions.dict_to_string(course.activity_dict))
            print("---------------------------")
            # for section in course.section_list:
            #     print(type(section.activity), section.activity)
            #     if section.activity not in activity_list:
            #         activity_list.append(section.activity)
            #         print("{} ----------------------".format(section.activity))
            #         # print(section.__str__(print_section_dicts=True))

    for activity in activity_list:
        print(type(activity), activity)


main()
