## Day 20
- 정규표현

## 정규표현 (Regular expression)
- 문자열 (string) 의 패턴을 표현하는 문법
- 정규식 패턴
    - `\d`: 숫자 digit
        - "0", "1", "2", "3", "4", "5", ..., "9"
        - "10" --> \d\d
    - `\w`: word 문자 (영어 알파벳, 숫자, 한글, ...)
        - "a", "b", ...., "A", "B", "0", "1", ...
    - `\s`: white space
        - " ", "\t", "\n", "\f"
    - `패턴{n}`
        - 예) `\d{3}`: 숫자가 세 번 반복
    - `패턴{m, n}`
        - 최소 m번 최대 n번 반복
    - `*`
        - 반복이 0회 이상
    - `+`
        - 반복이 1회 이상
    - `^`
        - line 의 시작
    - `$`
        - line 의 끝
    - `[]`
        - 패턴의 집합
        - 예)
            - `[\d\w]`: 숫자, 문자 모두 포함
            - `[a-e]`: 알파벳 a 부터 e 까지
            - `[a-zA-Z]`: 소문자 알파벳 a 부터 z 까지, 대문자 알파벳 A 부터 Z 까지 모두 포함
            - `[0-3a-zA-Z]`: 숫자 0부터 3까지, a 부터 z 까지, 대문자 알파벳 A 부터 Z 까지 모두 포함
    - `[^패턴들]`
        - not 패턴들
    - cf) 완전 정규표현식은 아니지만, shell에서 "*" 은 많이 쓴다. 만약 아래와 같이 비슷한 형식의 이름을 가진 파일들이 있다면
        ```
        data0.txt
        data1.txt
        ...
        data10.txt
        ```
        아래처럼 "*" 을 사용하여 저 파일들을 한꺼번에 처리할 수 있다.
        ```
        mv data*.txt dir
        ```
- (파이썬에서) regular expression 사용하기
    - re 라이브러리 사용
    - 규칙)
        ```python
        import re

        pattern_finder = re.compile(r"정규표현식")
        lst = pattern_finder.findall(스트링 데이터)
        ```
    - 예)
        ```python
        import re

        s = "apple pineapple hello world"
        pattern_finder = re.compile(r"\w*apple")
        lst = pattern_finder.findall(s)

        print(lst)
        ```
        출력 결과
        ```
        ['apple', 'pineapple']
        ```
    