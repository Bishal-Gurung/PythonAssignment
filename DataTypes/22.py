a = [1,2,3,4,1,3,5,7,8,4,5,2,1,7,8,2,3,4,9,4,6]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
