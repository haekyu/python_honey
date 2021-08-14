# 어떤 자연수 n이 주어져 있을 때, n의 약수들을 모은 리스트를 리턴하는 함수를 만들어 보세요.
# ex) n = 20 이면 [1, 2, 4, 5, 10, 20] 리턴.
#     이 때, List comprehension 을 사용해서 만들어보세요.

# def devisor(n):
#     lst = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             lst.append(i)
#     return lst
#
# output = devisor(20)
# print(output)

def devisor(n):
    lst = [i for i in range(1, n+1) if n % i == 0]
    return lst

output2 = devisor(20)
print(output2)