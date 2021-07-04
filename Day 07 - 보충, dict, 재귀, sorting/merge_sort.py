def merge_sort(lst):

    # Base case (!!!! 중요 !!!!)
    if len(lst) <= 1:
        return lst

    # Divide (left_lst, right_lst)
    middle_idx = int(len(lst) / 2)
    left_lst = lst[:middle_idx]
    right_lst = lst[middle_idx:]

    # Sort (left_lst sorting, right_lst sorting)
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    # Merge (!!!! 중요 !!!! append 잘 하면 됨, 아래 함수 참고)
    merged_lst = merge(left_lst, right_lst)

    return merged_lst


def merge(left_lst, right_lst):

    # If an input lst is empty, return the other lst
    # No need to merge
    if len(left_lst) == 0:
        return right_lst
    elif len(right_lst) == 0:
        return left_lst

    # Initialize variables
    left_idx = 0
    right_idx = 0
    merged_lst = []

    # Merge left_lst and right_lst
    while (left_idx < len(left_lst)) or (right_idx < len(right_lst)):

        # Check whether we want left or right value to insert
        want_left = False
        left_val = left_lst[left_idx]
        right_val = right_lst[right_idx]
        if left_val < right_val:
            want_left = True

        # Insert left value if want_left == True
        if want_left:
            merged_lst.append(left_val)
            left_idx += 1

        # Insert right value if want_left == False
        else:
            merged_lst.append(right_val)
            right_idx += 1

        # Check if all values of one of the list are scanned 
        if left_idx == len(left_lst):
            merged_lst = merged_lst + right_lst[right_idx:]
            break
        if right_idx == len(right_lst):
            merged_lst = merged_lst + left_lst[left_idx:]
            break

    return merged_lst


lst = [5, 1, 2, 6, 2, 1, 3, 0]
sorted_lst = merge_sort(lst)
print('before sorting:', lst)
print('after sorting:', sorted_lst)
