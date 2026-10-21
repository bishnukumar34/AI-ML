def hello():
    print("hello")


def helloWorld(var):
    print(var)

hello()
helloWorld("print")

#average

def average(a, b, c):
    avg = (a+b+c)/3
    return avg

print(average(2, 3, 4))



#Lambda Function


sum = lambda a, b, c: a+b+c

print(sum(3, 4, 5))

def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact*=i
    return fact

print(factorial(5))