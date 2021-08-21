lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]
print(max(lst))

max = 2

for e in lst:
    if e > max:
        max = e
print(max)

print(max(lst))