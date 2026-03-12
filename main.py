n = int(input("enter a number : "))

temp = n

rev = 0

while n > 0:
    digit =  n % 10
    rev = rev*10+n%10
    n= n//10

if temp == rev:
    print("number is palindrom  ")
else:
    print("number is not palindrom  ")