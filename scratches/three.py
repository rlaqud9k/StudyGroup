def d(i):
    list = []
    inte = str(i)
    for q in inte:
        list.append(int(q))
    list.append(i)
    print(list)
    return sum(list)

llist = []
for i in range(1,50000):
    if d(i) < 5000:
        llist.append(d(i))
llist = set(llist)
print(llist)
lllist = []
for i in range(5000):
     if not llist.__contains__(i):
         lllist.append(i)

print(lllist)
print(sum(lllist))