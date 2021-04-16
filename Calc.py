import math


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def mod(a, b):
    return a % b


def squa(a, b):
    return a ** b


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)


def ceil(a):
    return math.ceil(a)


def floor(a):
    return math.floor(a)


def fact():
    a = int(input("Enter a value :"))
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    print(fact)


def exp(a):
    return math.exp(a)


def log(a):
    return math.log(a)


def log1(a):
    return math.log2(a)


def rad(a):
    return a * math.pi/180


def deg(a):
    return a * 180/math.pi


def interest(p, r, t):
    return p*r*t/100


def markspercent(Total_marks_obtained, Sum_of_total):
    return Total_marks_obtained / Sum_of_total * 100


def fahrenheit(degree):
    return int(round(9*degree) / (5 + 32))


def celsius(degree):
    return int(round(degree - 32) * (5 / 9))

