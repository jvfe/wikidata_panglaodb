import pandas as pd


def main():

    food = ["Q1409015", "Q494268"]
    plant_strucutures = ["Q1120914", "Q1293511", "Q148515"]
    chinese_medicine = [
        "Q6704255",
        "Q7543099",
        "Q6704252",
        "Q6704255",
        "Q6140833",
        "Q7578442",
        "Q6140977",
        "Q7618690",
        "Q5691852",
    ]
    misc = [
        "Q1120914",
        "Q1155702",
        "Q1475019",
        "Q1615371",
        "Q18816500",
        "Q2281500",
        "Q5173237",
        "Q5262664",
        "Q67208213",
        "Q719458",
        "Q7535317",
        "Q7840744",
        "Q85782674",
        "Q96377210",
        "Q97671426",
    ]

    false_matches = food + plant_strucutures + chinese_medicine + misc

    cells_raw = pd.read_csv("results/true_matches/cells_raw.csv")
    tissues_raw = pd.read_csv("results/true_matches/tissues_raw.csv")
    organs_raw = pd.read_csv("results/true_matches/organs_raw.csv")

    cells_clean = cells_raw[~cells_raw["id"].isin(false_matches)].drop_duplicates(
        subset=["id", "input_value"]
    )
    tissues_clean = tissues_raw[~tissues_raw["id"].isin(false_matches)].drop_duplicates(
        subset=["id", "input_value"]
    )
    organs_clean = organs_raw[~organs_raw["id"].isin(false_matches)].drop_duplicates(
        subset=["id", "input_value"]
    )

    cells_clean.to_csv("results/true_matches/cells_checked.csv", index=False)
    tissues_clean.to_csv("results/true_matches/tissues_checked.csv", index=False)
    organs_clean.to_csv("results/true_matches/organs_checked.csv", index=False)


if __name__ == "__main__":
    main()
