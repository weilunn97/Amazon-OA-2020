from typing import List


class DSNode:
    def __init__(self, val, parent=None, children=0):
        self.val = val
        self.parent = parent
        self.children = children


class DisjointSet:
    def __init__(self, n: int):
        self.nodes = {i: DSNode(i) for i in range(1, n + 1)}

    def find_root_parent(self, x: DSNode) -> bool:
        root_parent = x.parent
        while root_parent and root_parent.parent:
            x.children -= 1
            root_parent = root_parent.parent
        x.parent = root_parent
        return root_parent

    def union(self, x: int, y: int):
        x, y = self.nodes.get(x), self.nodes.get(y)
        root_x = self.find_root_parent(x) or x
        root_y = self.find_root_parent(y) or y

        # EDGE CASE : SAME GROUP
        if root_x == root_y:
            return False

        # CASE 1 : X BECOMES PARENT, Y LOSES ALL ITS CHILDREN
        if root_x.children >= root_y.children:
            root_x.children += 1 + root_y.children
            root_y.children = 0
            root_y.parent = root_x

        # CASE 2 : Y BECOMES PARENT, X LOSES ALL ITS CHILDREN
        else:
            root_y.children += 1 + root_x.children
            root_x.children = 0
            root_x.parent = root_y

        return True


def min_cost_connection(n: int, edges: List[List[int]], new_edges: List[List[int]]) -> int:
    """
    Time  : O()
    Space : O(), where N = len(s)
    """
    # SORT THE EDGES BY WEIGHT
    new_edges = sorted(new_edges, key=lambda e: e[-1])

    # TRACK THE COST
    cost = 0
    ds = DisjointSet(n)

    # ADD THE EXISTING GRAPH FIRST
    for u, v in edges:
        ds.union(u, v)

    # TRY PLACING IT
    for u, v, c in new_edges:
        if ds.union(u, v):
            cost += c

    return cost


if __name__ == "__main__":
    print(min_cost_connection(6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]) == 7)
