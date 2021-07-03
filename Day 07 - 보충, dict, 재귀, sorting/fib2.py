memo = {}

def f(n):

    # Base case
    if n <= 1:
        return 1

    # Logic: f(n) = f(n-1) + f(n-2)
    
    # f(n-1)
    # f_n_1 = reuse를 하든, 새로 계산을 때리든 구해요
    if n - 1 in memo:
        f_n_1 = memo[n - 1]
    else:
        f_n_1 = f(n - 1)

    # f(n-2)
    # f_n_2 = reuse를 하든, 새로 계산을 때리든 구해요
    if n - 2 in memo:
        f_n_2 = memo[n - 2]
    else:
        f_n_2 = f(n - 2)

    # 메모 (n)
    f_n = f_n_1 + f_n_2
    memo[n] = f_n

    return f_n


# memo = {}
f_100 = f(100)
print(f_100)
# print(memo)
