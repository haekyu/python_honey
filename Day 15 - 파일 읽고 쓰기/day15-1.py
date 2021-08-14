import numpy as np
f = open("C:/Users/HONEY/PycharmProjects/hk study/sample_mat.txt", 'r')
lines = f.readlines()
f.close()

for i, line in enumerate(lines):
    lines[i] = line.rstrip('\n')
for i, line in enumerate(lines):
    lines[i] = line.replace(' ', ', ')

print(lines)
type(lines)

lines_lst = []
for i in range(len(lines)):
    new_line = lines[i].split(', ')
    for j in new_line:
        j = int(j)
    print(new_line)
    lines_lst.append(new_line)
print(lines_lst)

# lst = []
# for i in lines:
#     lst.append(lines[i])
#
# print(lst)



