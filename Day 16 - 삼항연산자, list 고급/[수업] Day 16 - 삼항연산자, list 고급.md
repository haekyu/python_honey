## 오늘

- 삼항연산자
- list comprehension
- dict comprehension
- list를 다른 함수로 parsing 하는 함수
    - map        
    - filter

## 삼항연산자

- if else 문을 한 줄로 구겨넣은 표현식

- 세 개의 항으로 구성되어있음

  - (조건이 True일때의 값) `val_true`
  - (조건) `if cond else` 
  - (else일때의 값) `val_false`

- 문법)

  ```python
  val_true if cond else val_false
  ```

- 예)

  ```python
  k = 10
  val = k + 1 if k % 2 == 0 else k + 2
  
  print(val)
  ```

  실행 결과

  ```
  11
  ```

## List comprehension
- 단 한줄로 list 를 for문으로 만드는 방법중에 하나
- 예) 가장 간단한 경우
    ```python
    # [1, 2, 3, 4] 를 만들고 싶다면
    
    # Ver1: for문 & append
    lst = []
    for i in range(4):
        lst.append(i)
    
    # Ver2: list comprehension
    lst = [i for i in range(4)]
    ```

- 예) if 문의 조건을 만족할때에만 append 하는 경우

  ```python
  # [1, 3, 5, 7] 을 만들고 싶다면
  
  # Ver1: for문 & append
  lst = []
  for i in range(8):
      if i % 2 == 1:
          lst.append(i)
      
  # Ver2: list comprehension
  lst = [i for i in range(8) if i % 2 == 1]
  ```

- 예) if 문과 else 문에따라 다른 원소를 append 하는 경우

  ```python
  # [0, 1, 0, 3, 0, 5, 0, 7] 을 만들고 싶다면
  
  # Ver1: for문 & append
  lst = []
  for i in range(8):
      if i % 2 == 0:
          lst.append(0)
      else:
          lst.append(i)
  
  # Ver2: list comprehension
  lst = [0 if i % 2 == 0 else i for i in range(8)]
  ```

  


## Dictionary comprehension
- 단 한줄로 dictionary 를 for문을 이용하여 만드는 방법

- 예) 가장 간단한 경우

  ```python
  # 이러한 딕셔너리를 만들고 싶을 때
  d = {
    0: 1, 
    1: 2, 
    2: 3, 
    3: 4
  }
  
  # Ver1: 일반적인 for 문
  d = {}
  for k in range(4):
      d[k] = k + 1
  
  # Ver2: dictionary comprehension
  d = {k: k+1 for k in range(4)}
  ```

- 예) if 문의 조건을 만족할때에만 맵핑이 추가되는 경우

  ```python
  # 이러한 딕셔너리를 만들고 싶을 때
  d = {
    0: 1,
    2: 3, 
    4: 5
  }
  
  # Ver1: 일반적인 for 문
  d = {}
  for k in range(5):
      if k % 2 == 0:
          d[k] = k + 1
  
  # Ver2: dictionary comprehension
  d = {k: k+1 for k in range(5) if k % 2 == 0}
  ```

- 예) if 문과 else 문에따라 다른 맵핑이 추가되는 경우

  ```python
  # 이러한 딕셔너리를 만들고 싶을 때
  d = {0:1, 1:3, 2:3, 3:5}
  
  # Ver1: 일반적인 for 문
  d = {}
  for k in range(4):
      if k%2 == 0:
          d[k] = k+1
          # key = k
          # val = k+1
      else:
          d[k] = k+2
          # key = k
          # val = k+2
  
  # Ver2: dictionary comprehension
  d1 = {(k if k%2 == 0 else k): (k+1 if k%2 == 0 else k+2) for k in range(4)}
  d2 = {k: (k+1 if k%2 == 0 else k+2) for k in range(4)}
  
  # cf) 아래는 불가능하다.
  {k: k+1 if k%2 == 0 else k: k+2 for k in range(4)}
  ```



## list를 다른 함수로 parsing 하는 함수
- map
    - list원소 각각 하나를 parser 함수로 처리
    
    - 인풋

      - 리스트 (예: `[a, b, c, d, e]`)
      - parser 함수 (예: `f`)

    - 아웃풋
    
      - 예)`[f(a), f(b), f(c), f(d), f(e)]`

    - 공식

      - `map(함수, 리스트)`
      - map() 함수의 결과는 map 이라는 클래스의 object 이므로, 우리가 익숙한 list 로 형변환시켜주면 좋다. 즉 `list(map(함수, 리스트))` 의 형태로 많이 쓰게 된다.
    
    - 예)
    
      ```python
      def f(x):
          return x % 3
        
      lst_in = [0, 1, 2, 3, 4, 5, 6, 7, 8]
      
      # 이름 있는 함수 버전
      lst_out1 = list(map(f, lst_in))
      print(lst_out1)
      
      # 람다 함수 버전
      lst_out2 = list(map(lambda x: x % 3, lst_in))
      print(lst_out2)
      ```
    
      실행 결과
    
      ```
      [0, 1, 2, 0, 1, 2, 0, 1, 2]
      [0, 1, 2, 0, 1, 2, 0, 1, 2]
      ```
    
      
    
- filter
    
    - list원소 중, 필터링 함수의 결과값이 true 가 되는 원소들만 걸러내는 함수
    
    - 인풋
    
        - 리스트 (예:`[a, b, c, d, e]`)
        - parser 함수 (예: `f`)

    - 아웃풋
    
        - `f(a), f(b), f(c), f(d), f(e)` 중에서 true 값을 주는 원소들
        - 예)
          - `f(a), f(b), f(c), f(d), f(e)` 값들이 다음과 같다면, 
            - f(a) == true
            - f(b) == false
            - f(c) == false
            - f(d) == true
            - f(e) == true 라면
          - filter 함수의 결과는 `[a, d, e]` 이다.

    - 공식
    
        - `filter(함수, 리스트)`

    - 예)
    
        ```python
        lst_in = [i for i in range(10)]
        
        def f(x):
            return x % 3 == 0
        
        # 이름 있는 함수 버전
        lst_out1 = filter(f, lst_in)
        print(lst_out1)
        
        # 람다 함수 버전
        lst_out2 = filter(lambda x: x % 3 == 0, lst_in)
        print(lst_out2)
        ```
    
        실행 결과
    
        ```
        [0, 3, 6, 9]
        ```
    
        