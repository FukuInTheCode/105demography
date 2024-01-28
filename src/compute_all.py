from src.parsing import get_data


def compute_all(abrs: list[str]) -> int:
    data = get_data(abrs)
    total = [[country[0] for country in data], [0 for _ in range(57)]]

    for i in range(57):
        for country in data:
            total[1][i] += int(country[1 + i])
    total[0].sort()
    print("Country:")
    for country in total[0]:
        print(f" {country}", end='')
        if (country != total[0][-1])
            print(",", end='')
    # a1, b1 = calc_fit1(total[1])
    # a2, b2 = calc_fit2(total[1])
    # calc_correlation(a1, b1, a2, b2)
    return 0
