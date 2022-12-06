from abc import ABC, abstractmethod


class ITeacher(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Teacher(ITeacher):

    def __init__(self, name, age):
        if name and isinstance(name, str):
            self.__name = name
        else:
            raise ValueError

        if age and isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    def get_name(self):
        return self.__name

    def __str__(self):
        result = f"Teacher {self.__name} is {self.__age} years old"
        return result


class ICourse(ABC):

    def __init__(self, name, topics, teachers):
        if name and isinstance(name, str):
            self._name = name
        else:
            raise ValueError

        self._topics = []
        self.add_topic(topics)

        self._teachers = []
        self.add_teacher(teachers)

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    def teachers(self):
        return self._teachers

    def add_teacher(self, teachers):
        if teachers:
            if isinstance(teachers, Teacher):
                self._teachers.append(teachers)
            elif isinstance(teachers, list):
                for teacher in teachers:
                    self._teachers.append(teacher)
            else:
                raise ValueError
        else:
            raise ValueError

    def add_topic(self, topics):
        if topics:
            if isinstance(topics, str):
                self._topics.append(topics)
            elif isinstance(topics, list):
                for topic in topics:
                    self._topics.append(topic)
            else:
                raise ValueError
        else:
            raise ValueError


class ILocalCourse(ICourse, ABC):

    @abstractmethod
    def lab(self):
        pass


class IOffsiteCourse(ICourse, ABC):
    @abstractmethod
    def town(self):
        pass


class LocalCourse(ILocalCourse):

    def __init__(self, name, lab, topics, teachers):

        super().__init__(name, topics, teachers)

        if lab and isinstance(lab, str):
            self.__lab = lab
        else:
            raise ValueError

    def lab(self):
        return self.__lab

    def get_name(self):
        return f"Local course named {self._name}"

    def __str__(self):
        result = f"{self.get_name()} in {self.__lab} for "
        for topic in self._topics:
            result += topic + " "

        result += "("

        for teacher in self._teachers:
            result += str(teacher) + " "

        result += ")"

        return result


class OffsiteCourse(IOffsiteCourse):

    def __init__(self, name, town, topics, teachers):

        super().__init__(name, topics, teachers)

        if town and isinstance(town, str):
            self.__town = town
        else:
            raise ValueError

    def town(self):
        return self.__town

    def get_name(self):
        return f"Local course named {self._name}"

    def __str__(self):
        result = f"{self.get_name()} in {self.__town} for "
        for topic in self._topics:
            result += topic + " "

        result += "("

        for teacher in self._teachers:
            result += str(teacher) + " "

        result += ")"

        return result


class ICourseFactory(ABC):
    @abstractmethod
    def create_teacher(self, name, age):
        pass

    @abstractmethod
    def create_local_course(self, name, lab, topics, teacher):
        pass

    @abstractmethod
    def create_offsite_course(self, name, town, topics, teacher):
        pass


class CourseFactory(ICourseFactory):

    def create_teacher(self, name, age):
        return Teacher(name, age)

    def create_local_course(self, name, lab, topics, teachers):
        return LocalCourse(name, lab, topics, teachers)

    def create_offsite_course(self, name, town, topics, teachers):
        return OffsiteCourse(name, town, topics, teachers)


try:
    course_factory = CourseFactory()

    teacher1 = course_factory.create_teacher("Mark", 34)
    teacher2 = course_factory.create_teacher("Alina", 30)
    teacher3 = course_factory.create_teacher("Roma", 40)

    local_course1 = course_factory.create_local_course("FirstLocalCourse", "Lab1", "programming", teacher1)
    offsite_course1 = course_factory.create_offsite_course("FirstOffsiteCourse", "Kyiv", ["english", "spanish"], [teacher1, teacher3])
    offsite_course2 = course_factory.create_offsite_course("SecondOffsiteCourse", "Odessa", ["astronomy", "physics"], teacher2)

    print(teacher1)
    print(teacher2)
    print(teacher3)

    print(local_course1)
    print(offsite_course1)
    print(offsite_course2)

except ValueError:
    print("ValueError")
