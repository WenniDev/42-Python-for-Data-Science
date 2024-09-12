#!/usr/bin/env python

from load_csv import load
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def intify(array: list) -> list:
    """Convert an array of strings (formatted like '10M', '10k')\
to an array of integers."""
    def get_value(num: str, order: str) -> int:
        """Return the value of a number depending of his order."""
        match order:
            case 'M':
                value = float(num) * 10**6
            case 'K':
                value = float(num) * 10**3
            case _:
                value = float(num)
        return int(value)

    return [get_value(value[:-1], value[-1:]) for value in array]


def main():
    data = load('/tmp/population_total.csv')
    france_data = data[data['country'] == 'France']
    user_data = data[data['country'] == 'Belgium']

    fig, ax = plt.subplots()

    ax.plot(list(user_data)[1:(2050-1800)],
            intify(list(user_data.values)[0][1:(2050-1800)]))
    ax.plot(list(france_data)[1:(2050-1800)],
            intify(list(france_data.values)[0][1:(2050-1800)]), 'green')

    ax.set_xlabel('Year')
    ax.set_ylabel('Population')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))

    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{x/10**6:.0f}M'))
    ax.set_yticks(
        intify(["0M", "20M", "40M", "60M"]), ["", "20M", "40M", "60M"])

    ax.legend(['Belgium', 'France'], loc='lower right')
    ax.set_title('Population Projections')
    plt.show()


if __name__ == '__main__':
    main()
