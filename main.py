import random

print('hello world')
print(5+3)

a=[]
for i in range(10):
    a.append(random.randint(1, 10))
print(a, '\nMax:' , max(a), 'Max index:' , a.index(max(a)),)