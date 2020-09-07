"""Select only true matches"""

from wikidata_panglaodb.similarity import get_string_match
import pandas as pd
import numpy as np


def main():

    cells = pd.read_csv("results/all_matches/cells_reconciled.csv").dropna(
        subset=["id"]
    )
    organs = pd.read_csv("results/all_matches/organs_reconciled.csv").dropna(
        subset=["id"]
    )
    tissues = pd.read_csv(
        "results/all_matches/reconciled_tissues_germlayers.csv"
    ).dropna(subset=["id"])
    dfs = [cells, organs, tissues]

    for df in dfs:

        df["word_match"] = df.apply(
            lambda row: get_string_match(row["input_value"], row["name"]), axis=1
        )

        df["match"] = np.where((df["match"] | df["word_match"]), True, False)

        df.drop(["word_match"], axis=1, inplace=True)

        # Keep only true values
        df.drop(df[~df["match"]].index, inplace=True)

    cells.to_csv("results/true_matches/cells_raw.csv", index=False)
    organs.to_csv("results/true_matches/organs_raw.csv", index=False)
    tissues.to_csv("results/true_matches/tissues_raw.csv", index=False)


if __name__ == "__main__":
    main()
