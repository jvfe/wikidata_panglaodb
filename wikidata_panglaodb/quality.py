"""Item quality related functions"""

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict

sns.set(style="whitegrid", palette="muted")


def summarize_histology(dfs_list, total_list):
    """Return a summary table for item matches in the histology category
    
    Returns a summary table in the following structure:
        n_unique_matches is the number of uniquely named input values that matched
        perc_matched is the percentage of uniquely named input values that matched
        n_item_matches is the number of unique items they matched against, including duplicate concepts
        how_many_perfect_matches is the percentage of items matched that got
            a perfect 100.0 score in the reconciliation
        how_many_no_p31 is the percentage of items matched that don't have an 'instance of' property

    Args:
        dfs_list (list(DataFrame)): A dataframe list of the histology related reconciled tables 
            (cells, tissues and organs)
        total_list (list(int)): A list of the number of original input values.
    
    Returns:
        DataFrame: A summary table for the matches.
    """

    summary_table = pd.DataFrame(
        {
            "n_unique_matches": [df["input_value"].nunique() for df in dfs_list],
            "n_item_matches": [df["id"].nunique() for df in dfs_list],
            "n_perfect_matches": [len(df[df["score"] == 100.0]) for df in dfs_list],
            "n_no_p31": [len(df[df["type"] == "[]"]) for df in dfs_list],
            "totals": total_list,
        }
    )

    summary_table["perc_matched"] = (
        summary_table["n_unique_matches"] / summary_table["totals"]
    ) * 100
    summary_table["how_many_perfect_matches"] = (
        summary_table["n_perfect_matches"] / summary_table["n_item_matches"]
    ) * 100
    summary_table["how_many_no_p31"] = (
        summary_table["n_no_p31"] / summary_table["n_item_matches"]
    ) * 100

    summary_table.drop(
        ["n_no_p31", "n_perfect_matches", "totals"], axis=1, inplace=True
    )

    return summary_table


def plot_matched_item_types(reconciled_table, summary_table, data_type, ax):
    """Plot reconciled item types
    
    This will make a count table of item types, and plot it, for a defined entity type (data_type),
    it will take in the reconciled table itself, from where it will extract the counts,
    a summary table from where the totals can be acquired, the entity type being analysed 
    and an axis on a matplotlib figure.

    Args:
        reconciled_table (DataFrame): The table containing the reconciled items.
        summary_table (DataFrame): A summary table created by summarize_histology()
        data_type (str): The data type being analysed, "cells", "organs" or "tissues".
        ax (matplotlib.axes.Axes): A matplotlib figure axis to plot the final figure.
    
    Returns: 
        plot: A bar plot for the item type counts.
    """
    type_counts = (
        reconciled_table["type"]
        .value_counts()
        .reset_index()
        .replace("[]", "None")
        .rename(columns={"index": "Item type", "type": "# of items"})
    )

    type_counts["% of matched items"] = (
        type_counts["# of items"] / summary_table.loc[data_type, "n_item_matches"]
    ) * 100

    p = sns.barplot(
        x="Item type",
        y="% of matched items",
        data=type_counts,
        edgecolor="w",
        palette="magma",
        dodge=False,
        ax=ax,
    )
    p.set(xlabel=None)
    p.set_xticklabels(p.get_xticklabels(), rotation=45, horizontalalignment="right")

    return p


def get_number_of_statements_for_items(qid_list, has_property):
    """Return a pandas dataframe of items and their number of statements
    
    This function takes in a list of QIDs and uses the Wikibase API to return
    a table with the number of statements each item has.

    Args:
        qid_list (list): A list containing the QIDs you want to analyse.

    Returns:
        DataFrame: A dataframe of two columns, one for the input QIDs, another with 
            the number of statements for each QID.
    """

    # API limits to 50 items at once
    item_quality_dict = defaultdict(list)

    for i in range(0, len(qid_list), 50):

        curr_ids = qid_list[i : (i + 50)]

        params = {
            "action": "wbgetentities",
            "ids": "|".join(curr_ids),
            "format": "json",
        }

        resp = requests.post("https://www.wikidata.org/w/api.php", data=params)

        query_result = resp.json()["entities"]

        for item in query_result:
            properties = query_result[item]["claims"]
            if has_property in properties:
                item_quality_dict[item] = [len(properties.keys()), True]
            else:
                item_quality_dict[item] = [len(properties.keys()), False]

    item_quality_table = (
        pd.DataFrame.from_dict(
            item_quality_dict, columns=["n_statements", "has_property"], orient="index"
        )
        .rename_axis("id")
        .reset_index()
    )

    return item_quality_table

