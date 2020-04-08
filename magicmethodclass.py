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
#    def __repr__(self):
#        return 'Employee Details:- {} -- {} -- {}'.format(self.fullname(),self.email,self.pay)
    def __str__(self):
        return 'Employee Drtails:- {} -- {} -- {}'.format(self.fullname(),self.email,self.pay)
    def __add__(self,other):   #magic or dunder method
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
emp1 = Employee('Ashok','Kumar',50000)
emp2 = Employee('Prem','Kumar',60000)
print(emp1)
print(emp2)
print('Total Name Length : ',len(emp1))
print('Total Amount :',emp1+emp2)