class WeekDayError(Exception):
    pass
    

class Weeker:

    def __init__(self, day):
        self.days = 'Mon Tue Wed Thu Fri Sat Sun'.split()
        if day not in self.days:
            raise WeekDayError
        else:
            self._day = day

    def __str__(self):
       return self._day

    def add_days(self, n):

        current_day_index = self.days.index(self._day)
        new_day_index = (current_day_index + n) % len(self.days)

        new_day = self.days[new_day_index]
        self._day = new_day

    def subtract_days(self, n):

        current_day_index = self.days.index(self._day)
        new_day_index = (current_day_index - n) % len(self.days)

        new_day = self.days[new_day_index]
        self._day = new_day

if __name__ == "__main__":

    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")