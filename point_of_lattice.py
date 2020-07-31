def point_of_lattice(ax: int, ay: int, bx: int, by: int) -> str:
    # EDGE CASE - HORIZONTAL / VERTICAL LINE - YOU'LL ALWAYS END UP AT B
    if ax == bx or ay == by:
        return f"{bx},{by}"

    # GET THE GRADIENT OF AB
    grad = (by - ay) / (bx - ax)

    # GET THE GRADIENT AND INTERCEPT OF THE LINE PERPENDICULAR TO AB
    new_grad = -1 / grad
    new_intercept = by - new_grad * bx

    # CASE 1 - A LIES TO THE LEFT OF B - Y WILL ALWAYS DECREASE AFTER RIGHT TURN AT B
    # CASE 2 - A LIES TO THE RIGHT OF B - Y WILL ALWAYS INCREASE AFTER RIGHT TURN AT B
    new_x, new_y = bx, by
    while True:
        new_y += 1 if ax > bx else -1
        new_x = (new_y - new_intercept) / new_grad
        if int(new_x) == new_x and int(new_y) == new_y: break
    return f"{int(new_x)},{int(new_y)}"


if __name__ == "__main__":
    print(point_of_lattice(-1, 3, 3, 1) == "2,-1")
    print(point_of_lattice(-1, 3, -1, 1) == "-1,1")
