import matplotlib.pyplot as plt
import matplotlib.ticker as pltk
import load_csv as load


def parse_pop(arg):
    """Convert population values from strings with 'M' to floats.

    Args:
        arg (pd.Series): Series containing population
        values as strings (e.g., '20M').

    Returns:
        pd.Series: Series with population values as floats.
    """
    return arg.str.replace('M', '').astype(float)


def aff_pop() -> None:
    """Plot population projections for France and Belgium.

    Loads population data, processes values, and displays a line
    chart comparing both countries.

    Returns:
        None
    """
    try:
        df = load.load("population_total.csv")
        france_df = df[df["country"] == "France"]
        belgium_df = df[df["country"] == "Belgium"]

        france_values = parse_pop(france_df.drop(columns="country").iloc[0])
        belgium_values = parse_pop(belgium_df.drop(columns="country").iloc[0])

        years = df.columns[1:].astype(int)
        mask = (years >= 1800) & (years <= 2050)
        years = years[mask]
        france_values = france_values[mask]
        belgium_values = belgium_values[mask]

        plt.plot(years, belgium_values, label="Belgium", color="blue")
        plt.plot(years, france_values, label="France", color="green")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        ax = plt.gca()
        formatter = pltk.FuncFormatter(lambda x, _: f'{int(x)}M')
        ax.yaxis.set_major_formatter(formatter)
        ax.set_yticks([20, 40, 60])

        plt.xticks(range(1800, 2041, 40))

        plt.legend(loc="lower right")
        plt.show()
    except Exception as err:
        print("Error ->", err)


if __name__ == "__main__":
    aff_pop()
