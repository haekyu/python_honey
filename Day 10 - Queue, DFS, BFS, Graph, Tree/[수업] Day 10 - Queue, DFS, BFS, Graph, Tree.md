## 오늘

- Queue
- DFS
- BFS
- Graph
- Tree

## Queue

- List 의 한 종류
- 원소를 넣고 뺄 때, 특정한 행위밖에 하지 못하는 list (FIFO)
    - `enqueue`: 원소를 추가할 때는 마지막에 넣고
    - `dequeue`: 원소를 뺄 때는 가장 처음에 들어온 애가 (First in, FI) 먼저 나옴 (First Out, FO)

## DFS

- Graph 를 탐색하는 알고리즘
    - Graph 를 탐색한다는 이야기는, Graph 의 node 들을 방문해본다는 이야기인데, edge 를 통해서만 방문 진행을 할 수 있다는 이야기
- DFS 의 인풋
    - Graph
    - Starting point (starting node)
- DFS (Depth First Search) 의 탐색 룰
    - Depth (깊이): starting node 에서부터 특정 노드 n 까지 도달하는데 필요한 (최소한의) edge의 개수를 n의 depth 라고 부름 
    - 최대한 깊이 가보려고 한다. 갈 수 있을 때까지 계속 깊이 간다.
- DFS 구현
    - Stack 사용
        - push: 새로운 노드 (아직 방문해본 적이 없는 노드) 를 밟을 때, 그 노드를 push 함
        - pop: 더 이상 방문할 수 있는 노드가 없을 때, back 을 하면서 pop 함.
    - Stack 을 사용하는 이유
        Stack 에다가 내가 방문하는 노드들을 push 함. dead end 에 도달하면 (혹은 더 이상 진행할 수 있는 곳이 없으면) 뒤로 back 할건데, 가장 직전에 밟았던 곳으로 back 하기 때문에 stack을 사용함 (즉 가장 처음 들어왔던 starting point로 점프하지 않음). 이 때 뒤로 돌아갈 때 pop 을 사용.

## BFS
- Breath First Search: 얕고 넓게 보려는 서치
- Queue를 통해서 구현

## Graph
- Node
- Edge: node 의 연결
    - directed vs undirected
        - directed graph: edge 에 방향이 있을 때 (링크드리스트)
    - weighted vs unweighted
    - signed vs unsigned

## Tree
- 노드 사이에 상하관계가 있는 그래프
    - parent
    - child
- 예) 가족관계도
- Directed & Acyclic Graph (DAG) 중 하나

- Pandas
- Numpy

- ML

- 파일 읽고 쓰기
- 스트링 포맷팅
- 재귀
- 소팅 (숙제)
- 깃허브
- 터미널
- 정규표현

