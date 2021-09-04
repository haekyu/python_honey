def swap(lst, n, m): #리스트, 딕셔너리 같은 큰 애들은 shallow copy
                     # m, n 같은 숫자, 문자, boolean 같은 애들은 딥카피
    fn = lst[n]
    fm = lst[m]
    lst[n] = fm
    lst[m] = fn
    m = -1
    n = -1
i = 3
j = 0


lst = [0, 1, 2, 3, 4]
swap(lst, i, j)
print(lst)
print(i, j)