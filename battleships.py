from collections import defaultdict


def battleships(n: int, s: str, t: str) -> str:
    # SETUP A MAP OF LETTER : COLUMN MAPPING
    letter_col = {chr(ord('A') + i): i for i in range(26)}

    # TAG EACH BATTLESHIP PART TO ITS SHIP
    part_ship = dict()
    ship_parts = defaultdict(set)

    # KEEP A MAP OF {SHIP : [PART1, PART2...]} AND {PART : SHIP}
    for ship in s.split(','):
        tl, br = ship.split(' ')
        for i in range(int(tl[0:-1]), int(br[0:-1]) + 1):
            for j in range(ord(tl[-1]) - ord('A'), ord(br[-1]) - ord('A') + 1):
                part = f"{i}{chr(ord('A') + j)}"
                part_ship[part] = ship
                ship_parts[ship].add(part)

    # KEEP COUNT OF THE SUNK AND HIT SHIPS
    sunk = set()
    hit = set()

    # GO THROUGH EACH HITS
    for part_hit in t.split(" "):
        ship = part_ship.get(part_hit)
        if ship_parts.get(ship) is not None:
            ship_parts[ship].remove(part_hit)
            if len(ship_parts[ship]) == 0:
                sunk.add(ship)
                if ship in hit: hit.remove(ship)
            else:
                hit.add(ship)

    return f"{len(sunk)},{len(hit)}"


if __name__ == "__main__":
    print(battleships(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == "1,1")
    print(battleships(3, "1A 1B,2C 2C", "1B") == "0,1")
    print(battleships(12, '1A 2A,12A 12A', '12A') == "1,0")
