t1 = (23,32,43,34,)
print("\nAll the even numbers in t1 are: ")
test = []
for i in t1:
    if i % 2 == 0:
        test.append(i)
test_tup = tuple(test)
print(test_tup)
