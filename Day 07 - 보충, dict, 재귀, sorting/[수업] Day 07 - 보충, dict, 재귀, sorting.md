## 오늘

- 보충
    - tuple
    - default parameter
    - lambda: 이름 없는 함수
- Dictionary (dict)
- Recursion (재귀)
- Sorting
    - 이론
    - Big-O notation

## 보충

### tuple

- **여러가지** 원소를 **순서대로** 배열한 데이터

- tuple 만들기

    - 소괄호로 열고 닫고, 그 안에 데이터들을 순서대로 콤마(,)로 구분하여 나열
    - `(원소1, 원소2, 원소3, ... )`

- tuple vs list
    - 비슷한 점: tuple 이랑 list 는 굉장히 비슷해서 웬만한 연산은 둘 다 똑같이 사용 가능
        - indexing
            
            ``` python
            tp = ('a', 'b', 'c')
            print(tp[-1])
            ```
            
            실행 결과
            
            ```
            'c'
            ```
            
        - slicing
            
            ```python
            tp = ('a', 'b', 'c', 'd')
            print(tp[1:])
            ```
            
            실행 결과
            
            ```
            ('b', 'c', 'd')
            ```
        
    - 다른 점
        
        - tuple 은 수정이 불가하고 (read-only, immutable)
            
        - list 는 수정이 가능 (write 가능, mutable)
            
        - 예)
        
            ```python
            tp = ('a', 'b', 'c')
            tp[0] = 'A'
            ```
        
            실행 결과: 에러 뜸. tuple 에는 item assignment (아이템 / 원소 수정) 안된다는 뜻
        
        
            ```
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: 'tuple' object does not support item assignment

### Default parameter

- parameter == 함수의 인풋변수

- default parameter == 함수의 인풋변수 중에서 default 값을 가지는 애들

- default parameter 설정하는 방법
    
    ```python
    def f(input1, input2=default2, ...):
        ...
    ```

    위에서 input2 라는 변수는 default2 라는 기본값 (default 값) 을 갖게 된다.
    
- default parameter 사용하는 방법
    - default 값을 쓰는 경우
        - default parameter에 값을 주지 않으면 알아서 default 값으로 사용 됨
        
        - 예)
            
            ```python
            def f(x, y=0):
                return x + y
            
            output = f(1)
            print(output)
            ```
            
            실행 결과
            
            ```
            1
            ```
        
    - default 값을 쓰지 않는 경우
        - (default) parameter에 내가 원하는 값을 주면, 내가 준 값이 인풋 변수에 들어감
    
        - 방법1) 기존에 default parameter 배우기 전에 하던 것 처럼, 그냥 인풋 변수의 순서에 맞게 값을 주거나
        
        - 방법2) `특정 변수 이름 = 내가 원하는 값` 의 형식으로, 변수 이름을 콕 찝어 값을 줘도 된다. 이 때의 변수를 keyword argument 라고 부르기도 한다. 다른 말로 하면, 함수를 call 할 때 인풋 변수의 이름이 명시적으로 쓰인 경우, 그 인풋 변수를 keyword argument 라고 한다.
        
            - 방법 2) 는 왜 생겼을까?
            
                - (뇌피셜) Default parameter 가 엄청 많은 함수인 경우, 맨 끝에 있는 default parameter 만 값을 설정하고싶고 나머지 앞쪽 default parameter 들은 그냥 기본값을 쓰고싶다고 해보자. 이 경우, 인풋 값을 줄 때 변수 순서대로 주는 방법밖에 모른다면, 맨 끝 parameter 만 값을 따로 설정하고싶음에도 불구하고 앞에 있는 모든 다른 paramter 까지 값을 설정해줘야한다. 즉 비효율적.
                
                - 예) 
                
                    ```python
                    def PCA(n_components=None, *, copy=True, whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None):
                        ...
                    ```
                    
                    위와 같이 PCA 라는 함수를 쓰고 싶다고 해보자. default parameter가 정말 많다. 맨 마지막 인풋 변수 random_state 만 값을 따로 지정하고싶을 때 제일 효율적인 방법은 `방법 2) keyword argument` 를 사용하는 것이다.
                    
                    ```python
                    PCA(random_state=어쩌고저쩌고)
                    ```
                    
                    만약 방법 1) 만 안다면...
                    
                    ```python
                    PCA(
                        n_components=None, 
                        *, 
                        copy=True, 
                        whiten=False, 
                        svd_solver='auto', 
                        tol=0.0, 
                        iterated_power='auto', 
                        random_state=어쩌고저쩌고
                    )
                    ```
                    
                    이렇게 써야겠지..... 아주 비효율적이다 (내 손이 아프다) + 스크롤 압박 (아름답지 않다).
            
        - 예) Default parameter 사용 예시
        
            ```python
            def f(x, y=0):
                return x + y
            
            # 방법 1) 일반 함수 call 방식
            output1 = f(1, 100)
            
            # 방법 2) keyword argument
            output2 = f(1, y=100)
            
            print(output1)
            print(output2)
            ```
        
    - 평범한 parameter (non-default paramter) 와 default parameter 가 같이 있을 경우, 평범한 parameter 먼저 써줘야 함.
        
        - 예) 
            
            ```python
            def f(a, b, c=3, d=4):
                ...
            ```
        
        - 왜 non-default parameter 와 defaut parameter 간 순서가 생겼을까?
    
          - (뇌피셜) 이렇게 순서를 정해놓지 않으면 어느 인풋 변수에 어떤 값을 넣어야 할지 모르겠는 곤란한 경우가 생긴다.
        
          - 예) 
        
            ```python
            def f(a=1, b, c=3, d):
                print(a, b, c, d)
                
            f(100, 200, 300)
            ```
        
            위 경우를 생각해보자. 100, 200, 300 중에서 두 개는 non-default parameter 인 b 나 d 의 값이 될텐데.. 누가 어떤 값을 가지게 될지 모르는 난감한 상황이 발생한다. 아마 그래서 non-default parameter 를 먼저 앞에 두고, 그 다음에 default parameter 들이 오는 순서가 생기지 않았을까 싶다. 암튼 위의 코드를 실행하면 SyntaxError 가 발생한다.
        
            ```
            SyntaxError: non-default argument follows default argument
            ```

### lambda: 이름 없는 함수 

- Lambda 는 함수를 만드는 또 다른 방법 중 하나. 기존에 우리가 배웠던 def 를 통해 함수를 만드는 것과 다른 점은, **lambda 함수는 이름이 따로 없다**는 것이다.

- lambda 함수는 

    - 간단한 로직을
    - 한줄 정도로 땡치고 싶을때 줄로 쓴다.

- lambda 함수 만들기

    ```python
    lambda 인풋1, 인풋2, ... : 로직 (로직의 결과 output이 나오는 형태)
    ```

- 예)

    ```python
    def f(x, y):
        return x + y
    
    # 위 f 함수를 아래처럼 lambda 함수로 표현할 수 있다.
    lambda x, y: x + y
    
    # 우리가 함수를 call 할 때, 아래처럼 괄호 열고 닫고 인풋을 차례로 넣어주듯이
    f(1, 2) 
    
    # lambda 함수도 call 하려면, 아래처럼 괄호 열고 닫고 인풋을 차례로 넣어주면 된다
    output = (lambda x, y: x + y) (1, 2)
    print(output)
    ```

    실행결과

    ```
    3
    ```

    

## Dictionary

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

    
## Recursive function (재귀함수)

### 재귀함수란?

- 어떤 함수를 정의할 때 자기 자신을 정의에 사용하는 경우, 이 함수를 재귀함수라고 함.
- 예) 피보나치 수열
    - 1, 1, 2, 3, 5, 8, 13, 21, ...
    - 피보나치 수열의 7번째 숫자는 21
    - `fib(n) = fib(n-1) + fib(n-2)`

### 재귀함수 만들기

- 재귀 함수의 구성 요소

    - Base Case
        - 알고리즘의 **초기값**을 반드시 정의해줘야함!
        - 초기값을 정하지 않으면 Recursion Error 발생
    - Logic (induction, 재귀 식)

- 재귀 함수 코드 스타일

    ```python
    def f(input, ...):
        # Base case
        Base case 를 리턴
    		
        # Logic (induction)
        재귀 식을 통해 얻은 결과물을 리턴
    ```

- Base case의 중요성

    - Base case 가 없으면 코드가 무한의 깊이로 빠져들게 된다. 

    - 예) Base case 없는 경우

        ```python
        def f(i):
            # Base case 없음
        		
            # Logic
            return f(i - 1) + f(i - 2)
        
        print(f(7))
        ```

        실행결과: recursion 에서 실행가능한 최대 깊이를 초과했다 (대략 recursion이 무한으로 돌고 있다는 말임)

        ```
        RecursionError: maximum recursion depth exceeded
        ```

        왜 무한으로 빠지냐면... 컴퓨터 입장에서는

        ```
        f(7) 를 구하려면 f(6) + f(5) 니까 f(6) 를 먼저 구해야지
        f(6) 를 구하려면 f(5) + f(4) 니까 f(5) 를 먼저 구해야지
        f(5) 를 구하려면 f(4) + f(3) 니까 f(4) 를 먼저 구해야지
        f(4) 를 구하려면 f(3) + f(2) 니까 f(3) 을 먼저 구해야지
        f(3) 를 구하려면 f(2) + f(1) 니까 f(2) 를 먼저 구해야지
        f(2) 를 구하려면 f(1) + f(0) 니까 f(1) 을 먼저 구해야지
        f(1) 를 구하려면 f(0) + f(-1) 니까 f(0) 을 먼저 구해야지
        f(0) 를 구하려면 f(-1) + f(-2) 니까 f(-1) 을 먼저 구해야지
        f(-1) 를 구하려면 f(-2) + f(-3) 니까 니까 f(-2) 를 먼저 구해야지
        ....
        이렇게 끝이 없이 계산 계획만 세우다가 프로그램 터져버림
        ```

### 재귀함수 예시

- 예 1) 피보나치 함수

    ```python
    def fib(n):
        # Base Case
        if n <= 1:
            result = 1
    
        # Logic
        else:
            result = fib(n - 2) + fib(n - 1)
            
        return result
    ```

- 예 2) factorial 함수 (n! = 1 * 2 * 3 *... * n-1 * n)

    ```python
    def fac(n):
        # Base case
        if n == 1:
            result = 1
    
        # Logic
        else:
            result = n * fac(n - 1)
    
        return result
      
    print(fac(6))  
    ```

    실행 결과

    ```
    720
    ```

- 예 3) 1 + 2 + 3 + ... + n-1 + n

    ```python
    def sum_1_to_n(n):
        # Base case
        if n == 1:
            return 1
          
        # Logic
        return sum_1_to_n(n - 1) + n
      
    print(sum_1_to_n(10))
    ```

    실행 결과

    ```
    55
    ```

- 그러나... 재귀함수는 함부로 쓰면 안됨
    - 계산량이 exponential 하게 많아질 수 있기 때문에 / 중복 계산이 너무 많기 때문에
    - 예) f(n) = f(n-1) + f(n-2)
- 빠른 재귀함수를 만드는 방법 == 중복 계산을 없애자!
    - Dynamic programming
    - Tail recursion - 우리는 이 부분은 스킵합니다

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


​        

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