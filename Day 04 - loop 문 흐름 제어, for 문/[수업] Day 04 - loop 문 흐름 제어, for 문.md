## Day 04: Loop 문 흐름 제어, for 문

### 오늘 내용

- Loop 문 흐름 제어

  - break
  - continue

- for 문

  

### Loop 문의 흐름을 바꾸는 명령

- break (iteration 중단)
    - break 를 만나는 순간부터 전체 iteration 중단
    
    - 예)
        ```python
        i = 0
        while i < 10:
            print(i)
        
            # update i
            # i = i + 1 
            i += 1
        
            if (i == 5):
                break
        ```
        
        실행 결과
        
        ```
        0
        1
        2
        3
        4
        ```
        
        
    
- continue (iteration 스킵)
    
    - continue 를 만나는 순간부터 다음 iteration 으로 스킵
    
    - 예)
        ```python
        i = 0
        while i < 5:
            print('-' * 10)
            print('curr:', i)
        
            # update i
            # i = i + 1 
            i += 1
        
            if (i == 3):
                continue
        
            print('after:', i)
        ```
        
        실행 결과
        
        ```
        ----------
        curr: 0
        after: 1
        ----------
        curr: 1
        after: 2
        ----------
        curr: 2
        ----------
        curr: 3
        after: 4
        ----------
        curr: 4
        after: 5
        ```
        
        

### for 문

- 데이터 여러개가 있으면, 원소들을 (자동) 순차적으로 방문하는 loop
    - 그래서 list 랑 for 문이 궁합이 잘 맞음

- 문법
    ```python
    for 이터레이터 in 여러/순차 데이터:
        어쩌고
        저쩌고
        ...
    ```
    - 이터레이터가 차례로 데이터 내의 원소가 되면서 어쩌고 저쩌고 액션을 취한다. 

- 예)
    
    ```python
    lst = ['a', 'b', 'c']
    for e in lst:
        print(e)
    ```
    
    실행 결과
    
    ```
    'a'
    'b'
    'c'
    ```
    
- `range`

    - for 문을 자주 사용하는 방식 중에 리스트의 원소를 하나씩 방문하는 경우도 많이 있지만, 연속된 숫자를 차례대로 사용하는 경우도 꽤 많다. 이 때 필요한 것이 `range` 함수이다.

    - range 함수를 잘 쓰면, `여러 숫자들의 순차 데이터`를 만들 수 있다!

    - 예) 

        - 만약 iterator `i`가 0, 1, 2, ..., 99 순서대로 되길 원한다면...

        - 방법1)

            - ```python
                for e in [0, 1, 2, 3, 4, 5, 6, ......., 99]:
                    print(e)
                ```

            - 내가 손으로 일일이 0부터 99까지 타이핑해야하는 수고로움 + 가로 스크롤 압박 

            - 즉 매우 좋지 않은 hard coding 임

        - 방법 2)

            - ```python
                # [0, 1, ..., 99] 리스트 만들기
                lst = []
                i = 0
                while i < 100:
                    lst.append(i)
                    i = i + 1
                
                # 위에서 만든 리스트 사용!
                for e in lst:
                    print(e)
                ```

            - [0, 1, ..., 99] 리스트를 코딩으로 만들어 사용.

            - 방법 1보단 괜찮다. 솔직히 range 함수 모르면 이렇게라도 하면 된다. 그러나 [0, 1, ..., 99] 리스트를 만들기 위해 다섯줄이나 사용하기때문에 아름답진 않다.

        - 방법 3) 

            - ```python
                for i in range(.....):
                    어쩌고
                    저쩌고
                    ....
                ```

            - range 함수를 잘 쓰는 방법!!! 다섯줄을 사용해서 [0, 1, ..., 99] 리스트를 만들지 않아도 된다! 

    - `range` 쓰는 법

        - `range(from, to)`

            - from 이상 to 미만까지 순차적인 숫자의 배열

            - 예) `range(0, 3)` 는 0, 1, 2 배열을 만듦

                - 그러나 range 함수의 결과값은 숫자들의 배열이긴 하지만 list 데이터 타입은 아님. 그냥 range 라는 데이터 타입임. 

                    ```python
                    >>> range(0, 3)
                    range(0, 3)
                    
                    >>> type(range(0, 3))
                    <class 'range'>
                    ```

                - 그치만 list 로 형변환하면 list 형식으로 range 결과를 확인할 수 있음.

                    ```python
                    >>> list(range(0, 3))
                    [0, 1, 2]
                    ```

            - 예) 

              ```python
              for i in range(0, 3):
                  print(i)
              ```

              실행 결과

              ```
              0
              1
              2
              ```

              

        - `range(from, to, step)`
            
            - from 이상부터 to 미만까지, step 만큼 간격을 갖는 숫자의 배열
            
            - 예 1)
            
                ```python
                for i in range(0, 10, 2):
                    print(i)
                ```
            
                실행 결과
            
                ```
                0
                2
                4
                6
                8
                ```
            
            - 예 2)
            
                ```python
                for i in range(-10, 0, -2):
                    print(i)
                ```
            
                실행 결과
            
                ```
                -10
                -8
                -6
                -4
                -2
                ```
            
            - 예 3)
                
                ```python
                lst = ['a', 'b', 'c', 'd', 'e']
                for i in range(0, 5, 2):
                    e = lst[i]
                    print(e)
                ```
                
                실행 결과
                
                ```
                'a'
                'c'
                'e'
                ```
            
        - `range(to)`
            
            - 0부터 to까지의 숫자 배열
                
                - from: 0이 default
                - step: 1이 default
                
            - 제일 흔하게 쓰는 경우
                
            - 예)
                
                ```python
                for i in range(3):
                    print(i)
                ```
                
                실행 결과
                
                ```
                0
                1
                2
                ```
                
                
