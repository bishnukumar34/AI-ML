# print("Hello World!", "with Python!")
# print("Hello World! \nwith Python!")
name =  "Bishnu"
age = 15
print("My name is", name, "and I am", age+6, "years old.")
print(type(age))
#arithmetic operations
a = 10
b= 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) 

#relational operators
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#assignment operators
a += 5
print(a)
a += b
print(a)

#logical operators
var = True
print(not var)
print(not (5>8))
a=20
b =5
print(a>5 and b<2)
print(a>5 or b<2)

#type conversion

ans1 = 5 + 10.0
ans2 = int(5+10.0)
print(ans1)
print(ans2)
val = int("123")
print(val)

#input function
a=input("Enter a number: ")
print("You entered:", a)

#sum of two numbers
     #takes string input from user
a = input("Enter first number: ")# better to use int or float(input()) to convert input to integer directly
b = input("Enter second number: ")  
sum1 = a+b
sum2 = int(a)+int(b)
print(sum1)
print(sum2)

#average of two numbers
a = float(input("Enter first number: "))  
b = float(input("Enter second number: "))
average = (a+b)/2
print(average)


