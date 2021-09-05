def is_prime_number (x: int):
    #print(x)
    if x <= 1:
        output = False
    elif x == 2:
        output = True
    else:
        #print(x)
        for i in range(2, x):
            #print(x)
            if x % i == 0:
                output = False
                break
            else:
                output = True
    return output


prime_numbers = []
for i in range(2, 101):
    if is_prime_number(i):
        prime_numbers.append(i)
print(prime_numbers)

#print(list(range(2,2)))