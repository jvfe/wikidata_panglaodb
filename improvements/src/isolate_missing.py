"""Isolate data from PanglaoDB that's missing from Wikidata"""

# %%
from wikidata_panglaodb.pre import get_negative_intersection
from collections import defaultdict
import pandas as pd


def main():

    original_data = "../../analysis/data/panglaodb/"
    results_path = "../../analysis/results/true_matches/"

    original_cells_organs = pd.read_csv(f"{original_data}cells_organs_germlayers.csv")
    original_tissues = pd.read_csv(f"{original_data}tissues.csv")

    matched_cells = pd.read_csv(f"{results_path}cells_checked.csv")
    matched_organs = pd.read_csv(f"{results_path}organs_checked.csv")
    matched_tissues = pd.read_csv(f"{results_path}tissues_checked.csv")

    matches_to_be_made = {
        "cells": [matched_cells, original_cells_organs],
        "organs": [matched_organs, original_cells_organs],
        "tissues": [matched_tissues, original_tissues],
    }
    keys_for_merging = ["cell_type", "organ", "tissue"]

    missing_results = defaultdict()
    for dataframe, key in zip(matches_to_be_made.keys(), keys_for_merging):

        data_missing = get_negative_intersection(
            left_df=matches_to_be_made[dataframe][0],
            right_df=matches_to_be_made[dataframe][1],
            left_on="input_value",
            right_on=key,
        )

        missing_results[dataframe] = data_missing


if __name__ == "__main__":
    main()
