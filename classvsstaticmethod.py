
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

emp1 = Employee('Ashok','Kumar',50000)
emp2 = Employee('Prem','Kumar',60000)

print('No of employee',Employee.no_of_emp)
