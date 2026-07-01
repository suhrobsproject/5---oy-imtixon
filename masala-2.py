# 2 - masala

# n = int(input('n = '))
n = 10
a = [i for i in range(n)]
print(a)


def deco(func):
    def wrapper(a):
        c = func(a)
        b = []
        for i in c:
            b.append(sum(c[:i+1]))
        return b
    return wrapper

@deco
def massiv(a):
    return a

print(massiv(a))
