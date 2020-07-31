from typing import List


class TreeNode:
    def __init__(self, val, nb):
        self.val = val
        self.nb = nb
        self.total = 0
        self.nodes = 0


def max_avg_subtree(root: TreeNode) -> int:
    """
    Time  : O()
    Space : O(), where N = len(s)
    """

    # FOR EACH NODE, COUNT THE NUMBER OF CHILDREN IT HAS, AND ITS SUM
    count_nodes(root)
    count_total(root)

    # GO GET THE NODE WITH THE LARGEST AVG
    candidate = [root]
    get_largest_avg(root, candidate)
    return candidate[0].val


def count_nodes(root: TreeNode) -> int:
    if not root:
        return 0

    nodes = 0
    for nb in root.nb:
        nodes += 1 + count_nodes(nb)

    root.nodes = nodes
    # print(f"{root.val} has {root.children} children")
    return nodes


def count_total(root: TreeNode) -> int:
    if not root:
        return 0

    total = root.val
    for nb in root.nb:
        total += count_total(nb)

    root.total = total
    # print(f"{root.val} has {root.total} sum")
    return total


def get_largest_avg(root: TreeNode, candidate=List[TreeNode]):
    if not root or not root.nb:
        return

    curr_avg = root.total / root.nodes
    best_avg = candidate[0].total / candidate[0].nodes
    if curr_avg > best_avg:
        candidate[0] = root

    for nb in root.nb:
        get_largest_avg(nb, candidate)


if __name__ == "__main__":
    x3, x4, x5, x6, x7 = TreeNode(11, []), TreeNode(2, []), TreeNode(3, []), TreeNode(15, []), TreeNode(8, [])
    x1, x2 = TreeNode(12, [x3, x4, x5]), TreeNode(18, [x6, x7])
    x0 = TreeNode(20, [x1, x2])
    print(max_avg_subtree(x0) == 18)
