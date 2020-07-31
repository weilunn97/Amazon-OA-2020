from typing import List


def optimal_utilization(a: List[List[int]], b: List[List[int]], tgt: int) -> List[List[int]]:
    """
    Time  : O()
    Space : O()
    """
    # SORT A AND B BY THEIR VALUES
    a = sorted(a, key=lambda e: e[1])
    b = sorted(b, key=lambda e: e[1])

    # SETUP THE RESULTS
    res = []
    closest = None

    # SETUP 2 POINTERS
    pa, pb = 0, len(b) - 1

    while pa < len(a) and pb > -1:

        # CASE 1 : SUM <= TARGET
        if a[pa][1] + b[pb][1] <= tgt:

            # A. WE FIND A SUM THAT IS EVEN CLOSER TO TARGET
            if not closest or closest < a[pa][1] + b[pb][1]:
                closest = a[pa][1] + b[pb][1]
                res = [a[pa], b[pb]]

            # B. WE FIND A SUM THAT IS EQUAL TO THE CLOSEST
            elif closest == a[pa][1] + b[pb][1]:
                res.extend([a[pa], b[pb]])

            # ADVANCE POINTER ON A AND SEE IF WE CAN GET EVEN CLOSER
            pa += 1

        # CASE 2 : SUM > TARGET
        else:

            # REVERSE POINTER ON B AND SEE IF WE CAN GO BELOW THE TARGET SUM
            pb -= 1

    return [[res[i][0], res[i + 1][0]] for i in range(0, len(res) - 1, 2)]


if __name__ == "__main__":
    print(optimal_utilization([[1, 2], [2, 4], [3, 6]],
                              [[1, 2]],
                              7) == [[2, 1]])

    print(optimal_utilization([[1, 3], [2, 5], [3, 7], [4, 10]],
                              [[1, 2], [2, 3], [3, 4], [4, 5]],
                              10) == [[2, 4], [3, 2]])

    print(optimal_utilization([[1, 8], [2, 7], [3, 14]],
                              [[1, 5], [2, 10], [3, 14]],
                              20) == [[3, 1]])

    print(optimal_utilization([[1, 8], [2, 15], [3, 9]],
                              [[1, 8], [2, 11], [3, 12]],
                              20) == [[1, 3], [3, 2]])
