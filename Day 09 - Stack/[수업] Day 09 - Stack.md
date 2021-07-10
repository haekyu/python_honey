## Day 09

- Stack
- 행렬 (리스트로 표현)
- DFS

## Stack

### Stack 이란?
- list 의 한 종류
- 그러나 일반 list와 다르게 원소를 넣고 뺄 때 그 행위들이 제한적임 (LIFO)
    - 원소를 넣을 때는 가장 마지막에 넣고 (Last in -> LI) 
    - 원소를 뺄 때는 가장 마지막에 들어온 원소를 먼저 뺀다 (First out -> FO) 

### Stack 구현
- Class 의 구성요소
    - attribute
        - store: 리스트. 원소들을 보관.
    - function
        - push: 원소를 추가
          - 인풋 원소를 store 의 마지막에 넣는다
        - pop: 원소를 뺀다
          - 가장 마지막에 있는 원소를 리턴한다
          - store 는 마지막 원소가 없는 버전으로 업데이트됨
    
- 코드

    ```python
    class Stack:
        def __init__(self):
            self.store = []
        def push(self, e):
            self.store.append(e)
        def pop(self):
            if len(self.store) == 0:
                return None
            last = self.store[-1]
            self.store = self.store[:-1]
            return last



## 행렬

- List 로 행렬을 표현할 수 있다. row value들의 리스트로 표현하며, 각 row value 도 값들을 리스트로 저장한다.

  - 행렬 = `[ row1, row2, row3, ...]`
  - 이 때 `row1 = [?, ?, ?, ...]`, `row2 = [?, ?, ?, ...]`

- 예)

  ```
  10 20
  30 40
  ```

  처럼 생긴 행렬은

  ```
  [[10, 20],
   [30, 40]]
  ```

  과 같이 표현한다. 한줄로 쓰면 아래와 같다.

  ```
  [[10, 20], [30, 40]]
  ```

- 특정 위치 (특정 row와 column) 의 값 얻기

  - 리스트의 indexing 을 통해 행렬의 특정 row와 column에 위치한 값을 얻을 수 있다.
  - `행렬[row][col]`
    - `행렬[row]` 를 통해 먼저 row value들을 얻는다. 이 row value들은 해당 row 에 위치한 모든 column 값들을 가지고 있는 리스트이다.
    - `행렬[row][col]`: `행렬[row]`에서 얻은 column value들 중에서, 내가 원하는 특정 col 값을 indexing을 통해 얻는다.

## DFS (Depth First Search)

- 그래프 (Graph) 를 탐색하는 방법.
- 한국말로는 깊이 우선 탐색법
  - 깊이 우선 == 일단 최대한 깊게 가본다 == 갈 데까지 가본다
  - 시작점에서부터, 가능한 길을 최대한 한 방향으로 갈 수 있을 때까지 쭉 가다가, 더 이상 갈 수 없게 되면 다시 한걸음씩 되돌아가다가, 되돌아가는 중간에 다른 갈만한 갈림길이 생기면 그 새로운 갈림길로 또 쭉 갈 수 있을 때까지 진행하며, 그래프 전체를 탐색하는 방법.
- Stack을 사용하여 구현한다.