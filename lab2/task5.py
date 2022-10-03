class Group(object):
    def __init__(self, student_list):
        self.__student_list = []
        if len(student_list) <= 20:
            status = True
            for i in range(0, len(student_list)):
                for j in range(i, len(student_list) - 1):
                    if student_list[i].get_name() == student_list[j + 1].get_name() \
                            and student_list[i].get_surname() == student_list[j + 1].get_surname():
                        status = False
                        break
            if status:
                self.__student_list = student_list
            else:
                print("Invalid sequence1")
        else:
            print("Invalid sequence2")

    def add_student(self, student):
        self.__student_list.append(student)

    def remove_student(self, student_name, student_surname):
        new_student_list = [student for student in self.__student_list if student.get_name != student_name or
                            student.get_surname != student_surname]
        self.__student_list = new_student_list

    def get_group(self):
        return self.__student_list


class Student(object):
    def __init__(self, name, surname, number, math_mark, it_mark, lang_mark):
        self.__name = name
        self.__surname = surname
        self.__number = number
        self.__math_mark = math_mark
        self.__it_mark = it_mark
        self.__lang_mark = lang_mark

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_number(self):
        return self.__number

    def get_average_mark(self):
        return (self.__math_mark + self.__it_mark + self.__lang_mark) / 3


student1 = Student("mark", "zavgod", 1, 4, 5, 5)
student2 = Student("mark1", "zavgod", 2, 3, 5, 1)
student3 = Student("vova", "alalal", 3, 4, 3, 5)
student4 = Student("misha", "dldldl", 4, 4, 4, 4)
student5 = Student("dima", "d,e", 5, 5, 5, 5)
student6 = Student("roma", "dele", 6, 4, 2, 3)
student7 = Student("aliba", "dodep", 7, 2, 4, 1)

list_of_students = [student1, student2, student3, student4, student5, student6, student7]

group1 = Group(list_of_students)

group1.get_group().sort(key=lambda student: student.get_average_mark())
group1.get_group().reverse()

if len(group1.get_group()) > 5:
    for k in range(0, 5):
        print(group1.get_group()[k].get_name(), group1.get_group()[k].get_surname(), group1.get_group()[k].get_number(),
              group1.get_group()[k].get_average_mark())
