# n = int(input("enter a number : "))

# if (n<=999 and n>99):
#     fname = (n//100)
#     lname = (n%10)

#     if(fname == lname):
#         print("number is palindrom ")
#     else:

#         print("number is not palindrom ")
# else:
#     print("enter a three digit number ")


# n = int(input("enter a number : "))



# count = 0

# while n > 0:
#     n = n//10

#     count +=1

# print(count)

# string = input("enter a string : ")

# if string == string[::-1]:
#     print(f"string is palindrom : {string}")


# else:
#     print(f"string is not palindrom : {string}")



n = int(input("enter a number : "))

original = n

rev = 0

while n > 0:
    digit = n % 10
    rev=rev*10+n%10
    n=n//10

if original == rev:
    print(f"number is palindrom : {original}")
else:
    print("number is not palindrom : ")