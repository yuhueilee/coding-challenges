'''
Question: Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    - All the visited cells of the path are 0.
    - All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
'''
import math
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vertices = self.createGraph(grid)
        discovered = Queue()
        source = vertices[0]
        if source.val == 1:
            return -1
        # Set distance to 1 due to the constraints (distance == number of cells visited)
        source.distance = 1
        source.visited = True
        source.discovered = True
        # Discover all source's neighbors
        for v in source.edges:
            v.distance = source.distance + 1
            v.discovered = True
            discovered.append(Node(v))
        
        while not discovered.isEmpty():
            u = discovered.pop()
            u.visited = True
            
            for v in u.edges:
                # Make sure the vertex is not visited yet
                if not v.visited:
                    distance = u.distance + 1
                    # Update distance if nearer
                    if distance < v.distance:
                        v.distance = distance
                    # Mark vertex as discovered
                    if not v.discovered:
                        v.discovered = True
                        discovered.append(Node(v))
                        
        # Handle case when target is not reachable
        target = vertices[n * (n-1) + (n-1)]
        if target.distance == math.inf:
            return -1
        return target.distance
    
    def createGraph(self, grid: List[List[int]]):
        vertices = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                id = n * i + j
                val = grid[i][j]
                vertex = Vertex(id, val)
                vertices.append(vertex)
        
        for i in range(n):
            for j in range(n):
                u_id = n * i + j
                u = vertices[u_id]
                # Only create edges for vertex with 0 value
                if u.val == 0:
                    adjacent_coords = [
                        (i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1), (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)
                    ]
                    for coord in adjacent_coords:
                        if 0 <= coord[0] <= (n-1) and 0 <= coord[1] <= (n-1):
                            v_id = n * coord[0] + coord[1]
                            v = vertices[v_id]
                            if v.val == 0:
                                u.edges.append(v)
        return vertices
    
    
class Vertex:
    def __init__(self, id: int, val: int):
        self.id = id
        self.val = val
        self.edges = []
        self.distance = math.inf
        self.visited = False
        self.discovered = False

class Node:
    def __init__(self, payload, prev=None, next=None):
        self.payload = payload
        self.prev = prev
        self.next = next
            
class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        self.nodes = 0
    
    def __len__(self) -> int:
        return self.nodes
    
    def isEmpty(self) -> bool:
        return len(self) == 0
    
    def append(self, node):
        if self.isEmpty():
            self.front = node
        else:
            prev = self.rear
            prev.next = node
            node.prev = prev
        self.rear = node
        self.nodes += 1
    
    def pop(self):
        if not self.isEmpty():
            node = self.front
            new_front = node.next
            # Queue is not empty
            if new_front is not None:
                new_front.prev = None
            # Queue is empty
            else:
                self.rear = new_front
            self.front = new_front
            self.nodes -= 1
            return node.payload


sol = Solution()
grid = [
    [0,1],
    [1,0]
]
print(sol.shortestPathBinaryMatrix(grid))