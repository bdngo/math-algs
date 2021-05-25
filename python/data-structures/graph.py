from __future__ import annotations
from typing import Any, Callable, List, Generic, TypeVar
from collections import deque

T = TypeVar('T')

class Graph(Generic[T]):
    """
    Class for a undirected graph.
    """
    def __init__(self, val: T, nodes: List[Graph]=[]):
        """
        docstring
        """
        self.val = val
        self.nodes = nodes

    def __repr__(self) -> str:
        return self.val

def dfs(start: Graph, visit: Callable[[Graph], Any]) -> List[Graph]:
    """
    Performs depth-first search on this graph with start node START.
    """
    fringe, marked = [], []
    fringe.append(start)
    while fringe != []:
        v = fringe.pop()
        if v not in marked:
            marked.append(v)
            visit(v)
            fringe.extend(i for i in v.nodes if i not in marked)
    return marked

def bfs(start: Graph, visit: Callable[[Graph], Any]) -> List[Graph]:
    """
    Performs breadth-first search on this graph with start node START.
    """
    fringe, marked = deque([]), []
    fringe.append(start)
    while fringe != []:
        v = fringe.pop()
        if v not in marked:
            marked.append(v)
            visit(v)
            fringe.extendleft(i for i in v.nodes if i not in marked)
    return marked
