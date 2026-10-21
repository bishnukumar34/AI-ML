# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# print("Hello", name, "you are", age, "years old!")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = float(input("Enter third number: "))
# average = (a+b+c)/3
# print(average)

# a = input("Enter a number: ")
# b = int(a)
# print(b, type(b))
# b = float(a)
# print(b, type(b))
# a= str(b)
# print(a, type(a))

# x = 10 + 3*2**2
# print(x)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: ")) 
# temp = a
# a=b
# b=temp
# print("After swapping:")
# print("a =", a)
# print("b =", b)


# CelsiusTemp = float(input("Enter temperature in Celsius: "))
# FahrenheitTemp = (CelsiusTemp * 9/5) + 32
# print("Temperature in Fahrenheit:", FahrenheitTemp)

# r = float(input("Enter radius of the circle: "))
# area = 3.14 * r**2
# print("Area of the circle:", area)

# Principal = float(input("Enter principal amount: "))
# Rate = float(input("Enter rate of interest: "))
# Time = float(input("Enter time in years: "))
# SimpleInterest = (Principal * Rate * Time) / 100
# print("Simple Interest:", SimpleInterest)

a = float(input("Enter a number: "))
b = int(a)
# c = a%1
c = a-b
c = round(c, 2)
print("Integer part:", b)
print("Fractional part:", c)
