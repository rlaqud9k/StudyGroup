one = 1
two = 2
three = one + two

list1 = [1, 2]
list2 =[]
while three < 4000000:
    three = one + two
    list1.append(three)
    one = two
    two = three

for i in list1:
    if i%2 == 0:
        list2.append(i)
print(list1)
print(list2)
print(sum(list2))