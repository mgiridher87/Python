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

###Palindrome Check
import re
a="Dammit, I'm Mad!"
b=re.sub('[^a-zA-Z0-9]','',a)
print (b)
frnt=b[:].upper()
bk=b[::-1].upper()
print (frnt)
if frnt == bk:
    print ("{} is a palindrome".format(b))
else:
    print ("{} Its not a palindrome".format(b))
