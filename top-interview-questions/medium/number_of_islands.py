# Flood fill - Forest Fire Algorithm

from collections import deque

WATER = '0'
LAND = '1'


class Node:
    def __init__(self, x, y, terrain):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.visited = False

    def __repr__(self):
        return self.terrain

    
class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        self.nodes = []
        self.nb_islands = 0
        if grid:
            self.read_input(grid)
            self.explore()
        return self.nb_islands
        
    def read_input(self, grid):
        self.width = len(grid[0])
        self.height = len(grid)
        for x in range(self.width):
            row = []
            for y in range(self.height):
                node = Node(x, y, grid[y][x])
                row.append(node)
            self.nodes.append(row)
        
    def explore(self):
        for x in range(self.width):
            for y in range (self.height):
                self.explore_node(x, y)
                
    def explore_node(self, x, y):
        node = self.nodes[x][y]
        if node.terrain == WATER:
            return
        if node.visited:
            return
        self.flood_fill(node)
        self.nb_islands += 1
        
    def flood_fill(self, start):
        queue = deque()
        queue.append(start)
        
        while len(queue) != 0:
            current = queue.popleft()
            self.fill_neighbors(queue, current)
            
    def fill_neighbors(self, queue, node):
        if node.x + 1 < self.width:
            right_neighbor = self.nodes[node.x + 1][node.y]
            self.fill(queue, right_neighbor)
            
        if node.x > 0:
            left_neighbor = self.nodes[node.x - 1][node.y]
            self.fill(queue, left_neighbor)
            
        if node.y + 1 < self.height:
            down_neighbor = self.nodes[node.x][node.y + 1]
            self.fill(queue, down_neighbor)
            
        if node.y > 0:
            up_neighbor = self.nodes[node.x][node.y - 1]
            self.fill(queue, up_neighbor)
            
    def fill(self, queue, node):
        if node.terrain == LAND and not node.visited:
            node.visited = True
            queue.append(node)
