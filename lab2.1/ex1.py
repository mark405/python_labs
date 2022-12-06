import json
from datetime import datetime


class RegularTicket:
    __tickets = []

    def __init__(self, event):
        self._price = event.price
        self.__event = event
        self.__tickets.append(self)
        self.__id = self.__tickets.index(self)

    @property
    def event(self):
        return self.__event

    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f"{self.__class__.__name__} #{self.id} for " \
               f"{self.event} " \
               f"Price {self.price}"

    @classmethod
    def construct_ticket_by_number(cls, number):
        for i in cls.__tickets:
            if number == i.id:
                return i

        raise ValueError

    @classmethod
    def get_all_tickets(cls):
        return cls.__tickets


class AdvancedTicket(RegularTicket):
    def __init__(self, event, advance_coef):
        super().__init__(event)
        self._price = self._price - self._price * advance_coef


class LateTicket(RegularTicket):
    def __init__(self, event, late_coef):
        super().__init__(event)
        self._price = self._price + self._price * late_coef


class StudentTicket(RegularTicket):
    def __init__(self, event, student_coef):
        super().__init__(event)
        self._price = self._price - self._price * student_coef


class Event:
    def __init__(self, price, name, date):
        if (date.date() - datetime.today().date()).days <= 0:
            raise ValueError(f"Event {name} has been passed")
        elif price < 0:
            raise ValueError(f"Price can not be less than zero - {price}")
        elif not name:
            raise ValueError(f"Name can not be null - {name}")

        self.__price = price
        self.__name = name
        self.__date = date

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    def __str__(self):
        return f"{self.__name} {self.__date.strftime('%d/%m/%Y')}"


def buy_ticket(event, student=False, left_range=10, right_range=60):
    current_date = datetime.today().date()
    event_date = event.date.date()

    date_difference = (event_date - current_date).days

    if student:
        return StudentTicket(event, 0.5)
    elif 0 < date_difference <= left_range:
        return LateTicket(event, 0.1)
    elif left_range < date_difference <= right_range:
        return RegularTicket(event)
    elif date_difference > right_range:
        return AdvancedTicket(event, 0.6)


def write_data():
    all_tickets = RegularTicket.get_all_tickets()
    with open("tickets.json", "a") as outfile:
        outfile.write("[")
        for i in all_tickets:
            ticket_dictionary = {
                "id": i.id,
                "name": i.__class__.__name__,
                "event": i.event.name,
                "price": i.price,
                "date": i.event.date.strftime('%d/%m/%Y')
            }
            json_object = json.dumps(ticket_dictionary, indent=5)
            outfile.write(json_object + ",\n")
        outfile.write("]")


try:

    ev = Event(400, "Gig", datetime.strptime("21/11/2022", "%d/%m/%Y"))
    ev1 = Event(1000, "Big Gig", datetime.strptime("25/12/2022", "%d/%m/%Y"))

    ticket1 = buy_ticket(ev)
    ticket2 = buy_ticket(ev1, True)
    ticket3 = buy_ticket(ev1)
    ticket4 = buy_ticket(ev1)

    print(ticket1)
    print(ticket2)

    write_data()


except ValueError as verr:
    print(verr.__str__())
