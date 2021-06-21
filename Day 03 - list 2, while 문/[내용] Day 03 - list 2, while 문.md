### 오늘 내용
- List 2
- loop 문 중에서 while 문
    - while
    - for

### 지난 시간 내용 정정

- 리스트 대소 비교
    - 예) ['a', 100, 'c'] > ['a', 2, 'e']
    - cf) 'a100c' < 'a2e'
    - Day 02 내용도 업데이트 했습니다



### List 2

- List란 **여러가지 원소**를 **순서대로** 저장한 데이터

- 이 때, 어떠한 원소가 **몇 번째** 인지에 상당히 관심이 많다.

- **Index** = (원소가) **몇 번째** 인지를 나타내는 숫자

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
          >>> lst[0:3]
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
          >>> lst[0:5:2]
          ['a', 'c', 'e']
          ```
    
      - 예2) 역방향 1
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[4:0:-1]
          ['e', 'd', 'c', 'b']
          ```
    
      - 예3) 역방향 2: ['e', 'd', 'c', 'b', 'a'] 이 나오려면?
    
        - ```python
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          
          # 실패 - lst[4] ('e') 부터 lst[-1] ('e') 직전까지 (즉 'e' 포함되지 않음) 원하므로 아무것도 나오지 않음
          >>> lst[4:-1:-1]
          []
          
          # 성공
          >>> lst[-1 : -6 : -1]
          ['e', 'd', 'c', 'b', 'a']
          ```
    
    - index 범위에서 index 를 생략하는 경우가 많다.
    
      - `from` : 첫 index가 default
    
      - `to`: 끝 index가 default 
    
      - `size`: 1이 default
    
      - 예)
    
        - ```python
          # ex) to 생략 - (from 부터) "끝까지" 
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[3:]
          ['d', 'e']
          
          # ex) from 생략 - "처음부터" (to 까지)
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[:3]
          ['a', 'b', 'c']
          
          # ex) from, to 생략 - "처음부터" "끝까지"
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[:]
          ['a', 'b', 'c', 'd', 'e']
          
          # ex) from, to 생략 - "처음부터" "끝까지"
          >>> lst = ['a', 'b', 'c', 'd', 'e']
          >>> lst[::-1]
          ['e', 'd', 'c', 'b', 'a']
          ```
    
        - 



























