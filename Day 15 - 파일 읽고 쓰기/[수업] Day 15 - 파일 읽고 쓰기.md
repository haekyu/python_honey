

# Day 15 - 파일 읽고 쓰기

- 파일 객체를 통해 읽고 쓰기
- 파일의 위치

## 파일 객체를 통해 읽고 쓰기
### 기본

- 파일 객체란? 다음을 말한다.
  - file reader
  - file writer
  - file appender
-  `open()`: 이 함수를 쓰면 파일 객체를 만들 수 있다
    - `open()` 함수 쓰는 법:
        - `f = open(파일경로, 옵션)`
        - 여기서 f를 파일 객체라고 부름
    - `open()` 함수의 옵션 종류
        - `'r'`: read. file reader 를 만들고 싶을 때 사용
        - `'w'`: write. file writer 를 만들고 싶을 때 사용
        - `'a'`: append. file appender 를 만들고 싶을 때 사용
- `close()`: 파일 닫기
    - `파일객체.close()` 로 사용
    - `open()` 하고 볼일 다 봤으면 반드시 파일을 닫아줘야함. 닫지 않으면 다른 프로그램이 같은 파일을 수정했을 때 파일이 꼬이기 때문.

### 파일 읽쓰 구조1: open & close

- 문법

  ```python
  f = open(파일 경로, 옵션)
  
  # ...파일을 읽어서 저장을 하든
  # ...파일에 스트링을 쓰든 
  # ...암튼 원하는 일을 한다
  
  f.close()
  ```

### 파일 읽쓰 구조2: with

- With 문은 f.close() 를 생략한 버전. close() 를 굳이 콜하지 않아도 with 문이 끝나면 알아서 파일이 저절로 닫힌다.

- 문법

  ```python
  with open(파일 경로, 옵션) as f:
      # ...파일을 읽어서 저장을 하든
      # ...파일에 스트링을 쓰든 
      # ...암튼 원하는 일을 한다
  ```

### Read

- 파일 객체를 만들 때, open() 의 옵션으로 'r' 을 준다.
    
- Read ver1: 한 줄 한 줄 읽기
    
    - 무한 루프 만들어서 한 줄 한 줄 읽는 방법. 일단 길고 무한루프가 있기 때문에 아름답지는 않다.
    
    - 문법)
    
      ```python
      f = open(파일경로, 'r')
      
      lines = []
      while True:
          # 한 줄 읽기
          line = f.readline()
          
          # EoF (End of File) 이면 무한루프 종료
          if line == "":
              break
      
          # 읽었던 한 줄을 저장
          lines.append(line)
          
      f.close()
      ```
    
      
    
- Read ver2: 줄별로 한 방에 읽는 방법

    - 무한루프를 만드는 ver1보다 아름답다

    - 문법)

        ```python
        f = open(파일 경로, 'r')
        lines = f.readlines()
        f.close()
        ```

- Read 된 결과의 newline ('\n') 정리하기

    - 파일객체로 파일을 읽으면, 한 줄 한 줄 읽은 결과에서 마지막에 newline 이 붙을 수 있다.
    
        - 예) 
        
            file.txt
            
            ```
            aaa
            bbb
            ccc
            ```
            
            file.txt 를 읽으면
            
            ```python
            with open("./file.txt", 'r') as f:
                lines = f.readlines()
            print(lines)
            ```
            
            실행 결과
            
            ```
            ["aaa\n", "bbb\n", "ccc"]
            ```
        
    - 만약 저 line 의 trailing (맨 뒤에 있는) newline을 없애고싶다면, 다음 후처리 코드를 넣어주면 된다.
    
        ```python
        for i, line in enumerate(lines):
            lines[i] = line.rstrip('\n')
        ```
    
        - 예)
    
          ```python
          with open('./file.txt', 'r') as f:
              lines = f.readlines()
          
          for i, line in enumerate(lines):
              lines[i] = line.rstrip('\n')
              
          print(lines)
          ```
    
          실행 결과
    
          ```
          ["aaa", "bbb", "ccc"]
          ```

### Write

- 새로운 파일을 쓰기. 기존 파일을 쓰라고 명령을 내릴 경우, 아예 덮어쓰기를 한다. 

- 파일 객체를 만들 때, open() 의 옵션으로 'w' 를 준다.

- `write()` 
    
    - 원하는 string 을 파일에 써주는 함수
    - 파일을 열고나서 닫기전에 원하는 스트링을 write() 로 써주면 됨
    
- 예)
    
     ```python
     with open('write_ex.txt', 'w') as f:
         f.write('Hello\n')
         f.write('World\n')
         f.write('Haha')
     ```
    
    실행 결과, write_ex.txt를 열어보면 아래와 같을 것이다.
    
    ```
    Hello
    World
    Haha
    ```

### Append

- 기존 파일의 내용에 새 내용을 덧붙임.

- 파일 객체를 만들 때, open() 옵션으로 'a'를 준다.

- Write 와 마찬가지로 `write()` 함수를 쓴다.

- 예)

    write_ex.txt 가 아래와 같다고 해보자

    ```
    Hello
    World
    Haha
    ```

    Append 를 해보자

    ```python
    with open('write_ex.txt', 'a') as f:
        f.write('New Hello\n')
        f.write('New World\n')
        f.write('New Haha')
    ```

    실행 결과, write_ex.txt를 열어보면 아래와 같을 것이다.

    ```
    Hello
    World
    HahaNew Hello
    New World
    New Haha
    ```

## 파일의 위치/경로
- 파일 위치 기본 개념
    - 상위 디렉토리에서 하위 디렉토리로 하나 하나 깊게 들어가는 방식으로 작성
    - 상위/하위 디렉토리를 구분할 때 '/' 를 씀
        - 예)
            C:/Users/HONEY/Desktop/file.txt
    
- 절대 경로
    - 비유 예)
      - 미국 > 조지아 > 애틀란타 > 미드타운 > 조지아텍 > 코다빌딩 > 10층
      - 미국 > 조지아 > 애틀란타 > 린드버그 > 레스토랑1 
    - 예)
      - /Users/Name/Desktop/0804/test_file.txt
    
- 상대 경로
    
    - 비유 예, 위의 예시 사용)
        - 나의 위치가 현재 조지아텍 일 때, 코다빌딩 10층은 상대경로로 다음과 같이 표현
            - 나의 위치 > 코다빌딩 > 10층
        - 나의 위치가 현재 조지아텍 일 때, 레스토랑1은 상대경로로 다음과 같이 표현
            - 나의 위치 > 상위 경로 > 상위 경로 > 린드버그 > 레스토랑 1
            - 자세히 쓰면:
                - 나의 위치 (== 조지아텍) > 
                - 상위 경로 (== 미드타운) > 
                - 상위 경로 (== 애틀란타) >
                - 린드버그 > 
                - 레스토랑 1
    - 현재 나의 위치: `.` 으로 표시
        - 예) 
          - test_file.txt 의 절대 경로가  `/Users/Name/Desktop/0804/test_file.txt` 일 때,
          - 그리고 현재 위치가 `Desktop` 디렉토리일 때,  
          - test_file.txt 의 상대 경로는 `./0804/test_file.txt` 이다.
    - 상위 경로: `..` 으로 표시   
        - test1.txt 의 절대경로가 `/Users/Name/Desktop/dir1/test1.txt` 이고
        - test2.txt 의 절대경로가 `/Users/Name/Desktop/dir2/test2.txt` 이고
        - 현재 위치가 `dir1`일 때, `test2.txt` 의 상대 경로는 `./../dir2/test2.txt` 이다.
    
    