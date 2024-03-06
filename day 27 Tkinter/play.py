def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add(3,3,2,2,2,2,3,4,2,4,2,43,2)

def calculate(n, **kwargs ):
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


calculate(2, add = 3, mul = 4)