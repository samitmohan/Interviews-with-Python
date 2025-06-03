# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/?envType=daily-question&envId=2025-05-27
def differenceOfSums(n: int, m: int) -> int:
    num1, num2 = [], []
    for i in range(1, n+1):
        if i % m == 0:
            num2.append(i)
        else:
            num1.append(i)
    return sum(num1) - sum(num2)

    

if __name__ == "__main__":
    print(differenceOfSums(n = 10, m = 3))
        