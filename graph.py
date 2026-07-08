# Graph — Depth-First Search (DFS) and Breadth-First Search (BFS)
#
# The graph is represented as an adjacency list: a dict mapping each vertex
# to a list of its neighbours. This costs O(V + E) space, which is more
# efficient than an adjacency matrix (O(V²)) when the graph is sparse.
# Supports both directed and undirected graphs via the `directed` flag.
#
# -------------------------------------------------------------------------
# DFS — Recursive Pseudocode (this implementation):
#   DFS(G, s):
#   1. mark s as visited
#   2. for each neighbour w of s
#   3.     if w not visited
#   4.         DFS(G, w)
#
# DFS — Iterative Pseudocode (see dfs_iterative below):
#   DFS-Iterative(G, s):
#   1.  let S be a stack containing just s
#   2.  let visited = empty set
#   3.  while S is not empty
#   4.      pop v from top of S
#   5.      if v not in visited
#   6.          mark v as visited
#   7.          for each neighbour w of v
#   8.              if w not in visited
#   9.                  push w onto S
#
# How DFS works:
#   DFS explores as far down one branch as possible before backtracking.
#   The recursive version uses the call stack implicitly — each call goes
#   one level deeper, and returning from a call is the backtrack. The
#   iterative version does the same thing with an explicit stack (LIFO),
#   but because neighbours are pushed in forward order and then popped in
#   reverse, it may visit them in a different order than the recursive version.
#
# -------------------------------------------------------------------------
# BFS Pseudocode:
#   BFS(G, s):
#   1.  let Q be a queue containing just s
#   2.  let visited = {s}
#   3.  while Q is not empty
#   4.      dequeue v from front of Q
#   5.      for each neighbour w of v
#   6.          if w not in visited
#   7.              mark w as visited
#   8.              enqueue w to back of Q
#
# How BFS works:
#   BFS explores all vertices at distance 1 from the start before moving
#   to distance 2, then distance 3, and so on — level by level. Using a
#   queue (FIFO) enforces this: a vertex's neighbours are all enqueued
#   before any of those neighbours' neighbours get a turn. This guarantees
#   BFS finds the shortest path (fewest edges) in an unweighted graph.
#   Notice that BFS marks a vertex visited when it is *enqueued*, not when
#   it is dequeued — this prevents the same vertex being added to the queue
#   multiple times by different neighbours.
#
# -------------------------------------------------------------------------
# Time Complexity (both DFS and BFS): O(V + E)
#   Every vertex is processed once — O(V).
#   Every edge is examined once (twice for undirected) — O(E).
#
# Space Complexity: O(V)
#   visited set:        O(V)
#   traversal_order:    O(V)
#   DFS recursive:      O(V) for the implicit call stack (worst case: a
#                       linear chain where every call is still on the stack)
#   DFS iterative:      O(V) for the explicit stack
#   BFS:                O(V) for the queue (worst case: all neighbours of
#                       the start vertex are enqueued at once)


from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed  # False = undirected (edges go both ways)

    def add_vertex(self, vertex):
        # Add an isolated vertex (no edges yet); ignore if it already exists
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        # Auto-create either vertex if it doesn't exist yet
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        if not self.directed:
            self.adj_list[v2].append(v1)  # Undirected — add the return path too

    def dfs(self, start_vertex):
        # Recursive DFS — returns vertices in the order they were first visited
        if start_vertex not in self.adj_list:
            return []
        visited = set()
        traversal_order = []

        def _dfs_recursive(node):
            visited.add(node)
            traversal_order.append(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)  # Go deeper before trying next neighbour

        _dfs_recursive(start_vertex)
        return traversal_order

    def dfs_iterative(self, start_vertex):
        # Iterative DFS using an explicit stack — same depth-first behaviour
        # as the recursive version but avoids Python's recursion limit on very
        # deep graphs. Neighbours may be visited in a different order because
        # the stack pops the last-pushed neighbour first (LIFO).
        if start_vertex not in self.adj_list:
            return []
        stack = [start_vertex]
        visited = set()
        traversal_order = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:       # Node may have been pushed multiple times
                visited.add(vertex)
                traversal_order.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal_order

    def bfs(self, start_vertex):
        # BFS using a deque — returns vertices level by level from start_vertex
        if start_vertex not in self.adj_list:
            return []
        queue = deque([start_vertex])
        visited = set([start_vertex])  # Mark on enqueue, not on dequeue
        traversal_order = []

        while queue:
            current_node = queue.popleft()
            traversal_order.append(current_node)
            for neighbor in self.adj_list[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)       # Mark before enqueuing to prevent duplicates
                    queue.append(neighbor)

        return traversal_order


# Sanity check
#
#     1
#    / \
#   2   3
#    \ /
#     4
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print(g.dfs(1))           # [1, 2, 4, 3]  — goes deep on the 2→4 branch first
print(g.dfs_iterative(1)) # [1, 3, 4, 2]  — same depth-first, reversed neighbour order
print(g.bfs(1))           # [1, 2, 3, 4]  — level by level
