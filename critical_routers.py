from collections import defaultdict
from typing import List


def critical_routers(num_nodes: int, num_edges: int, edges: List[List[int]]) -> List[int]:
    """
    Time  : O()
    Space : O()
    """

    # CREATE THE GRAPH
    g = create_graph(edges)

    # DFS FROM NODE 0
    node = 0
    prev = -1
    vis = set()
    rank = [0] * num_nodes
    lowest_rank = [0] * num_nodes
    critical = set()
    dfs(g, node, prev, vis, rank, lowest_rank, critical)
    return critical


def dfs(g: dict, node: int, prev: int, vis: set, rank: List[int], lowest_rank: List[int], critical: set) -> None:
    if node in vis:
        return

    vis.add(node)
    rank[node] = len(vis)
    lowest_rank[node] = len(vis)

    for nb in g.get(node, []):
        if nb == prev:
            continue
        dfs(g, nb, node, vis, rank, lowest_rank, critical)
        lowest_rank[node] = min(lowest_rank[node], lowest_rank[nb])
        if lowest_rank[nb] > rank[node]:
            if len(g.get(node)) > 1: critical.add(node)
            if len(g.get(nb)) > 1: critical.add(nb)


def create_graph(edges: List[List[int]]) -> dict:
    g = defaultdict(list)
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    return g


if __name__ == "__main__":
    print(critical_routers(7, 7, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]) == {2, 3, 5})
    print(critical_routers(6, 4, [[0, 3], [1, 2], [1, 4], [1, 5], [2, 3]]) == {1, 2, 3})
    print(critical_routers(6, 4, [[0, 1], [0, 2], [1, 2]]) == set())
