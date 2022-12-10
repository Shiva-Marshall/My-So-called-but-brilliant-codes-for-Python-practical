a = input("Enter any number: ")
a = int(a)
for i in (2,a-1):
    if a%i == 0:
        print("It's not a prime number")
    elif a%i != 0:
       print("It's not a prime number")
