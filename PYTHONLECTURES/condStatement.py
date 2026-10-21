# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# color=input("Enter the color:")

# if color == "red":
#     print("stop")
# elif color == "yellow":
#     print("wait")
# elif color == "green":
#     print("go")
# else:
#     print("invalid color")


# age = int(input("Enter your age:"))
# if (age < 13):
#     print("You are a child.")
# elif (age <= 20):
#     print("You are a teenager.")
# else:
#     print("You are an adult.")

# username = input("Enter username:")
# password = input("Enter password:")


# if(username == "admin" and password == "admin123"):
#     print("Login successful")
# elif(username != "admin"):
#     print("Invalid username")
# else:
#     print("wrong password")

# n = int(input("Enter a number:"))
# if(n%5==0):
#     print("The number is multiple of 5.")
# else:
#     print("The number is not a multiple of 5.")

# n = int(input("Enter a number:"))
# if(n%2==0):
#     print("The number is even.")    
# else:
#     print("The number is odd.")



# #Nesting 

# username = input("Enter username:")
# password = input("Enter password:")

# if (username == "admin" and password == "admin123"):
#     print("Login successful")
# else:
#     if (username != "admin"):
#         print("Invalid username")
#     else:
#         print("wrong password")


# #Match case
# color =input("Enter the color:")

# match color:
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Wait")
#     case "Red": 
#         print("Stop")
#     case _:
#         print("Invalid color")

# #Loops in Python

# #while loop
# i =1
# while i<=5:
#     print("Hello", i)
#     i+=1

# i = 5

# while i>=1:
#     print("Hello", i)
#     i-=1



# n = int(input("Enter a number:"))
# i =1
# while i<=10:
#     print(n, "x", i, "=", n*i)
#     i+=1


# n = int(input("Enter a number:"))
# i =1
# while i<=10:
#     if n*i%6==0:
#         break
#     print(n, "x", i, "=", n*i)
#     i+=1




string = "hello"
#in => membership operator can be used in for loop and if else statements
for var in string:
    print(var)
    
if 'o' in string:
    print("o is present in the string")



i = 1
for i in range(5): #0 to 4
    print("Hello", i)



#counting the number of 'i' in a string
word = "artificial intelligence"

count =0
for var in word:
    if var == 'i':
        count+=1

print("The number of 'i' in the string is:", count)

#print vowel count in a string
count =0
word = "artificial intelligence"
for var in word:
    if var in 'aeiou':
        count+=1

print("The number of vowels in the string is:", count)


for i in range(1, 11, 2):
    print(i)


#sum of first n natural numbers

n = int(input("Enter the number: "))
sum = 0

for i in range(1, n+1):
    sum+=i
print(sum)


