import random as r
name_list = ['Ashok','Prem','Mjay','Akash']
color_list = ['Red','Black','Blue','Green','Violet']
number_choice = list(range(0,10))
print(r.random())
print(r.uniform(1,10))
print(r.randint(0,6))
name = r.choice(name_list)
print('Hello',name)
colors = r.choices(color_list,weights=[20,20,5,5,5],k = 10)
print(colors)
print('Choices in Random ',number_choice)
sample_list = r.sample(number_choice,k=5)
r.shuffle(number_choice)
print('Shuffle in Random ',number_choice)
print('Sample in Random ',sample_list)
print(r.randrange(0,11,2))
