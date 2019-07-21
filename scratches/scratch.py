three_array = []
five_array = []
all_array = []
for i in range(1000):
    if i%3 == 0 and i%5 ==0:
        all_array.append(i)
    if i%3 == 0:
        three_array.append(i)
    if i%5 == 0:
        five_array.append(i)


print(three_array)
print(five_array)
print(all_array)

tr = sum(three_array)
fr = sum(five_array)
ar = sum(all_array)
print(tr + fr - ar)
