from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Return the indices of the k weakest rows in the binary matrix

        Args:
            mat (List[List[int]]): binary matrix
            k (int): integer

        Returns:
            List[int]: indices of the k weakest rows in the binary matrix
        
        Time complexity:
            Best and Worst O(M(N + logM)) = O(MN) to create nodes + O(MlogM) to append node to min heap
            where M is the number of rows and N is the number of columns in binary matrix

        Space complexity:
            Best and Worst O(MN)
            where M is the number of rows and N is the number of columns in binary matrix
        """
        m, n = len(mat), len(mat[0])
        nodes = []
        res = []

        # Create nodes
        for i in range(m):
            soldiers = 0
            j = 0
            while j < n and mat[i][j] != 0:
                soldiers += mat[i][j]
                j += 1
            index = i + 1
            node = Node(index, soldiers)
            nodes.append(node)

        # Create min heap
        min_heap = PriorityQueue(nodes)

        # Extract k minimum nodes
        for _ in range(k):
            node = min_heap.extract_min()
            res.append(node.index - 1)

        return res


class PriorityQueue:
    def __init__(self, nodes):
        """Create a min heap by inserting nodes to the array-based binary tree

        Args:
            nodes (List[Node]): list of nodes
        
        Time complexity:
            Best and Worst O(NlogN) to insert all the nodes
            where N is the total number of nodes in the heap
        """
        self.heap = [None] * (len(nodes) + 1)
        # Pointer to the last node in heap
        self.rear = 0
        # Append all nodes to heap
        for node in nodes:
            self.append(node)

    def append(self, node):
        """Insert node to the heap

        Args:
            node (Node): node to be inserted
        
        Time complexity:
            Best and Worst O(logN) to rise the new node
            where N is the total number of nodes in the heap
        """
        # Increment pointer
        self.rear += 1
        # Push node to rear
        self.heap[self.rear] = node
        # Rise the node
        self.rise(self.rear)

    def extract_min(self):
        """Extract the minimum node from heap

        Returns:
            Node: node with the highest priority (minimum value)
        
        Time complexity:
            Best and Worst O(logN) to sink the leaf node
            where N is the total number of nodes in the heap
        """
        if self.rear != 0:
            root = self.heap[1]
            leaf = self.heap[self.rear]
            # Replace root with lead
            self.heap[1] = leaf
            # Decrement pointer
            self.rear -= 1
            # Sink the leaf
            self.sink(1)
            return root

    def rise(self, curr: int):
        """Rise the node until parent is smaller than the current

        Args:
            curr (int): current node index
        
        Time complexity:
            Best and Worst O(logN)
            where N is the total number of nodes in the heap
        """
        # Parent index
        parent = curr // 2
        while parent > 0 and self.isGreaterThan(parent, curr):
            # Swap parent with current
            self.heap[parent], self.heap[curr] = self.heap[curr], self.heap[parent]
            # Move pointers up
            curr = parent
            parent = curr // 2

    def sink(self, curr: int):
        """Sink the node until children is bigger than the current

        Args:
            curr (int): current node index
        
        Time complexity:
            Best and Worst O(logN)
            where N is the total number of nodes in the heap
        """
        # Children index
        left, right = curr * 2, curr * 2 + 1
        # Case 1: two children
        if right <= len(self):
            if self.isGreaterThan(curr, left) or self.isGreaterThan(curr, right):
                min_child = self.min_child(left, right)
                # Swap curr with min child
                self.heap[curr], self.heap[min_child] = self.heap[min_child], self.heap[curr]
                # Move pointer down
                curr = min_child
                self.sink(curr)
        # Case 2: one child
        elif left <= len(self):
            if self.isGreaterThan(curr, left):
                # Swap curr with left
                self.heap[curr], self.heap[left] = self.heap[left], self.heap[curr]
                # Move pointer down
                curr = left
                self.sink(curr)
        # Case 3: no child

    def min_child(self, left, right):
        """Find the min child (node with a higher priority) between left and right child

        Args:
            left (Node): node
            right (Node): node

        Returns:
            node: left or right node
        """
        if self.isGreaterThan(left, right):
            return right
        else:
            return left

    def isGreaterThan(self, key1: int, key2: int) -> bool:
        """Compare the values of the nodes with the keys given

        Args:
            key1 (int): key of the node
            key2 (int): key of the node

        Returns:
            bool: whether node with key1 has a greater value than node with key2,
            node with a lower value has a higher priority (due to min heap property)
        """
        node1 = self.heap[key1]
        node2 = self.heap[key2]
        # Case 1: compare value
        if node1.val > node2.val:
            return True
        elif node1.val < node2.val:
            return False
        # Case 2: compare index
        elif node1.index > node2.index:
            return True
        elif node1.index < node2.index:
            return False

    def __len__(self) -> int:
        return self.rear


class Node:
    def __init__(self, index: int, val: int):
        self.index = index
        self.val = val


sol = Solution()
mat = [
  [1, 1, 0, 0, 0], 
  [1, 1, 1, 1, 0], 
  [1, 0, 0, 0, 0], 
  [1, 1, 0, 0, 0], 
  [1, 1, 1, 1, 1]]
k = 3
print(sol.kWeakestRows(mat, k))
