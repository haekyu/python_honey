#def f(x, y = 0):
    #return x + y

#print(f(y = 100))

print((lambda x: x**0.5)(64))

#dict
d = {'apple': 'red', 'banana': 'yellow', 'peach': 'pink'}
d['watermellon'] = 'green'
print(d)
d['watermellon'] = 'green_and_black'
print(d)
print(d['apple'])

#recursive fuction_1
def f(x) :
    if x <= 1:
        return 1
    else:
        return f(x-1) + f(x-2)
print(f(10))

#recursive fuction_2
def sum_1_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_1_to_n(n-1)
print(sum_1_to_n(10))

#recursive fuction_3
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(10))

