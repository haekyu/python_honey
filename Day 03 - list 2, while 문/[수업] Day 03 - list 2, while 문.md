# Day 03: list 2, while 문

## 오늘 내용

- List 2
- loop 문 중에서 while 문
    - while
    - for

## 지난 시간 내용 정정

- 리스트 대소 비교
    - 예) ['a', 100, 'c'] > ['a', 2, 'e']
    - cf) 'a100c' < 'a2e'
    - Day 02 내용도 업데이트 했습니다



## List 2

- List란 **여러가지 원소**를 **순서대로** 저장한 데이터

- 이 때, 어떠한 원소가 **몇 번째**인지 상당히 관심이 많다.

- **Index** = (원소가) **몇 번째**인지를 나타내는 숫자

  - index는 0부터 시작
  - 음수 index 존재 (파이썬의 특징이기도 함)
      - `-1`번째 원소? == 가장 끝에 있는 원소
      - `-2`번째 원소? == 끝에서 두번째에 있는 원소

  - 예) ['a', 'b', 'c']
    - 'a'는 0번째 원소 혹은 -3번째 원소 ('a'의 index 는 0 혹은 -3)
    - 'b'는 1번째 원소 혹은 -2번째 원소 ('b'의 index 는 1 혹은 -2)
    - 'c'는 2번째 원소 혹은 -1번째 원소 ('c'의 index 는 2 혹은 -1)

- **Indexing**

  - 내가 index를 주고, 그 index번째에 해당하는 원소를 가지고 오는 행위

  - `lst[index]`: lst에서 index 번째에 해당하는 원소를 가져옴

    - 예1) indexing 으로 해당 원소 읽기 (read)

      - ```python
        >>> lst = ['a', 'b', 'c']
        >>> lst[1]
        'b'
        ```

    - 예2) indexing 으로 해당 원소 수정 (write)   

      - ```python
        >>> lst = ['a', 'b', 'c']
        >>> lst[1] = 'BBB'
        >>> lst
        ['a', 'BBB', 'c']
        ```

