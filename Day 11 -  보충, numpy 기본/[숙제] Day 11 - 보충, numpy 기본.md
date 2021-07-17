### 1. 함수 연습

- rank 함수를 구현해 보세요.
    - **input**: 두 개의 list를 인풋으로 받습니다.
        - names: 학생들의 이름을 보관하는 리스트입니다.
        - scores: 각 학생들의 점수를 보관하는 리스트입니다. 모두 숫자입니다.
    - **output**: 
        - 각 학생들의 등수를 순서대로 보관하는 리스트를 리턴합시다.
- 예) 우리가 구현하는 함수를 get_ranks 라고 가정.
    ```python
    name_lst = ['일', '이', '삼', '사', '오']
    score_lst = [30, 42, 51, 18, 23]
    
    ranks = get_ranks(name_lst, score_lst)
    
    for name, score, rank in zip(name_lst, score_lst, ranks):
        print('{}번째 학생: 이름={}, 점수={}, 등수={}등'.format(name, score, rank))
    ```
    출력 결과
    ```
    0번째 학생: 이름=일, 점수=30, 등수=3등
    1번째 학생: 이름=이, 점수=42, 등수=2등
    2번째 학생: 이름=삼, 점수=51, 등수=1등
    3번째 학생: 이름=사, 점수=18, 등수=5등
    4번째 학생: 이름=오, 점수=23, 등수=4등
    ```
    
- 힌트) 학생 A의 등수는 "A의 점수보다 높은 다른 사람들의 명 수 + 1" 이 됩니다.



### 2. Palindrome

- Palindrome을 판단하는 **함수**를 만들어 보세요.
    - **input**: 어떤 string
    - **output**: input이 palindrome인지 아닌지 (True or False)
- Palindrome이란?
    - 앞에서부터 읽으나 뒤에서부터 읽으나 동일한 단어나 구를 말합니다.
    - 예) "소주만병만주소", "noon", "Wow", "My gym", "No lemon, no melon"
    - 규칙
        - 대소문자 구분하지 않음
        - 띄어쓰기, 쉼표 등 알파벳이 아닌 문자는 무시
        - 영어 단어만 있다고 가정
- **힌트 1)** 대소문자 구분하지 않기
  
    - 대소문자 구분하지 않는 방법 중 하나는 모든 문자를 대문자로 만들거나 모든 문자를 소문자로 만드는 것입니다.
    - lower() 함수나 upper() 함수를 사용해보세요. lower()는 어떤 스트링의 모든 문자를 소문자로 만드는 함수입니다. upper()는 모든 문자를 대문자로 만드는 함수입니다.
    - lower() 함수 예시
        ```python
        s = "No lemon, no melon"
        ss = s.lower()
        print(ss)
        ```
        출력 결과
        ```
        'no lemon, no melon'
        ```
- **힌트 2)** 알파벳만 걸러내기
    - 어떤 string의 알파벳만 filtering 하는 기능을 사용해 봅시다. 
    - `filter()` 함수를 사용합니다.
      
        - `filter(input1, input2)` 는 두 개의 input을 받습니다.
          
            - input1: 필터 (== 함수)
            - input2: 필터링 될 대상 (== sequence, 가령 string이나 list 등)
        - `filter(f, seq)` 는 seq안의 원소 각각을 f 라는 필터로 거릅니다. 이 때 f(원소) 가 True인 원소는 남기고, f(원소)가 False 인 원소는 다 버립니다.
        - filter 예시 1)
            ```python
            # 짝수인지 아닌지를 리턴하는 함수
            def is_even(n):
                if n % 2 == 0:
                    return True
                else:
                    return False
            
            filtered_evens = list(filter(is_even, [1, 2, 3, 4, 5]))
            print(filtered_evens)
            ```
            출력 결과 
            ```
            [2, 4]
            ```
        - filter 예시 2)
            ```python
            ss = 'no lemon, no melon'
            filtered_alphas = list(filter(str.isalpha, ss))
            print(filtered_alphas)
            ```
            출력 결과
            ```
            ['n', 'o', 'l', 'e', 'm', 'o', 'n', 'n', 'o', 'm', 'e', 'l', 'o', 'n']



### 3. 재귀함수 연습

- Factorial 함수를 구현해 보세요. 단! 재귀함수 버전으로 구해보세요.
    - **input**: n
    - **output**: n!의 값

- n!은 다음과 같이 정의합니다.
    - n이 0보다 작거나 같은 경우: n! = 1
    - n이 0보다 큰 경우: n! = n * (n-1)!

- 예) 
    ```python
    print(fac(0))
    print(fac(3))
    print(fac(5))
    ```
    출력 결과
    ```
    1
    6
    120
    ```



### 4. output 없는 함수

- Swap 함수를 구현해봅시다. 
    - **input**: 세 개의 인풋을 받습니다.
        - 어떤 list
        - index1
        - index2
    - **output**: 리턴하는 아웃풋은 없습니다! 아웃풋이 없는 함수도 있습니다!!
- 하는 일
    - 인풋으로 받은 리스트에서, 두 원소의 위치를 바꿉니다.
    - 바꿀 위치는 인풋으로 받은 두 인덱스입니다.
- 예)
    ```python
    lst = [0, 1, 2, 3, 4]
    swap(lst, 3, 0)
    print(lst)
    ```
    출력결과
    ```
    [3, 1, 2, 0, 4]
    ```
    잘 관찰해 보면, lst[3]과 lst[0]의 위치가 바뀌어있음을 알 수 있습니다. 
- swap함수의 output은 딱히 없지만, 무언가 일을 하고 있음을 알 수 있습니다!
- output이 없는 함수를 void 함수라고 부르기도 합니다. void는 empty라는 뜻입니다.