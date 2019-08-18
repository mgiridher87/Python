import random
a=random.sample(range(1,50),20)
b=random.sample(range(10,70),15)
print(a)
print(b)
c=[]
for i in a:
    if i in b:
        c.append(i)
print (list(set(c)))
