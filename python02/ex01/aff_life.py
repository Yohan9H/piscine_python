import matplotlib.pyplot as plt
import load_csv as load


def aff_life() -> None:
    try:
        df = load.load("life_expectancy_years.csv")
        france_df = df[df["country"] == "France"]
        france_values = france_df.drop(columns="country").values.flatten()
        years = df.columns[1:].astype(int)
        plt.plot(years, france_values)
        plt.title("France Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(range(1800, 2101, 40))
        plt.show()
    except Exception as err:
        print("Error ->", err)


if __name__ == "__main__":
    aff_life()
