class Group(object):
    def __init__(self, student_list):
        if 0 < len(student_list) <= 20:
            if self.check_if_duplicate(student_list):
                raise NameError

            self.__student_list = student_list
        else:
            raise ValueError

    def get_list_of_fio(self, student_list):
        list_of_fio = []
        for i in student_list:
            list_of_fio.append([i.get_name(), i.get_surname()])

        return list_of_fio

    def check_if_duplicate(self, student_list):
        list_of_fio = self.get_list_of_fio(student_list)

        for i in list_of_fio:
            if list_of_fio.count([i[0], i[1]]) > 1:
                return True

        return False

    def add_student(self, student):
        if self.check_if_duplicate(self.__student_list + [student]):
            raise NameError

        self.__student_list.append(student)

    def remove_student(self, student):
        list_of_fio = self.get_list_of_fio(self.__student_list)

        index_of_student = list_of_fio.index([student.get_name(), student.get_surname()])

        self.__student_list.pop(index_of_student)

    def get_group(self):
        return self.__student_list

    def get_top_five(self):
        sorted_students = sorted(self.__student_list, key=lambda x: x.get_average_mark(), reverse=True)

        top_five_students = []
        for i in range(5):
            top_five_students.append(sorted_students[i])

        return top_five_students


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


student1 = Student("mark1", "zavgo", 1, 4, 5, 5)
student2 = Student("mark1", "zavgod", 2, 3, 5, 1)
student3 = Student("vova", "alalal", 3, 4, 3, 5)
student4 = Student("misha", "dldldl", 4, 4, 4, 4)
student5 = Student("dima", "d,e", 5, 5, 5, 5)
student6 = Student("roma", "dele", 6, 4, 2, 3)
student7 = Student("aliba", "dodep", 7, 2, 4, 1)
student8 = Student("alifba", "dodefp", 7, 2, 4, 1)

list_of_students = [student1, student2, student3, student4, student5, student6, student7]

try:
    group1 = Group(list_of_students)
    group1.remove_student(student7)
    top = group1.get_top_five()

    for i in top:
        print(f"{i.get_name()} | {i.get_surname()} | {i.get_number()} | {i.get_average_mark()}")
except NameError:
    print('NameError')
except ValueError:
    print("ValueError")
