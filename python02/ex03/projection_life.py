import matplotlib.pyplot as plt
import matplotlib.ticker as pltk
import load_csv as load
import pandas as pd

file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"


def parse_number(arg: pd.Series) -> pd.Series:
    def parse_value(x):
        if isinstance(x, str):
            x = x.replace('k', 'e3').replace('M', 'e6')
            return float(x)
        return float(x)
    return arg.apply(parse_value)


def projection_life() -> None:
    try:
        df_gdp = load.load(file)
        df_life = load.load("life_expectancy_years.csv")

        gdp_1900 = df_gdp[["country", "1900"]].copy()
        life_1900 = df_life[["country", "1900"]].copy()

        gdp_1900.rename(columns={"1900": "gdp_1900"}, inplace=True)
        life_1900.rename(columns={"1900": "life_1900"}, inplace=True)

        merged = gdp_1900.merge(life_1900, on="country")

        merged["gdp_1900"] = parse_number(merged["gdp_1900"])
        merged["life_1900"] = merged["life_1900"].astype(float)

        plt.scatter(merged["gdp_1900"], merged["life_1900"], alpha=0.7)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")

        plt.xscale("log")
        ax = plt.gca()
        ax.set_xticks([300, 1000, 10000])
        ax.get_xaxis().set_major_formatter(pltk.FuncFormatter(
            lambda x, _: f'{int(x/1000)}k' if x >= 1000 else f'{int(x)}'))
        plt.show()
    except Exception as err:
        print("Error ->", err)


if __name__ == "__main__":
    projection_life()