- **Slicing**

  - index의 범위를 주고, 그 범위에 해당하는 원소들을 통째로 가져오는 행위
  - `lst[index 범위]`: lst에서 index 범위에 해당하는 원소들을 가져옴
  - index 범위 표현 방법
    -  `from: to`
      - from (index) 이상에서
      - to (index) 미만까지
      - 예)
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[0: 3]
          ['a', 'b', 'c']
          ```
      
    - `from: to: step`
    
      - from (index) 이상에서
    
      - to (index) 미만까지
    
      - step 크기 / 방향 만큼
    
        -  step이 양수면 순방향
        -  step이 음수면 역방향
    
      - 예1) 순방향
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[0: 5: 2]
          ['a', 'c', 'e']
          ```
    
      - 예2) 역방향 1
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[4: 0: -1]
          ['e', 'd', 'c', 'b']
          ```
    
      - 예3) 역방향 2: ['e', 'd', 'c', 'b', 'a'] 이 나오려면?
    
        - 실패) 
    
          - ```python
            >>> lst = ['a', 'b', 'c', 'd', 'e']
            >>> lst[4: -1: -1]
            []
            ```
    
          - `lst[4]` ('e') 부터 `lst[-1]` ('e') 직전까지 (즉 'e' 포함되지 않음) 원하는 것이므로 아무것도 나오지 않음
    
        - 성공)
    
          - ```python
            >>> lst = ['a', 'b', 'c', 'd', 'e']
            >>> lst[-1 : -6 : -1]
            ['e', 'd', 'c', 'b', 'a']
            ```
    
    - index 범위를 줄 때, 숫자들을 생략하는 경우가 많다 (편리하니까).
    
      - `from` : 첫 index가 default. 생략 시 자동 첫 index가 들어감
    
      - `to`: 끝 index가 default. 생략 시 자동 마지막 index가 들어감
    
        -  cf) `from`과 ` to`가 모두 생략되면 자동으로 처음과 끝, 즉 전체 리스트가 자동으로 잡힘
    
      - `size`: 1이 default. 생략 시 자동 1이 들어감
    
      - 예1) to 생략 - (from 부터) "끝까지" 
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[3:]
          ['d', 'e']
          ```
    
      - 예2) from 생략 - "처음부터" (to 까지)
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[:3]
          ['a', 'b', 'c']
          ```
    
      - 예3) from, to 생략 - "처음부터" "끝까지" / size 생략 - 순방향으로 한칸씩
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[:]
          ['a', 'b', 'c', 'd', 'e']
          ```
    
      - 예4) from, to 생략 - "처음부터" "끝까지"
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[::-1]
          ['e', 'd', 'c', 'b', 'a']
          ```
  
- `append`

  - 리스트 맨 뒤에 원소 하나를 덧붙이는 함수
  
  - 규칙
  
    - ```python
      lst = [...]
      lst.append(원소)
      ```
    
  - 예)
  
    ```python
    lst = ['a', 'b', 'c']
    lst.append(3)
    print(lst)
    ```
    실행 결과
  
        ['a', 'b', 'c', 3]
  
  - **실수 주의!**
  
    ```python
    lst = ['a', 'b', 'c']
    lst = lst.append('d')
    print(lst)
    ```
    실행 결과
    
        None
  
- List 와 str 의 비교

  - 둘은 비슷. 웬만한 연산 둘 다 됨, 둘이 본질적으로 같은 형식으로 컴퓨터 내부에서 저장되어있기 때문.
  
    - indexing, slicing, `len()`, ... 웬만한 것들은 list 와 str 모두 사용 가능
  
  - 차이점
  
    - list 는 수정이 되고 (list는 read/write 가능하고)
  
    - str 은 수정이 안됨 (str은 read-only)
  
    - 예) list 는 write 가능
      ```python
      lst = ['a', 'b', 'c']
      lst[0] = 'A'
      print(lst)
      ```
  
      실행 결과
  
      ```
      ['A', 'b', 'c']
      ```
  
    - 예2) str 은 read-only
  
      ```python
      sss = 'abc'
      sss[0] = 'A'
      ```
  
      실행 결과 (에러 뜸. str 은 뭔가를 assign 못한단 뜻. 즉, 뭔가 값을 대입하지 못한단 뜻.)
  
      ```
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      TypeError: 'str' object does not support item assignment
      ```
  
      
  
- 잡 지식) Shallow copy 와 Deep copy

  - Shallow copy
  
    - (한 변수를 다른 변수에 복사할 때) **이름만 가볍게 복사**
  
    - 두개의 변수 중 하나를 변경했을 때, 나머지 변수도 동일하게 수정됨
  
    - 예) 
  
      - ```python
        # Shallow copy
        >>> ori_list = ['a', 'b', 'c']
        >>> cp_lst = ori_lst
        
        # 두 변수 중 하나가 수정되면, 나머지 변수도 똑같이 수정됨
        >>> cp_lst[0] = 'AAA'
        >>> op_lst
        ['AAA', 'b', 'c']
        ```
  
  - Deep copy
  
    - (한 변수를 다른 변수에 복사할 때) **내용물 전체를 깊게 복사**
  
    - 두개의 변수 중 하나를 변경하더라도, 나머지 변수는 수정되지 않음. Deep copy가 끝나면 두 변수는 그냥 완전 독립체
  
    - 예)
  
      - ```python
        # Deep copy
        >>> ori_list = ['a', 'b', 'c']
        >>> cp_lst = ori_lst[:]
        
        # 두 변수 중 하나가 수정되더라도, 나머지 변수는 변함 없음
        >>> cp_lst[0] = 'AAA'
        >>> op_lst
        ['a', 'b', 'c']
        ```
  
  - Cf) 기본 데이터 타입 (숫자, 문자, 참/거짓) 은 deep copy 와 shallow copy 를 고민할 필요가 없다. 그냥 변수에 다른 변수를 assign 하더라도, 알아서 deep copy가 됨
  
    - 예)
  
      - ```python
        # 기본 데이터타입의 copy
        >>> original = 10
        >>> copied = original
        
        # 한 변수의 수정
        >>> original = 3
        
        # 나머지 변수는 변하지 않는다
        >>> copied
        10
        ```



## While 문

- Loop문 (반복문)

  - While문은 Loop문의 한 종류
  - Loop문은 뭔가 반복행위가 많을 때 사용. 그 반복 행위를 일일이 다 작성하는 것보다 Loop문을 사용하면, 코드를 작성하는 나도 편하고 나중에 보기에도 아름다운 코드가 된다.

- Syntax (사용 문법)

  - ```python
    while 조건:
        액션 1
        액션 2
        액션 3
        ...
    ```

  - 조건이 True이면 계속 액션 1,2,3, ... 을 실행해라.

- `iteration`

  - 반복 한바퀴를 iteration 이라고 부른다. (액션 1,2,3,... 한 차례)
  - iteration 의 매개체를 iterator 라고 부르는데, 그 iterator 변수의 이름을 보통 `i` 라고 많이 쓴다 (iterator의 앞글자 따서). 아래 예시에도 iterator 들의 이름을 `i` 라고 썼다.

- 예 1)

  - ```python
    i = 0
    
    while i < 3:
      	print(i)
        i = i + 1
    ```

  - 실행 결과

    ```shell
    0
    1
    2
    ```

- 예 2)

  - ```python
    lst = ['a', 'b', 'c']
    
    i = 0
    while i < 3:
        print(lst[i])
        i = i + 1
    ```

  - 실행 결과

    ```shell
    'a'
    'b'
    'c'
    ```

- 무한 루프

  - Iteration 이 무한히 도는 상황을 말하는데, 보통은 좋은 상황은 아니다. 특별히 무한 루프를 내가 만든 것이 아닌 한에서는 거의 대부분 뭔가 버그가 있기 때문에 발생한다. 무한 루프의 더 큰 문제는...... 무한 루프가 돌고있다는 상황 자체를 인지하기 어렵기 때문이다! (그것도 모른 채 코드는 계속 무한으로 끝없이 돌고있으면.. 슬프다) 내 코드가 단순히 좀 늦게 돌아가는 코드인지, 아니면 무한루프가 돌아가고 있는 것인지 그걸 잘 파악해야 버그를 금방 금방 고칠 수 있다.

  - 무한 루프를 안만드는게 최선이지만, 은근 흔하게 실수하다 많이 만들어진다. 그래서 **무한루프인지 빨리 파악**하는게 정말 정말 중요하다. 여러 방법이 있겠지만, iteration마다 iterator를 프린트 해줘서 iterator가 제때 업데이트 되는지 확인하는 방법도 있다.

    - 예) 무한루프

      - ```python
        lst = ['a', 'b', 'c']
        
        i = 0
        while i < 3:
            
            lst[i] = lst[i] + lst[i]
            
            # 아래 코드가 주석처리되어 실행되지 않는다고 하면
            # i = i + 1
        ```

        실행 결과 

        ```
        (무한 루프 + 아무것도 안나옴 + 언제까지 기다려야 하는지 모를 답답함)
        ```

    - 예) 무한루프임을 빨리 깨닫도록 iterator 프린트

      - ```python
        lst = ['a', 'b', 'c']
        
        i = 0
        while i < 3:
          
            print('----------')
            print('i = ' + i)
            
            lst[i] = lst[i] + lst[i]
            
            # 아래 코드가 주석처리되어 실행되지 않는다고 하면
            # i = i + 1
        ```

      - 실행 결과

        ```shell
        i = 0
        i = 0
        i = 0
        i = 0
        i = 0
        i = 0
        i = 0
        ...
        (엇 뭔가 이상하다는 직감이 바로 온다)
        ```

    - 예) 매 iteration마다 너무 자주 프린트를 하면 (스크롤 압박이 심하고) 코드의 성능이 떨어질 수 있기에, 대충 N번째 (자기가 고르기 나름) iteration마다 프린트 하기도 한다

      - ```python
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        
        i = 0
        while i < 9:
          
            if i % 3 == 0:
                print('----------')
                print('i = ' + i)
            
            lst[i] = lst[i] + lst[i]
            
            i = i + 1
        ```

      - 실행 결과

        ```shell
        i = 0
        i = 3
        i = 6
        i = 9
        ```

  - 디버깅 잘하려면 프린트를 잘 할 줄 알아야 함. 본인의 센스 영역이므로 경험치를 잘 쌓으면 좋다!



















