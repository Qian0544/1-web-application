import datetime
from dateutil.relativedelta import relativedelta
class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name 
        self.last_name = last_name 
        self.date_of_birth = date_of_birth
    def age(self):
        return relativedelta(datetime.date.today(), self.date_of_birth).years
author = Person("John", "Grisham", datetime.date(1995, 2, 8)) 
print(author.age())