'''
Question: Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Create vertices array
        vertices = self.createGraph(grid)
        islands = 0

        for i in range(len(vertices)):
            vertex = vertices[i]
            # Check if vertex is a land and not yet visited
            if vertex.val == 1 and not vertex.visited:
                islands += 1
                # Perform dfs on all its connecting land vertices
                self.dfs(vertex)

        return islands

    def dfs(self, u):
        u.visited = True
        discovered = Stack()
        for v in u.edges:
            discovered.push(v)

        while not discovered.isEmpty():
            u = discovered.pop()
            u.visited = True
            for v in u.edges:
                if not v.visited:
                    discovered.push(v)

    def createGraph(self, grid: List[List[str]]):
        vertices = []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                id = n * i + j
                val = int(grid[i][j])
                vertex = Vertex(id, val)
                vertices.append(vertex)

        for i in range(m):
            for j in range(n):
                id = n * i + j
                u = vertices[id]
                adjacent = [(i - 1, j), (i + 1, j),
                            (i, j - 1), (i, j + 1)]
                for k in range(len(adjacent)):
                    coord = adjacent[k]
                    if 0 <= coord[0] <= (m - 1) and 0 <= coord[1] <= (n - 1):
                        vertex_id = n * coord[0] + coord[1]
                        v = vertices[vertex_id]
                        u.edges.append(v)

        return vertices


class Vertex:
    def __init__(self, id, val):
        self.id = id
        self.val = val
        self.edges = []
        self.visited = False


class Stack:
    def __init__(self):
        self.rear = None
        self.nodes = 0

    def __len__(self):
        return self.nodes

    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        node = self.Node(item)
        prev = self.rear
        if prev is not None:
            prev.next = node
        node.prev = prev
        self.rear = node
        self.nodes += 1

    def pop(self):
        if not self.isEmpty():
            item = self.rear.payload
            new_rear = self.rear.prev
            if new_rear is not None:
                new_rear.next = None
            self.rear = new_rear
            self.nodes -= 1
            return item

    class Node:
        def __init__(self, payload, prev=None, next=None):
            self.payload = payload
            self.prev = prev
            self.next = next


sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(sol.numIslands(grid))
