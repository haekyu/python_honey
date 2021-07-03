## 오늘
- 보충
    - tuple
    - default parameter
    - lambda: 이름 없는 함수
- dict
- recursion (재귀)
- sorting
    - 이론
    - Big-O notation

## 보충

- tuple
    - **여러가지** 원소를 **순서대로** 배열한 데이터
    - `(` 원소1, 원소2, 원소3, ... `)`
    - tuple vs list
        - tuple 이랑 list 는 굉장히 비슷해서 웬만한 연산은 둘 다 가능
            - indexing
                <!-- ```python
                tp = ('a', 'b', 'c')
                print(tp[-1])
                ``` -->
            - slicing
                tp = ('a', 'b', 'c', 'd')
                print(tp[1:])
        - 하지만, tuple 은 수정이 불가하고 (read-only, immutable) list 는 수정이 가능합니다 (write 가능, mutable)
            - 예)
                <!-- ``` -->
                tp = ('a', 'b', 'c')
                tp[0] = 'A'
                <!-- ``` -->
- default parameter
    - parameter == 함수의 인풋변수
    - default parameter == 함수의 인풋변수 중에서 default 값을 가지는 애들
    - default parameter 설정하는 방법
        def f(input1, input2 = default 값, ...):
            sdf
            sdf
            sfd
            sdf

    - default parameter 사용하는 방법
        - default 값을 쓰는 경우
            - 값을 안주면 알아서 default 값으로 사용 됨
            - 예)
                def f(x, y=0):
                    return x + y

            - f(1) == 1  

        - default 값을 쓰지 않는 경우
            - 내가 원하는 값을 주면 됨

                def f(x, y=0):
                    return x + y

                f(1, 100) == ?
                f(1, y=100)

        - 
        <!-- PCA(n_components=None, *, copy=True, whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None)
        PCA(random_state='sdfsdf') -->
        - 평범한 parameter와 default parameter 가 같이 있을 경우, 평범한 parameter 먼저 써줘야 함
            def f(a=1, b, c=3, d):
                sdfd
                sdf
                sdf

            def g(a, b, c=3, d=4):
                sdf
                sdf
                dsf

            f(100, 200, 300)
            g(100, 200, 300)

- lambda: 이름 없는 함수 
    - 장점: 공간 save (특히나, 굳이 로직을 reuse 할 필요 없이, 그냥 한줄정도로 땡치고싶을 때)
    - 규칙
        lambda 인풋1, 인풋2, ... : 함수 결과 output 나오는 식
    - 
        def f(x, y):
            return x + y

        lambda x, y: x + y

        f(1, 2)
        (lambda x, y: x + y) (1, 2)

        def sqrt(x):
            return x ** 0.5

        루트 64

### dict
- (이론) Hash Table
    - 빠른 search 를 위해 태어난 자료 구조
    - (key(word), value) 여러개 + 맵핑 당 순서 없음
    - Search time complexity: O(1) 
- key가 있는지 없는지 (membership)
    - in
- 정의
    d = {key1: val1, key2: val2, key3: val3}

    d = {}
    d[key1] = val1
    d[key2] = val2
    d[key3] = val3

    d = {
        'apple': 'red', 
        'banana': 'yellow',
        'peach': 'pink'
    }

    'apple' in d --> True / False
    'cherry' in d

    d['watermellon'] = 'green'

    d['watermellon'] = 'green_and_black'

    d['apple']

    
### Recursion (재귀)
- Recursive function (재귀함수)
- 피보나치 수열
    - 1, 1, 2, 3, 5, 8, 13, 21, ...
    - 피보나치 수열의 7번째 숫자는 21
- 내가 어떤 값을 구하려고 하는데 (함수의 값을 구하려고 하는데)
    - 내가 같은 로직으로 구했던 (즉 같은 함수를 통해 구했던) 다른 값들이 이용될때
    - 그 때 재귀함수 (recursion) 을 쓴다
    - def f(i): 
        return i번째 피보나치 수

    - f(7) = f(6) + f(5)
    - f(x) = f(x-1) + f(x-2)
- Recursive function 만드는 **규칙**

def f(input, ...):

    # Base case

    # Logic (induction)


def f(i):
    # Base case
    if i <= 1:
        return 1

    # Logic (inductive hypothesis)
    return f(i - 1) + f(i - 2)

def f(i):
    if i <= 1:
        return 1
    else:
        return f(i - 1) + f(i - 2)

O(2^n)
O(n^2)

def f(i): 
    return f(i - 1) + f(i - 2)

f(7) = f(6) + f(5)
f(6) = f(5) + f(4)
f(5) = f(4) + f(3)
f(4) = f(3) + f(2)
f(3) = f(2) + f(1)
f(2) = f(1) + f(0)
f(1) = f(0) + f(-1)
f(0) = f(-1) + f(-2)
f(-1) = f(-2) + f(-3)
.....
def sum_1_to_n(n):
    return 1 + 2 + 3 + 4 + .... + n-1 + n

    # logic
    sum_1_to_n(n) = n + sum_1_to_n(n-1)

sum_1_to_n(10)

def fact(n):
    ????

fact(10)

n! = 1 * 2 * 3 * .... * n

- 재귀함수는 함부로 쓰면 안됨
    - 계산량이 exponential 하게 많아질 수 있기 때문에
    - 예) f(n) = f(n-1) + f(n-2)
- 빠른 재귀함수를 만드는 방법
    - (O) Dynamic programming
    - (X) Tail recursion
- Dynamic programming
    - 내가 이미 계산한 값이 있으면, 그 값을 기억해 뒀다가 reuse 하는방식

    - 

    def f(n, memo):

        # Base case

        # Logic

            # 내가 미리 구한 값이 memo에 있는지 확인

            # 있으면 그냥 쓰면 되고

            # 없으면 그때 계산 때린다

            # 메모한다

            # 리턴한다

            
def f(n, memo):

    # Base case
    if n <= 1:
        return 1

    # Logic: f(n) = f(n-1) + f(n-2)
    
    # f(n-1)
    # f_n_1 = reuse를 하든, 새로 계산을 때리든 구해요
    if n-1 in memo:
        f_n_1 = memo[n-1]
    else:
        f_n_1, memo = f(n-1, memo)

    # f(n-2)
    # f_n_2 = reuse를 하든, 새로 계산을 때리든 구해요
    if n-2 in memo:
        f_n_2 = memo[n-2]
    else:
        f_n_2, memo = f(n-2, memo)

    # 메모 (n)
    f_n = f_n_1 + f_n_2
    memo[n] = f_n

    # return f_n, memo



// memo[n] = f(n)
memo = {}
f(100, memo)

### Sorting
- Selection Sort: O(n^2)
- Insertion Sort: O(n^2)
- Merge Sort: O(n log n)


def merge_sort(lst):
    
    # Divide (left_lst, right_lst)
    middle_idx = int(len(lst) / 2)
    left_lst = lst[:middle_idx]
    right_lst = lst[middle_idx:]

    # Sort (left_lst sorting, right_lst sorting)
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    # Merge (! append 잘 하면 됨)
    merged_lst = []

    return lst # sort 된 버전의 리스트
