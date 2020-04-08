import datetime
class Employee:
    no_of_emp = 0
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.no_of_emp += 1
        self.email = first.lower() + '_' + last.lower() + '@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def raise_amount(self):
        self.pay = int(self.pay *self.raise_amt)
    @classmethod
    def raise_in_amt(cls,amount):
        cls.raise_amt = amount
    @classmethod
    def from_str(cls,emp_str):
        first,last,pay = emp_str.split()
        return cls(first,last,int(pay))
    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Ashok','Kumar',50000)
emp2 = Employee('Prem','Kumar',60000)

Employee.raise_in_amt(1.05)
emp3 = Employee.from_str(input())
print(emp3.__dict__)
print('No of employee',Employee.no_of_emp)
print('Raise Amount',Employee.raise_amt)
print('Raise Amount',emp1.raise_amt)
print('Raise Amount',emp2.raise_amt)

mydate = datetime.date(2020,3,22)
print(Employee.is_workingday(mydate))
