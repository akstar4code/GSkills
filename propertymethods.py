
class Student:
    def __init__(self, name, std, roll):
        self.name = name
        self.std = std
        self.roll = roll

    def mail_id(self):
        x = self.name.split()
        return x[0].lower() + '_' + x[1].lower() + '@student.co.in'
    @property
    def name_div(self):
        x = self.name.split()
        return 'First Name: {}\nLast Name: {}'.format(x[0],x[1])


stud1 = Student('Ashok Kumar', 'B.Tech', 'CSE2017/085')
print(stud1.name_div)