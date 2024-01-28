import sys


def calc_fit1(data) -> int:
    # n = len(data) ???
    n = 57
    sumX = sum(data[i][0] for i in range(n))
    sumY = sum(data[i][1] for i in range(n))
    sumXY = sum(data[i][0] * data[i][1] for i in range(n))
    sumXSquared = sum(data[i][0] ** 2 for i in range(n))

    a1 = n * (sumXY - sumX * sumY) / (n * sumXSquared - sumX ** 2)
    b1 = 0
    return a1, b1