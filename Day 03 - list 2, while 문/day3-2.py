lst = [1, -2, 5, 4, -3]
sum_of_elements = 0
num_of_elements = 0

idx = 0
while idx < 5:
    sum_of_elements = sum_of_elements + lst[idx]
    idx = idx + 1
num_of_elements = idx

avg_of_elements = sum_of_elements / num_of_elements
print(avg_of_elements)