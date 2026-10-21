# #1
# salary = int(input("Enter your salary: "))

# if salary < 30000:
#     tax = (salary*5)/100
#     print(tax)
# elif salary < 70000:
#     tax = (salary*15)/100
#     print(tax)
# else:
#     tax= (salary*25)/100
#     print(tax)


# #2
# def evenNoBetweenThem(a, b):
    
#     for i in range(a, b+1):
#         if(i%2 == 0):
#             print(i)

# evenNoBetweenThem(5, 10)

# #3

# n = int(input("Enter the digit"))

# while(n>0):
#     k=n%10
#     print(k)
#     n =int(n/10)

# #4
# n = int(input("Enter the digit"))
# count=0
# while(n>0):
#     n =int(n/=10)
#     count+=1

# print(count)

# #5
# def sumOfDigit(n):
#     sum =0
#     while(n>0):
#         k = n%10
#         print(k)
#         sum+=k
#         n= int(n/10)
#     return sum

# print(sumOfDigit(312))

## 6

# for i in range(1, 101):
#     if(i%3==0 and i%5==0):
#         print(i)

# # optimised approach

# for i in range(3, 101, 3):
#     if(i%5==0):
#         print(i)


# #7


# while True:
#     n = input("Enter a number or Quit: ")
#     if n == "Quit":
#         break
#     k= int(n)
#     if k>0:
#         print("Number is positive")
#     elif k==0:
#         print("Number is zero")
#     else:
#         print("Number is negitive")
    
# #8
# def calculator(a, b, operation):
#     if(operation == '+'):
#         return a+b
#     elif(operation == '-'):
#         return a-b
#     elif(operation == '*'):
#         return a*b
#     elif(operation == "/"):
#         return a/b
#     else:
#         error="operation not supported"
#         return error

# print(calculator(3,4,'/'))


# #9
# def is_prime(n):
#     isPrime=True
#     for i in range(2, int(n/2+1)):
#         if n%i==0:
#             isPrime=False
#     return isPrime

# print(is_prime(21))

#10

#guessing Game

num = 75
n =0

while n!=num:
    n = int(input("Enter the number: "))
    if(num==n):
        print("Correct!")
    elif n>num:
        print("Too high")
    else:
        print("Too low")