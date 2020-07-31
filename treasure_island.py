from typing import List


def treasure_island(grid: List[List[str]]) -> int:
    """
    Time  : O(MN)
    Space : O(MN), where M = len(grid), and N = len(grid[0])
    """
    vis = set()
    curr_level = [(0, 0)]
    steps = 0

    while curr_level:

        # SETUP A QUEUE OF NEXT LEVEL NODES TO EXPLORE
        next_level = []

        for i, j in curr_level:

            # CHECK IF VISITED
            if f"{i},{j}" not in vis:

                # ADD TO VISITED
                vis.add(f"{i},{j}")

                # TARGET FOUND
                if grid[i][j] == 'X':
                    return steps

                # EXPAND IN ALL 4 DIRECTIONS
                expand(grid, i - 1, j, next_level)
                expand(grid, i + 1, j, next_level)
                expand(grid, i, j - 1, next_level)
                expand(grid, i, j + 1, next_level)

        # PROCEED TO NEXT LEVEL
        curr_level = next_level
        steps += 1

    return -1


def expand(grid, i, j, next_level):
    if min(i, j) < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 'D':
        return

    next_level.append((i, j))


if __name__ == "__main__":
    print(treasure_island([['O', 'O', 'O', 'O'],
                           ['D', 'O', 'D', 'O'],
                           ['O', 'O', 'O', 'O'],
                           ['X', 'D', 'D', 'O']]) == 5)

    print(treasure_island([['O', 'D', 'O', 'O'],
                           ['D', 'O', 'D', 'O'],
                           ['O', 'O', 'O', 'O'],
                           ['X', 'D', 'D', 'O']]) == -1)

    print(treasure_island([['O', 'O', 'O', 'O'],
                           ['D', 'O', 'D', 'O'],
                           ['O', 'O', 'X', 'O'],
                           ['O', 'D', 'D', 'O']]) == 4)

    print(treasure_island([['O', 'O', 'O', 'O'],
                           ['D', 'D', 'D', 'O'],
                           ['O', 'X', 'D', 'O'],
                           ['O', 'O', 'O', 'O']]) == 9)

    print(treasure_island([['O', 'D', 'O', 'O'],
                           ['O', 'O', 'O', 'O'],
                           ['O', 'O', 'O', 'O'],
                           ['O', 'O', 'O', 'X']]) == 6)
