from Stevens import Stevens


def main():

    stevens = Stevens.Stevens()

    for subject in stevens.term.subject_list:
        for course in subject.course_list:
            for section in course.section_list:
                print(section.__str__(print_section_dicts=True))


main()
