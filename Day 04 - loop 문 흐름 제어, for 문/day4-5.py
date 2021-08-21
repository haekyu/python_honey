lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]
max = 2
num = 0

for e in lst:
    if e > max:
        max = e

for i in lst:
    if max == i:
        num = num + 1
print(num)
