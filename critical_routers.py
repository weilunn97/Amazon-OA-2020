from collections import defaultdict
from typing import List, Set


def critical_routers(num_nodes: int, num_edges: int, edges: List[List[int]]) -> Set[int]:
    """
    Time  : O()
    Space : O()
    """

    # CREATE THE GRAPH
    g = create_graph(edges)

    # SETUP THE ID AND LOW LINK FOR EACH NODE
    ids = [-1] * num_nodes
    low_links = [-1] * num_nodes
    critical = set()

    # START A DFS FROM NODE 0
    dfs(g, 0, -1, ids, low_links, critical, set())
    print(critical)
    print(ids)
    print(low_links)
    return critical


def dfs(g: dict, n: int, prev: int, ids: List[int], low_links: List[int], critical: Set[int], vis: Set[int]) -> None:
    # BASE CASE
    if n in vis:
        return

    # ID = LOW_LINK BY DEFAULT
    ids[n] = low_links[n] = len(vis)
    vis.add(n)

    # TRAVERSE EACH NEIGHBOUR
    for nb in g.get(n, []):

        # IF IT'S THE PREVIOUS NODE, IGNORE
        if nb == prev:
            continue

        # PERFORM A DFS
        dfs(g, nb, n, ids, low_links, critical, vis)

        # UPDATE MY LOW LINK
        low_links[n] = min(low_links[n], low_links[nb])

        print(f"ID({n}) = {ids[n]} | Low-Link({nb}) = {low_links[nb]}")
        # 1. FIRST, CHECK FOR EDGE COUNT > 1
        if len(g.get(n)) > 1:

            # A. CHECK FOR CRITICAL EDGE / BRIDGE - MY ID < NEIGHBOUR'S LOW LINK, OR...
            if ids[n] < low_links[nb]:
                critical.add(n)


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
    print(critical_routers(5, 4, [[0, 2], [1, 2], [2, 3], [2, 4]]) == {2})
