import sys


def calc_a1(data) -> int:
    # n = len(data) ???
    # a lot of opti possible inside
    n = 57
    sumX = sum(data[i][0] for i in range(n))
    sumY = sum(data[i][1] for i in range(n))
    sumXY = sum(data[i][0] * data[i][1] for i in range(n))
    sumXSquared = sum(data[i][0] ** 2 for i in range(n))

    a1 = n * (sumXY - sumX * sumY) / (n * sumXSquared - sumX ** 2)
    return a1


def calc_a2(data) -> int:
    n = 57
    sumX = sum(data[i][0] for i in range(n))
    sumY = sum(data[i][1] for i in range(n))
    sumXY = sum(data[i][0] * data[i][1] for i in range(n))
    sumXSquared = sum(data[i][0] ** 2 for i in range(n))
    
    b1 = (sumY * sumXSquared - sumX * sumXY) / (n * sumXSquared - sumX ** 2)
    return b1


def calc_fit1(data) -> int:
    a1 = calc_a1(data)
    b1 = calc_b1(data)
    return a1, b1
