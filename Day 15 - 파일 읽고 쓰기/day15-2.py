def bubble_sort(lst):
    for stage in range(len(lst)):
        for j in range(len(lst) - stage - 1):
            # if j == (len(lst) - stage - 1) :  #??
            #     continue
            # else:
            small = lst[j]
            big = lst[j + 1]
            if lst[j] > lst[j + 1]:
                lst[j] = big
                lst[j + 1] = small
    return lst

lst = [5, 1, 9, 10, 0, 2, 6, 2, 1]
output = bubble_sort(lst)
print(output)