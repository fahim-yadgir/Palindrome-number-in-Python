# n = int(input("enter a number : "))

# original = n

# rev = 0

# while n > 0:
#     digit = n % 10
#     rev=rev*10+rev%10
#     n=n//10


# if original == rev:
#     print("numebr is palindrom ")

# else:
#     print("numebr is palindrom ")

# for i in range(1,5):
#     print("*" * i)

# for i in range(3,0,-1):
#     print("*" * i)


string = input("enter a string : ")

new = ''

for i in string:
    new = i+new

print(new)


