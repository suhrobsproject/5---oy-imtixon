# 4 - masala


matn = 'Bugun imtixon kuni hamma kelishi shart'

a = matn.split()
# gen = (i for i in a)

def generator(a):
    for i in a:
        yield i

for i in generator(a):
    print(i)
