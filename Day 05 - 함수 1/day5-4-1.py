def is_prime_number (x: int):
    lst = []
    # x = 1일 경우(베이직 케이스)를 정해주기

    for i in range(2, x):
        if x % i == 0:
            lst.append(i)
    if len(lst) == 0:
        output = True
    else:
        output = False
    return output


prime_numbers = []
for i in range(2, 101):
    if is_prime_number(i):   #맞냐아니냐 변수: is로 시작하는 경우 많음
        prime_numbers.append(i)
print(prime_numbers)