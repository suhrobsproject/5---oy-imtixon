# 1 - masala

n = int(input('n = '))

a = 0 
b = 1

d = []

for i in range(n):
    d.append(a)
    a , b = b, a
    a = b + a
    
generator = (i for i in d)

for i in generator:
    print(i)
