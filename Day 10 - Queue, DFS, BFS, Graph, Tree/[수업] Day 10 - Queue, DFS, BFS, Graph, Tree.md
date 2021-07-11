## 오늘

- Queue
- DFS
- BFS
- Graph
- Tree

## Queue

- List 의 한 종류
- 그러나 일반 list와 다르게 원소를 넣고 뺄 때, 그 행위들이 제한적임 (FIFO)
    - `enqueue`: 원소를 추가할 때는 마지막에 넣고
    - `dequeue`: 원소를 뺄 때는 가장 처음에 들어온 애가 (First in, FI) 먼저 나옴 (First Out, FO)

## 그래프 탐색

- 그래프 (Graph) 탐색이란, 어떤 노드에서 시작해서 차례대로 모든 노드를 한 번씩 방문하는 알고리즘.
  - 인풋으로 Graph 와 starting node (root node) 가 주어져야 한다.
- 우리는 그래프 탐색 알고리즘중에서, 제일 유명한 DFS 와 BFS 를 배운다.

## DFS

- DFS (Depth First Search) 란?
    
    - 한국말로 `깊이 우선 탐색` 
    - 그렇다면 `깊이`란 무엇일까? 
        - `Depth (깊이)`: starting node 에서부터 특정 노드 n 까지 도달하는데 필요한 (최소한의) edge의 개수를 n의 depth 라고 부름
    
    - `깊이 우선`이란 무엇일까?
      - 깊이 우선 == 일단 최대한 깊게 가본다 == 갈 데까지 가본다
      - 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가, 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서, 이곳으로부터 다른 방향으로 다시 탐색을 진행
    
- DFS 구현
    - Stack 사용
        - `push`: 새로운 노드 (아직 방문해본 적이 없는 노드) 를 밟을 때, 그 노드를 스택에 push 함. push 된 노드는 방문된 노드.
        - `pop`: 더 이상 방문할 수 있는 노드가 없을 때, stack을 pop 하면서, pop 된 노드로 되돌아감.
        
    - DFS에서 Stack 을 사용하는 이유? 
        
        - Stack 에다가 내가 방문하는 노드들을 저장 (push) 함. 더 이상 진행할 수 있는 곳이 없으면 뒤로 돌아갈건데, DFS는 `가장 최근에 밟았던 곳`으로 되돌아감.
        - 가장 최근에 밟았던 곳을 잘 알려줄 수 있는 자료구조는 Stack임. `pop()`을 하면 가장 최근에 push 된 원소가 나오기 때문.
        
    - 코드
    
        ```python
        # Stack 구현
        class Stack:
        
            def __init__(self):
                self.store = []
        
            def is_empty(self):
                return len(self.store) == 0
        
            def push(self, e):
                self.store.append(e)
        
            def pop(self):
                if len(self.store) == 0:
                    return None
                last = self.store[-1]
                self.store = self.store[:-1]
                return last
        
        # DFS 구현
        def dfs(start_node, G):
            """
            Args:
            	  - start_node: 시작 노드
            	  - G: 그래프
            Returns:
            	  - visited: 모든 방문된 노드들
            """
        
            stack = Stack()
            visited = {}
            
            curr_node = start_node
            
            stack.push(start_node)
            visited[curr_node] = True
            
            while not stack.is_empty():
              
                # Pick next_node among curr_node's neighbors
                next_node = pick_next(curr_node, G, visited)
                if next_node is None:
                    # 더 이상 갈 곳이 없으면 되돌아간다 (pop 한다)
                    curr_node = stack.pop()
                    continue
        
                # Go to the next node
                curr_node = next_node
                stack.push(curr_node)
                visited[curr_node] = True
        
            return visited
          
          
        # pick_next 함수 구현
        def pick_next(curr_node, G, visited):
            """
            Args:
            	  - curr_node: 현재 그래프
            	  - G: 그래프
            """
            
            # G에서 curr_node 의 neighbors 를 구한다
            neighbors = ....
            
            # neighbors 중에서, 아직 방문되지 않은 노드를 하나 고른다.
            for neighbor in neighbors:
                if neighbor not in visited:
                    return neighbor
                  
            # neighbors 중에서, 다음으로 갈만한 노드가 없다면 
            # 즉, 모든 neighbor 노드가 방문되었거나 neighbors 가 없다면
            # None 을 리턴한다.
            return None
        ```
    
        

## BFS

- BFS (Breadth First Search) 란?

  - 한국말로 `너비 우선 탐색` . 깊이보다는 얕더라도 넓게 (wide)  탐색
  - `너비 우선` 이란, 그래서 무엇일까?
    - Starting 노드에서 가장 가까운 노드들부터 우선적으로 탐색.

- BFS 구현

  - Queue 사용

    - `enqueue`: 방문한 노드를 죄다 enqueue로 집어넣음
    - `dequeue`: 현 시점 노드를 dequeue로 뺌

  - BFS에서 Queue 를 사용하는 이유? 

    - BFS에서는 Enqueue를 통해 방문할 가능성이 있는 노드들이 차례로 (depth 순으로) 들어감
    - 이 때, dequeue를 통해 방문 가능성이 있는 아이들 중, 가장 depth 가 적은 노드부터 방문하고 싶음. 그래서 가장 먼저 들어왔던 원소를 dequeue 를 통해 빼내는 것임

  - 코드

    ```python
    # Queue 구현
    class Queue:
    
        # Attribute
        def __init__(self):
            self.store = []
    
        # Functions
        def is_empty(self):
            return len(self.store) == 0
    
        def enqueue(self, e):
            self.store.append(e)
    
        def dequeue(self):
            if self.is_empty():
                return None
            else:
                first_in = self.store[0]
                self.store = self.store[1:]
                return first_in
    
    # BFS 구현
    def bfs(start_node, G):
        
        q = queue()
        visited = {}
        
        curr_node = start_node
        
        q.enqueue(curr_node)
        visited[neighbor] = True
        
        while not q.is_empty():
          
            # 현재 노드 = Dequeue 된 노드
            curr_node = q.dequeue()
            
            # curr_node 의 neighbors 를 잘 구한다.
            neighbors = ... 
            
            # neighbors 중에서, 방문되지 않은 neighbor 들만 q에 enqueue한다.
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited[neighbor] = True
    ```

    

## Graph

- Node
- Edge: node 의 연결
    - directed vs undirected
        - directed graph: edge 에 방향이 있을 때 (ex: linked list)
    - weighted vs unweighted
        - weighted graph: edge 에 weight 가 있을 때
    - signed vs unsigned
        - signed graph: edge 에 부호 (+, -) 가 있을 때

## Tree
- 노드 사이에 상하관계가 있는 그래프
    - parent
    - child
- 예) 가족관계도
- Directed & Acyclic Graph (DAG) 중 하나

    


