a = float(input("Enter any number"))
b = float(input("Enter any number"))
c = float(input("Enter any number"))

if b*b<4*a*c:
    print("No real roots")
elif b*b==4*a*c:
    print("Two same real roots")
else:
    print("Two distinct real roots")

    root1 = (-b+(b*b-4*a*c))/2
    root2 = (-b-(b*b-4*a*c))/2
    print("The roots of the equation is" , root1 , root2)