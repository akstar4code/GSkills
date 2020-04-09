import pyqrcode
ICard = '''
    name = Ashok Kumar
    Email = ashok.oct20@gmail.com
    DOB = 14-12-1999
'''
my_id = pyqrcode.create(ICard)
my_id.svg('my_idcard.svg',scale=8)