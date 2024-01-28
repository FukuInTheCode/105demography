from src.parsing import get_data


def compute_all(abrs: list[str]) -> int:
    # data = get_data(abrs)
    total = [[country[0] for country in data], [0 for _ in range(57)]]

    print(total)
    # for i in range(57):
    # for country in data:
    # total[1][i] += int(country[1 + i])
    return 0
