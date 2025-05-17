# O(n) -> O(logn)

import time


def naiveexp(base, p):
    res = 1
    for _ in range(p):
        res *= base
    return res


def fastexp(base, p):
    if p == 0:
        return 1
    if p == 1:
        return base
    else:
        r = fastexp(base, p // 2)
        if p % 2 == 0:
            return r * r  # even
        else:
            return r * base * r  # odd


if __name__ == "__main__":
    powers_to_test = [
        10,
        100,
        1_000,
        10_000,
        50_000,
        100_000,
        200_000,
        300_000,
        400_000,
        500_000,
    ]
    base = 2

    print("power\tnaive_time (s)\tfast_time (s)")
    for p in powers_to_test:
        start = time.time()
        try:
            naiveexp(base, p)
        except:
            pass
        naive_time = time.time() - start

        start = time.time()
        fastexp(base, p)
        fast_time = time.time() - start

        print(f"{p}\t{naive_time:.6f}\t\t{fast_time:.6f}")

"""
Results-:
power   naive_time (s)  fast_time (s)
10      0.000002                0.000002
100     0.000004                0.000002
1000    0.000059                0.000003
10000   0.003455                0.000020
50000   0.074514                0.000131
100000  0.299399                0.000324
200000  1.189026                0.000584
300000  2.611735                0.000747
400000  4.584180                0.001149
500000  7.204963                0.001910

Iterative
def fast_exp_iter(base, power):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= base
        base *= base
        power //= 2
    return result
"""
