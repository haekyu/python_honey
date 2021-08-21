sss = 'nLove is an open door! Love is an open door! Life can be so much more!a'
lst = list(sss)
#print(lst)

idx = 0
num = 0

while idx < len(lst)-1 :
    if lst[idx] == 'a':
        #print(idx)
        if lst[idx+1] == 'n':
            num = num + 1
    idx = idx + 1
print(num)

"""
while idx > -len(lst):
    print("---------")
    print(idx)
    if lst[idx] == 'n':
        if lst[idx-1] == 'a':
            num = num + 1
            print(num)
    idx = idx - 1
    print("End", idx)
print(num)
"""