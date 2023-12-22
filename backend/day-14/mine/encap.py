"""
Author: Willie M. Bonavente
Date: 12/3/2023
Encapsulation

"""

from datetime import datetime

class Employee:
    
    def __init__(self, name, birth_yr, birth_mo, birth_day):
        self.name = name
        self.birth_yr = birth_yr
        self.birth_mo = birth_mo
        self._birth_date = self._to_unix_time(birth_yr, birth_mo, birth_day)
          
    def _to_unix_time(self, yr, mo, d):
        return datetime(yr, mo, d).timestamp()

    def birthdate(self):
        return datetime.fromtimestamp(self._birth_date).strftime("%B %d, %Y")

employee1 = Employee("John", 1999, 10, 20) 
print(employee1.birthdate())       
        