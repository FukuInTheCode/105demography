import sys
import math


def calc_a1(data) -> float:
    # n = len(data) ???
    # a lot of opti possible inside
    n = 57
    sumX = sum(data[i][0] for i in range(n))
    sumY = sum(data[i][1] for i in range(n))
    sumXY = sum(data[i][0] * data[i][1] for i in range(n))
    sumXSquared = sum(data[i][0] ** 2 for i in range(n))

    a1 = n * (sumXY - sumX * sumY) / (n * sumXSquared - sumX ** 2)
    return a1


def calc_b1(data) -> float:
    n = 57
    sumX = sum(data[i][0] for i in range(n))
    sumY = sum(data[i][1] for i in range(n))
    sumXY = sum(data[i][0] * data[i][1] for i in range(n))
    sumXSquared = sum(data[i][0] ** 2 for i in range(n))

    b1 = (sumY * sumXSquared - sumX * sumXY) / (n * sumXSquared - sumX ** 2)
    return b1


def root_mean_square(data, a1, b1) -> float:
    n = 57
    values = [data[i][1] for i in range(n)]
    predic = [a1 * data[i][0] + b1 for i in range(n)]
    rms = math.sqrt(sum((values[i] - predic[i]) ** 2 for i in range(n)) / n)

    return rms


def calc_fit1(data) -> int:
    a1 = calc_a1(data)
    b1 = calc_b1(data)
    rms = root_mean_square(data, a1, b1)
    print("Fit1")
    print(f"\tY = {a1} X - {b1}")
    print(f"\tRoot-mean-square deviation: {rms}")
    print(f"\tPopulation in 2050: ")
    
    return a1, b1
