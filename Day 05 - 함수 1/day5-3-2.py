def is_prime_number (x: int):
    #cnt = 0
    if x <= 1:
        output = "x>1"
        return output
    else:
        for i in range(2, x):
            if x % i == 0:
                #cnt = cnt + 1
                #print(cnt, i)
                output = False
                break
            else:
                output = True
        return output


x = 14
output = is_prime_number(x)
print(output)
