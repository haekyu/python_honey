## Day 02: 변수, 조건문, list 1

### 변수
- `=` (assign 연산자) 사용
    - ex) `x = 3`
        - x 에다가 3을 넣는다 
        - x 를 3으로 정의 / assign 한다
- 변수 이름 짓기
    - 규칙 (기본 룰)
        - 영어
        - 한글 (가능은 한데 쓰지 마세요)
        - 숫자 (그러나 숫자로 시작하는 변수 이름은 불가능)
            - x1 (O)
            - 1x (X)
        - 띄어쓰기 X
            - x y
            - age of ppl
                - ageofppl
        - `_` (언더바, 언더스코어)
            - 보통은 띄어쓰기 대용으로 사용
            - `age_of_people`
    - 네이밍 센스
        - (아름다운 코드를 위해) 변수 이름을 잘 짓는게 중요하다
        - 변수의 이름만 보고도 걔가 무슨 역할을 하는 애인지 느낌 오게끔!
            - a, b, c, i, ii, aa, bb 같은 변수 이름 쓰면 욕먹음
        - 너무 길지 않게
            - 모음을 생략하는 사람들이 있다
                - avg (average)
                - ppl (people)
                - cnt (count)
                - 기타 등등... 다른 사람들 코드 많이 보다보면 사람들이 보통 뭘 어떻게 줄이는지 대충 감이 온다.
        - 여러 단어가 포함된 변수의 네이밍 스타일
            - 예) average of price 라는 이름의 변수를 만들고 싶을 때 
            - `_` (언더스코어) 사용
                - average_of_price
            - Camel 방식
                - 각 단어를 대문자로 시작 (맨 처음 단어는 소문자로 시작하기도 함) 
                - averageOfPrice
    
### 조건문
- 주어진 조건에따라 무언가 다른 action을 하게끔 만들고 싶을 때 조건문을 사용한다. 
- if 문
    ```python
        if (boolean으로 표현된 조건):
            액션1
            액션2
            액션3
            ...
    ```
    - (boolean 으로 표현된) 조건이 True 일 때, 액션1, 액션2, 액션3, ... 을 실행시킨다.
    - 조건에 걸리는 액션1, 2, 3, ... 이 indent (빈 블럭, 주로 탭 하나) 하나로 들여써진 것을 잘 기억!!
    - 조건 옆에 콜론 (:) 이 쓰인 것도 잘 기억!
    - 예1) x라는 변수가 21334 라고 하자. x 가 7의 배수라면 y 를 True로 정의.
        ```python
        x = 21334
        if x % 7 == 0:
            y = True
        ```
    
    - 예2) x라는 변수가 "abc" 라고 하자. x에 "B" 가 들어가 있다면, x 를 "aBc"로 정의해라. 
        ```python
        x = "abc"
        if 'B' in x:
            x = "aBc"
        ```
     
- if else 문
    ```python
        if 조건:
            액션 1
            액션 2
            ...
        else:
            액션 A
            액션 B
            ...
    ```
    - 조건이 True 일 때, 액션 1, 액션 2, ... 을 실행시킨다. 만약 그 조건이 False 라면 액션 A, 액션 B, ... 을 실행시킨다.
    - 예1) x라는 변수가 21334 라고 하자. x 가 7의 배수라면 y 를 True로 정의, 만약 그렇지 않다면 y를 False 로 정의.
        ```python
        x = 21334
        if x % 7 == 0:
            y = True
        else:
            y = False
        ```

-  if elif (else) 문
    - 확인하고 싶은 조건이 여러개일때!
    - 예) x = "abcDe" 라 하자.
        - 만약, x에 "A" 가 있으면 ...
        - 그렇지 않고, x 에 "B" 가 있으면 ...
        - 그것도 아니고 ("A", "B" 둘 다 x에 없고), "C" 가 x 에 있으면 ...
    - (if elif 를 모른다면) 위 예시를 다음과 같이 쓸 것이다.
        ```python
            if "A" in x:
                ...
            else:
                if "B" in x:
                    ...
                else:
                    if "C" in x:
                        ...
        ```
        위 코드는 아름답지 않다. 조건이 많아질 수록 indent가 계속 들어가게 되어 코드가 가로로 길어지기 때문.
    - (***if elif*** 를 사용하여) 위 예시를 더 ***아름답게*** 고쳐보자.
        ```python
            if "A" in x:
                ...
            elif "B" in x:
                ... 
            elif "C" in x:
                ...
            else:
                ...
        ```
        else 블럭은 생략 가능하다. 중요한 것은 `elif` 가 `else if` 의 줄임말이라는 것.
    - 예) x = "aBcDefg" 일 때, 
        - 만약 "A" 가 x에 있다면 print("AAA")
        - 그렇지 않고, 만약 "B" 가 x 에 있다면 print("BBB")
        - 그렇지 않고, 만약 "C" 가 x 에 있다면 print("CCC")
        - 그렇지 않고, 만약 "D" 가 x 에 있다면 print("DDD")
        - 그렇지 않으면, print("XXX")
            ```python
                x = "aBcDefg"
          
                if "A" in x:
                    print("AAA")
                elif "B" in x:
                    print("BBB")    
                elif "C" in x:
                    print("CCC")
                elif "D" in x:
                    print("DDD")
                else:
                    print("XXX")
            ```
            실행 결과
            ```
            BBB
            ```
    - 예2) x = "aBcDefg" 일 때, 위 예시와 다르게 "AAA"와 "DDD"가 모두 프린트 되게 하려면?
        ```python
        x = "aBcDefg"
        if "A" in x:
            print("AAA")
        
        if "B" in x:
            print("BBB")    
        
        if "C" in x:
            print("CCC")
        
        if "D" in x:
            print("DDD")
        ```
        실행 결과
        ```
        BBB
        DDD
        ```
    
