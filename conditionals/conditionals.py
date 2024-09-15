
#syntax

a = 3
if a > 0:
    print("A is a positive number")

b = 5
if b < 0:
    print("B is a negative number")
else:
    print("B is a positive number")


c= 0
if c > 0:
    print("C is a positive number")
elif c < 0:
    print("C is a negative number")
else:
    print("C is a zero")


d = 0
if d > 0:
    if d % 2 == 0:
        print('D is a positive and even integer')
    else:
        print('D is a positive number')
elif d == 0:
    print('D is zero')
else:
    print('D is a negative number')

e = 0
if e > 0 and e % 2 == 0:
        print('E is an even and positive integer')
elif e > 0 and e % 2 !=  0:
     print('E is a positive integer')
elif e == 0:
    print('E is zero')
else:
    print('E is negative')
