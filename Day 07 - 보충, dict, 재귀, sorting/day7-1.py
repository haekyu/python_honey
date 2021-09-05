def my_dict(word_lst):
    word_dict = {}
    for e in word_lst:
        if e[0] in word_dict:
            if e not in word_dict.values():
                '''
                print("e:", e)
                print(word_dict)
                val = word_dict[e[0]]
                val.append(e)
                print(val)
                word_dict[e[0]] = val
                '''
                word_dict[e[0]].append(e)
        else:
            word_dict[e[0]] = [e]  #초기값을 리스트로 넣어주여야 함
                                   #append는 업데이트 안해줘도 됨
    return word_dict

words = ["apple", "bear", "person", "aurora", "print", "boy", "ant", "an"]
word_dict = my_dict(words)
print(word_dict)



def my_count(word_lst):
    word_dict = {}
    for e in word_lst:
        if e[0] in word_dict:
            if e not in word_dict.values():
                '''
                print("e:", e)
                print(word_dict)
                val = word_dict[e[0]]
                val.append(e)
                print(val)
                word_dict[e[0]] = val
                '''
                word_dict[e[0]] = word_dict[e[0]] + 1  # +1한 값을 다시 assign 해줘야 업데이트 됨
        else:
            word_dict[e[0]] = 1    #초기값을 리스트로 넣어주여야 함
                                   #append는 업데이트 안해줘도 됨
    return word_dict

print(my_count(words))

'''
#
>>> a = {1: [2]}
>>> a[1] + [3]
[2, 3]
>>> a
{1: [2]}
#
>>> a = {1: [2]}
>>> a[1] = a[1] + [3]
>>> a
{1: [2, 3]}
'''