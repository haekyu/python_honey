def is_prime_number (x: int):
    lst = []
    if x <= 1:  #basic case가 먼저 오도록 코딩   #x, output은 로컬변수
        output = "x>1"
        return output
    else:
        for i in range(2, x):
            if x % i == 0:  #append 대신 약수의 개수를 count하는 게 더 아름다움
                lst.append(i)
        if len(lst) == 0:
            #break를 써서 약수 발견하면 멈추게 -> 7-10줄 줄일 수 있음
            output = True   #output은 로컬변수
        else:
            output = False   #output은 로컬변수
        return output


x = 17  #x는 글로벌변수
output = is_prime_number(x)   #output은 글로벌변수지만 로컬변수와 값이 같음
print(output)
