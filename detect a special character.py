Name = input("Enter your name pleae: ")
import re
if(bool(re.match('^[a-zA-Z0-9]*$',Name))==True):
    print("It does't contain any special character that you might be checking to see but it's not really up here")
else:
    print("Yeah ,jig is up, It contains the so-called Special character")