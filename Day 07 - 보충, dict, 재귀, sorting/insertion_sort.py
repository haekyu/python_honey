def insertion_sort(lst):
  
    for rnd in range(0, len(lst)):
        # Current rnd (round) 에서는
        # - lst[0: rnd] 가 현재로서는 sorted array이고
        # - lst[0: rnd + 1] 을 sorted array로 만들 예정이다.
        
        # sorted array에 새로 insert 할 target
        target_to_insert = lst[rnd]
        
        # target_to_put_in 을 lst[0: rnd] 안에 잘 넣는다.
        # target을 앞 원소부터 비교해가며, 삽입할 위치를 찾는다.
        # 삽입할 위치를 idx 라고 하자. idx = rnd 로 initialize 하는 것 주의!
        idx = rnd
        for j in range(0, rnd):
            if lst[j] > target_to_insert:
                idx = j
                break
        
        # target_to_insert 을 적절한 위치에 넣는다.
        inserted_left_lst = lst[:idx] + [target_to_insert] + lst[idx: rnd]
        lst[:rnd + 1] = inserted_left_lst
        
    return lst


lst = [5, 1, 2, 6, 2, 1, 3, 0]
sorted_lst = insertion_sort(lst)
print('before sorting:', lst)
print('after sorting:', sorted_lst)
