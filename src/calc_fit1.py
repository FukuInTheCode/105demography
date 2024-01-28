import sys
import math


def calc_a1(data) -> float:
    n = len(data)
    # a lot of opti possible inside
    sumX = sum(data[0][i] for i in range(n))
    sumY = sum(data[0][i] for i in range(n))
    sumXY = sum(data[0][i] * data[1][i] for i in range(n))
    sumXSquared = sum(data[0][i] ** 2 for i in range(n))

    a1 = n * (sumXY - sumX * sumY) / (n * sumXSquared - sumX ** 2)
    return a1


def calc_b1(data) -> float:
    n = len(data)
    sumX = sum(data[0][i] for i in range(n))
    sumY = sum(data[1][i] for i in range(n))
    sumXY = sum(data[0][i] * data[1][i] for i in range(n))
    sumXSquared = sum(data[0][i] ** 2 for i in range(n))

    b1 = (sumY * sumXSquared - sumX * sumXY) / (n * sumXSquared - sumX ** 2)
    return b1


def root_mean_square(data, a1, b1) -> float:
    n = len(data)
    values = [data[1][i] for i in range(n)]
    predic_rms = [a1 * data[0][i] + b1 for i in range(n)]
    rms = math.sqrt(sum((values[i] - predic_rms[i]) ** 2 for i in range(n)) / n)

    return rms


def predict(a1, b1) -> float:
    predi = a1 * 2050 + b1
    return predi


def calc_fit1(data) -> float:
    a1 = calc_a1(data)
    b1 = calc_b1(data)
    rms = root_mean_square(data, a1, b1)
    predic = predict(a1, b1)
    print("Fit1")
    print(f"\tY = {a1} X - {b1}")
    print(f"\tRoot-mean-square deviation: {rms}")
    print(f"\tPopulation in 2050: {predic}")

    return a1, b1
