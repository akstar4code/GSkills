import sqlite3
import classes as oc
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''create table employees(
             first text not null,
             last text,
             pay integer)''')
c.execute("insert into employees values('Prem','Kumar',50000)")
emp1 = oc.Employee('Ravi','Kumar',50000)
emp2 = oc.Employee('Chanchala','Kumari',60000)
c.execute("insert into employees values(?,?,?)",(emp1.first,emp1.last,emp1.pay))
c.execute("insert into employees values(:first,:last,:pay)",
          {'first':emp2.first,'last':emp2.last,'pay':emp2.pay})
c.execute("select * from employees where first='Chanchala'")
print(c.fetchall())
conn.commit()
conn.close()