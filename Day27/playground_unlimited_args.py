# def add(n1,n2):
#     return  n1 + n2

## To pass Unlimited Args.


def add(*args):
    sum = 0
    for n in args:
        #print(n,end=" ")
        sum += n
    return sum


#print(add (1,2,3,4,5,6,7,8,9))
# print(total)

# Keyword Arguments  **kwargs
# def calculator(**kwargs):
#     #print(type(kwargs))
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#
# calculator(add=3,multiply=5)

def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    print(n)

calculator(2,add=3,multiply=5)

class Car:
    def __init__(self, **kw):
        #self.make = kw["make"]   or
        self.make = kw.get("make")   ## If we use get then it will retun None and will not throw error
        self.model = kw["model"]

#mycar = Car(make="Nissan",model=2020)
car = Car(model=2022)
print(car.model)


def test(*args):
    print(args)


test(1, 2, 3, 5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)




