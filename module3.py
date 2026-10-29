import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

data = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")
data["BMI"] = data["Weight"] / data["Height"] ** 2

_pink = "fuchsia"
_size = (9, 6)


def _avgweightline():
    avg_weight = data.groupby(data["Age"].round())["Weight"].mean()
    plt.figure(figsize=_size)
    plt.plot(avg_weight.index, avg_weight.values, color=_pink, marker="o")
    plt.title("Average weight at each age")
    plt.xlabel("Age (years)")
    plt.ylabel("Average weight (kg)")
    plt.tight_layout()
    plt.savefig("avg_weight_by_age.png")
    plt.show()


def _heightweightscatter():
    plt.figure(figsize=_size)
    sns.scatterplot(
        data=data,
        x="Height",
        y="Weight",
        hue="Gender",
        palette={"Female": _pink, "Male": "darkslateblue"},
        alpha=0.5,
    )
    plt.title("Taller participants tend to weigh more")
    plt.xlabel("Height (m)")
    plt.ylabel("Weight (kg)")
    plt.tight_layout()
    plt.savefig("height_vs_weight.png")
    plt.show()


def _agehistogram():
    plt.figure(figsize=_size)
    sns.histplot(data=data, x="Age", bins=30, kde=True, color=_pink)
    plt.title("Most participants are in their early 20s")
    plt.xlabel("Age (years)")
    plt.ylabel("Number of participants")
    plt.tight_layout()
    plt.savefig("age_histogram.png")
    plt.show()


def _transportbox():
    plt.figure(figsize=_size)
    sns.boxplot(data=data, x="MTRANS", y="Weight", color=_pink)
    plt.title("Weight by main mode of transport")
    plt.xlabel("Transport")
    plt.ylabel("Weight (kg)")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig("weight_by_transport.png")
    plt.show()


def _bmibox():
    plt.figure(figsize=_size)
    sns.boxplot(data=data, x="NObeyesdad", y="BMI", color=_pink,
            order=["Insufficient_Weight", "Normal_Weight",
                   "Overweight_Level_I", "Overweight_Level_II",
                   "Obesity_Type_I", "Obesity_Type_II", "Obesity_Type_III"])
    plt.title("BMI at each obesity level")
    plt.xlabel("Obesity level")
    plt.ylabel("BMI")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("bmi_by_obesity_level.png")
    plt.show()


if __name__ == "__main__":
    _avgweightline()
    _heightweightscatter()
    _agehistogram()
    _transportbox()
    _bmibox()
