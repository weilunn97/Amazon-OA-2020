def nth_gp(n2: float, n3: float, n: int) -> float:
    r = n3 / n2
    n1 = n2 / r
    return n1 * (r ** (n - 1))


if __name__ == "__main__":
    print(nth_gp(1, 2, 4) == 4.000)
    print(nth_gp(-4, -8, 5) == -32.000)
    print(nth_gp(-8, 4, 6) == -0.500)
