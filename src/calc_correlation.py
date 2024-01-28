from math import sqrt


def calc_correlation(data, a1, b1) -> None:
    predicts = [a1 * year + b1 for year in data[0]]
    mean_tot = sum(data[1]) / len(data[1])
    mean_pre = sum(predicts) / len(predicts)
    num = ((observed - mean_tot) * (predicted - mean_pre) for observed, predicted in zip(data[1], predicts))
    deno_obs = sum((observed - mean_tot) ** 2 for observed in data[1])
    deno_pre = sum((predicted - mean_pre) ** 2 for predicted in predicts)
    print("Correlation: {:.4f}".format(num / (sqrt(deno_obs) * sqrt(deno_pre))))
