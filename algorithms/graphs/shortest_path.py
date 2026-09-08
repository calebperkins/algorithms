import heapq


def shortest_path(
    n: int, edges: list[tuple[int, int, int]], src: int
) -> dict[int, int | None]:
    """Compute shortest distances from src to every node using Dijkstra's algorithm.

    Args:
        n: number of nodes, labeled 0..n-1.
        edges: list of (u, v, weight) directed edges.
        src: source node.

    Returns:
        Dict mapping each node to its shortest distance from src, or None if unreachable.
    """
    # the distance to the node from the source node, once known
    distances: dict[int, int] = {src: 0}

    # min-heap of (distance_from_src, node) candidates, popped in increasing distance order
    pq: list[tuple[int, int]] = [(0, src)]

    # preprocess graph - remove duplicate edges between u and v
    graph: dict[int, dict[int, int]] = {m: {} for m in range(n)}
    for u, v, w in edges:
        if v not in graph[u] or w < graph[u][v]:
            graph[u][v] = w

    while pq:
        # distance from src to u
        src_to_u_dist, u = heapq.heappop(pq)

        # nodes are only pushed to pq once they have a real distance
        u_dist = distances[u]

        # we already have recorded a shorter distance
        if src_to_u_dist > u_dist:
            continue

        for v, u_to_v_dist in graph[u].items():
            alt_dist = u_dist + u_to_v_dist
            v_dist = distances.get(v)
            if v_dist is None or alt_dist < v_dist:
                distances[v] = alt_dist
                heapq.heappush(pq, (alt_dist, v))

    # add in unreachable nodes as None
    return {m: distances.get(m) for m in range(n)}
