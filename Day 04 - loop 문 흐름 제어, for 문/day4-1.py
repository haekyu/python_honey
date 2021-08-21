sss = 'Love is an open door! Love is an open door! Life can be so much more!'
lst = sss.split(' ')
#print(lst)

idx = 0
num = 0
"""
while idx < len(lst)-1:
    if lst[idx] == 'open':
        #print(idx)
        if lst[idx + 1][:4] == 'door':
            num = num + 1
    idx = idx + 1
print(num)
"""

while idx < len(lst)-1:
    if lst[idx] == 'open':
        #print(idx)
        if 'door' in lst[idx + 1]:
            num = num + 1
    idx = idx + 1
print(num)