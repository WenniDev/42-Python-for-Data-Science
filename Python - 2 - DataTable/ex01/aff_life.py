from matplotlib import pyplot as plt
from load_csv import load


def main():

    data = load("/tmp/life_expectancy_years.csv").transpose()
    plt.plot(data, data['Life expectancy (years)'])

    plt.show()

    return 0


if (__name__ == "__main__"):
    main()
