import time

def Palindrome1(s) -> bool:
    start_time = time.time()
    ss = s.lower()
    filtered_alpha = list(filter(is_alpha, ss))
    j = -1
    for i in range(len(filtered_alpha)//2):
        if filtered_alpha[i] == filtered_alpha[j]:
            j  = j - 1
            continue
        else:
            end_time = time.time()
            run_time = end_time - start_time
            print("Palindrome1: ", run_time)
            return False
    end_time = time.time()
    run_time = end_time - start_time
    print("Palindrome1: ", run_time)
    return True

def is_alpha(ss):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for e in ss:
        if e in alpha:
            return True
        else:
            return False


def Palindrome2(s) -> bool:
    start_time = time.time()
    ss = s.lower()
    filtered_alpha = list(filter(is_alpha, ss))
    reversed_alpha = filtered_alpha[::-1]
    if filtered_alpha == reversed_alpha:
        end_time = time.time()
        run_time = end_time - start_time
        print("Palindrome2: ", run_time)
        return True
    else:
        end_time = time.time()
        run_time = end_time - start_time
        print("Palindrome2: ", run_time)
        return False




def Palindrome3(s) -> bool:
    start_time = time.time()
    ss = s.lower()
    filtered_alpha = list(filter(is_alpha, ss))
    reversed_alpha = filtered_alpha[::-1]
    end_time = time.time()
    run_time = end_time - start_time
    print("Palindrome3: ", run_time)
    return filtered_alpha == reversed_alpha


P_answer = Palindrome1("No lemon, no melon")
print(P_answer)
P_answer = Palindrome2("No lemon, no melon")
print(P_answer)
P_answer = Palindrome3("No lemon, no melon")
print(P_answer)
