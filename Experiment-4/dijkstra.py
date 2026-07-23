import heapq

def dijkstra(graph, source):
    distance = {v: float("inf") for v in graph}
    previous = {v: None for v in graph}

    distance[source] = 0
    pq = [(0, source)]

    while pq:
        dist, current = heapq.heappop(pq)

        if dist > distance[current]:
            continue

        for neighbor, weight in graph[current]:
            new_dist = dist + weight

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    return distance, previous


graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

dist, prev = dijkstra(graph, 0)

print("Shortest distances from source 0:")
for vertex in graph:
    print(f"0 -> {vertex} = {dist[vertex]}")
