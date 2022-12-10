t1 = (23,32,43,34,)
print("\nAll the even numbers in t1 are: ")
test = []
for i in t1:
    if i % 2 == 0:
        test.append(i)
test_tup = tuple(test)
print(test_tup)
# c)
t2 = (11, 13, 15)
conc = t1 + t2
print(type(conc))
print('The concatenation of t2 is: ' + str(conc))
