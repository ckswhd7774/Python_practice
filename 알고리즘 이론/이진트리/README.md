# 트리란?

- 그래프의 일종으로, 여러 노드가 한 노드를 가르킬 수 없는 구조
- 회로(Cycle)이 없고, 두 노드를 잇는 길이 하나뿐인 그래프

## 트리의 구조

<img width="1023" alt="스크린샷 2021-06-28 오후 8 50 44" src="https://user-images.githubusercontent.com/77820288/123635978-45d0d380-d857-11eb-8e13-4baf869337e6.png">


- 루트(Root): 부모가 없는, 가장 상윗단의 노드
- 노드(Node): 트리 구조의 자료 값을 담고 있는 요소
- 에지(Edge): 노드 간의 연결선
- 부모(Parent): 연결된 두 노드 중 더 상위에 있는 노드
- 자식(Child): 연결된 두 노드 중 하위에 있는 노드
- 경로(Path): 두 노드를 연결하는 에지의 시퀀스
- 잎새 노드(Leaf Node): 자식 노드가 없는 노드
- 내부 노드(Internal Node): 잎새 노드를 제외한 모든 노드
- 레벨, 깊이(Level, Depth): 루트 노드로부터의 경로의 길이
- 트리의 높이(Height): 트리에서 가장 큰 레벨 값

### 트리의 특징

- 하나의 노드에서 다른 노드로 이동하는 경로는 유일
- Acyclic하다. (Cycle이 존재하지 않는다)
- 모든 노드는 서로 연결되어 있다. (외딴 섬이 존재하지 않는다.)
- 하나의 Edge를 끊으면 두개의 Sub-Tree로 분리된다.
- Edge의 수는 [Node의 수 - 1]이다.

## 이진 트리의 순회(Traversal)

- 깊이 우선 순회 (Preorder, Depth-First Traversal) (node -> left -> right)

<img width="985" alt="스크린샷 2021-06-28 오후 8 53 12" src="https://user-images.githubusercontent.com/77820288/123636026-54b78600-d857-11eb-8cec-4406a473fe22.png">

```python
# 배열 기반 이진 트리
import array
from collections import deque

class BinaryTree:
    def __init__(self, arr) :
        self.array = array.array('I', arr)
        
    # 전위순회
    def preorder(self) :
        def DFS(idx) :
            if idx >= len(self.array) :
                return 
            else :
                print(self.array[idx], end='')
                DFS(idx*2+1) # 왼쪽
                DFS(idx*2+2) # 오른쪽

        DFS(0)
        print()
tree = BinaryTree([i for i in range(7)])
tree.preorder()
## 0134256

```

전위 순회는 부모 노드 → 왼쪽 노드 → 오른쪽 노드 순서로 탐색한다.

- 대칭 순회 (Inorder, Symmetric Traversal) (left -> node -> right)

<img width="988" alt="스크린샷 2021-06-28 오후 8 55 13" src="https://user-images.githubusercontent.com/77820288/123636053-5d0fc100-d857-11eb-9d37-c6f98824a62a.png">

```python
# 배열 기반 이진 트리
# 중위순회
    def inorder(self) :
        def DFS(idx) :
            if idx >= len(self.array) :
                return 
            else :
                DFS(idx*2+1) # 왼쪽
                print(self.array[idx], end='')
                DFS(idx*2+2) # 오른쪽

        DFS(0)
        print()
tree.inorder()
## 3140526
```

중위 순회는 왼쪽 노드 → 부모 노드 → 오른쪽 노드 순서로 탐색한다.

- 후위 순회 (Postorder) (left -> right -> node)

<img width="986" alt="스크린샷 2021-06-28 오후 8 55 21" src="https://user-images.githubusercontent.com/77820288/123636079-6567fc00-d857-11eb-8474-e771adf62c6d.png">

```python
# 배열 기반 이진 트리
# 후위순회
    def postorder(self) :
        def DFS(idx) :
            if idx >= len(self.array) :
                return 
            else :
                DFS(idx*2+1) # 왼쪽
                DFS(idx*2+2) # 오른쪽
                print(self.array[idx], end='')

        DFS(0)
        print()
tree.postorder()
## 0123456
```

후위 순회는 왼쪽 노드 → 오른쪽 노드 → 부모 노드 순서로 탐색한다.

## 노드 기반 이진 트리의 순회

```python
# 노드 기반 이진 트리
from collections import deque
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]
        self.root = node_list[0]
    def preorder(self):
        def DFS(root):
            if root == None:
                return
            else:
                print(root.value, end='')
                DFS(root.left)
                DFS(root.right)
        DFS(self.root)
        print()
    def inorder(self):
        def DFS(root):
            if root == None:
                return
            else:
                DFS(root.left)
                print(root.value, end='')
                DFS(root.right)
        DFS(self.root)
        print()
    def postorder(self):
        def DFS(root):
            if root == None:
                return
            else:
                DFS(root.left)
                DFS(root.right)
                print(root.value, end='')
        DFS(self.root)
        print()
    def bfs(self, value):
        Q = deque()
        Q.append(value)
        while Q:
            current = Q.popleft()
            print(current.value,end='')
            if current.left != None:
                Q.append(current.left)
            if current.right != None:
                Q.append(current.right)
                
tree.preorder
tree = BinaryTree([i for i in range(7)])
tree.preorder()
tree.inorder()
tree.postorder()
tree.bfs(tree.root)
```

## 이진 트리의 탐색 (Search)

- 너비 우선 탐색 (Breadth-First Search; BFS)

<img width="986" alt="스크린샷 2021-06-28 오후 8 59 18" src="https://user-images.githubusercontent.com/77820288/123636103-6dc03700-d857-11eb-83ca-f00377d24530.png">

- 깊이 우선 탐색 (Depth-First Search; DFS)

<img width="987" alt="스크린샷 2021-06-28 오후 8 59 25" src="https://user-images.githubusercontent.com/77820288/123636142-77499f00-d857-11eb-8ea5-0635c0c8f52f.png">