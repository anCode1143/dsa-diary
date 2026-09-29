"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        adjList = {}
        def makeAdj(node):
            adjList[node] = []
            for neighbour in node.neighbors:
                adjList[node].append(neighbour)
                if neighbour not in adjList: 
                    makeAdj(neighbour)
        makeAdj(node)
        made = {}
        def makeNew(og):
            if og.val in made:
                return
            new = Node(val=og.val)
            made[og.val] = new
            for adj in adjList[og]:
                if not adj.val in made:
                    makeNew(adj)
                new.neighbors.append(made[adj.val])
        makeNew(node)
        return made[1]