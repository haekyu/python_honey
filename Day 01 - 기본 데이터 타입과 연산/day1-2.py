x = False
y = False
z = (x and not y) or (not x and y)
w = (x or y) and not (x and y)
q = (x or y) and (not x or not y)
print(q)