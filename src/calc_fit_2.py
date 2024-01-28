import sys
import math


def calc_a2(data) -> float:
    n = len(data[0])
    sumX = sum(data[0][i] for i in range(n))
    sumY = sum(data[1][i] for i in range(n))
    sumXY = sum(data[0][i] * data[1][i] for i in range(n))
    sumXSquared = sum(data[0][i] ** 2 for i in range(n))

    a2 = ((n * sumXY) - sumX * sumY) / ((n * sumXSquared) - sumX ** 2)
    return a2


def calc_b2(data, a2) -> float:
    n = len(data[0])
    sumX = sum(data[0][i] for i in range(n))
    sumY = sum(data[1][i] for i in range(n))
    sumXY = sum(data[0][i] * data[1][i] for i in range(n))
    sumXSquared = sum(data[0][i] ** 2 for i in range(n))

    b2 = (sumY * sumXSquared - sumX * sumXY) / (n * sumXSquared - sumX ** 2)
    return b2


def root_mean_square2(data, a2, b2) -> float:
    n = len(data[0])
    values = [data[1][i] for i in range(n)]
    predic_rms = [((values[i] - b2) / a2) for i in range(n)]
    rms = math.sqrt(sum((data[0][i] - predic_rms[i]) ** 2 for i in range(n)) / n)

    return rms


def predict2(data, a2, b2) -> float:
    predi = (2050 - b2) / a2
    return predi


def calc_fit2(data) -> None:
    a2 = calc_a2(data)
    b2 = calc_b2(data, a2)
    rms = root_mean_square2(data, a2, b2)
    predic = predict2(data, a2, b2)
    print("Fit2")
    print("   X = {:.2f} Y {} {:.2f}".format(a2, "-" if b2 < 0 else "+", b2))
    print("   Root-mean-square deviation: {:.2f}".format(rms))
    print("   Population in 2050: {:.2f}".format(predic))

    return
