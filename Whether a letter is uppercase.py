a = input("enter anything:: ")
x = a.isalpha()
y= a.isupper()
if x==True:
    print("It's an alphabhet")
else:
    print("It's an number or special character")
if y==True:
    print(a, "is an upperclass letter")
elif y==False:
    print(a, "is a lower class letter") 