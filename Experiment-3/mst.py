import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(vertices, edges):
    edges.sort()
    uf = UnionFind(vertices)

    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


def prim(vertices, graph, start=0):
    visited = [False] * vertices
    min_heap = [(0, start, -1)]

    mst = []
    total_cost = 0

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if visited[current]:
            continue

        visited[current] = True

        if parent != -1:
            mst.append((parent, current, weight))
            total_cost += weight

        for neighbor, w in graph[current]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (w, neighbor, current))

    return mst, total_cost


edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]

vertices = 7

graph = {i: [] for i in range(vertices)}

for weight, u, v in edges:
    graph[u].append((v, weight))
    graph[v].append((u, weight))


kruskal_mst, kruskal_cost = kruskal(vertices, edges.copy())

print("=== Kruskal's Algorithm ===")
for u, v, w in kruskal_mst:
    print(f"{u} - {v} : {w}")

print("Total Cost:", kruskal_cost)

print()

prim_mst, prim_cost = prim(vertices, graph)

print("=== Prim's Algorithm ===")
for u, v, w in prim_mst:
    print(f"{u} - {v} : {w}")

print("Total Cost:", prim_cost)
