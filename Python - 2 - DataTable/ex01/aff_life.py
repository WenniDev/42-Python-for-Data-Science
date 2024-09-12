from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def main():
    data = load("/tmp/life_expectancy_years.csv")
    france_data = data[data["country"] == "France"]

    fig, ax = plt.subplots()

    ax.set_title("France Life expectancy Projections")

    ax.set_ylabel("Life expectancy")
    ax.set_xlabel("Year")

    ax.plot(list(france_data)[1:],
            list(france_data.values)[0][1:])

    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))

    plt.show()

    return 0


if (__name__ == "__main__"):
    main()
