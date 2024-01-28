from src.parsing import get_data
from src.calc_fit_1 import calc_fit1
from src.calc_fit_2 import calc_fit2


def compute_all(abrs: list[str]) -> int:
    data = get_data(abrs)
    total = [[country[0] for country in data], [0 for _ in range(58)], [i for i in range(1960, 2018)]]

    for i in range(58):
        for country in data:
            total[1][i] += int(country[2 + i])
        total[1][i] /= 1e6
    total[0].sort()
    print("Country:", end="")
    for country in total[0]:
        print(f" {country}", end='')
        if country != total[0][-1]:
            print(",", end="")
    print()
    a1, b1 = calc_fit1(total[1:][::-1])
    a2, b2 = calc_fit2(total[1:])
    # calc_correlation(a1, b1, a2, b2)
    return 0
