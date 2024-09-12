from load_csv import load
from matplotlib import pyplot as plt


def main():

    income_data = load('/tmp/income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_data = load('/tmp/life_expectancy_years.csv')

    life_expectancy_in_1900 = list(life_data["1900"])
    income_per_person_in_1900 = list(income_data["1900"])

    fig, ax = plt.subplots()

    ax.set_title("1900")

    ax.set_ylabel("Life expectancy")
    ax.set_xlabel("Gross domestic product")

    ax.set_xscale('log')
    ax.set_xticks([300, 1000, 10000], ["300", "1k", "10k"])
    ax.scatter(income_per_person_in_1900, life_expectancy_in_1900)

    plt.show()

    return 0


if __name__ == '__main__':
    main()
