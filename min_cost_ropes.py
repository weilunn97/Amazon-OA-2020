from heapq import heappush, heappop, heapify
from typing import List


def min_cost_ropes(ropes: List[int]) -> int:
    """
    Time  : O()
    Space : O()
    """

    # PLACE THEM INTO A MIN HEAP
    heapify(ropes)

    # TRACK THE COST
    cost = 0

    # LOOP TILL ONLY 1 ROPE LEFT
    while len(ropes) > 1:
        r1, r2 = heappop(ropes), heappop(ropes)
        cost += r1 + r2
        heappush(ropes, r1 + r2)

    return cost


if __name__ == "__main__":
    print(min_cost_ropes([8, 4, 6, 12]) == 58)
    print(min_cost_ropes([20, 4, 8, 2]) == 54)
    print(min_cost_ropes([1, 2, 5, 10, 35, 89]) == 224)
    print(min_cost_ropes([2, 2, 3, 3]) == 20)
