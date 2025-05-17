import random


# Estimate pi given that you have random function which generates values b/w (0,1)


def estimate_pi(n):
    numPoint_circle = 0
    numPoint_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            numPoint_circle += 1
        numPoint_total += 1
    return 4 * numPoint_circle / numPoint_total


def main():
    # more points => more accurate
    print(estimate_pi(10))
    print(estimate_pi(1000))
    print(estimate_pi(100000000))


main()
