sss = 'Love is an open door! Love is an open door! Life can be so much more!'
lst = sss.split(' ')
#print(lst)
#print(len(lst)) #16

idx = 0
num = 0

while idx < len(lst):
    if lst[idx] == 'an':
        num = num + 1
    idx = idx + 1
print(num)