"""Item quality related functions"""

import requests
import pandas as pd
import numpy as np
from collections import defaultdict


def summarize_matches(dfs_list, total_list):
    """Return a simple summary table for item matches regardless of category
    
    Returns a summary table in the following structure:
        n_unique_matches is the number of uniquely named input values that matched
        perc_matched is the percentage of uniquely named input values that matched
        n_item_matches is the number of unique items they matched against, including duplicate concepts
        

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
            "totals": total_list,
        }
    )

    summary_table["perc_matched"] = (
        summary_table["n_unique_matches"] / summary_table["totals"]
    ) * 100

    return summary_table


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

    summary_table = summarize_matches(dfs_list, total_list)

    summary_table["n_perfect_matches"] = [
        len(df[df["score"] == 100.0]) for df in dfs_list
    ]
    summary_table["n_no_p31"] = [len(df[df["type"] == "[]"]) for df in dfs_list]

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


def get_genes_item_quality(df, drop=True):
    """Changes ID columns to binary values

    Changes the alternative id columns in the reconciled gene data to binary values,
    also drops unecessary columns if drop == True.

    Args:
        df (DataFrame): Reconciled gene data.
        drop (bool): Wether or not to drop the other columns.

    Returns:
        DataFrame: Simplified dataframe for plotting.
         
    """

    result_df = df.copy().rename(columns={"item": "id"})

    result_df["has_ensg"] = np.where(result_df["ensg_wdt"].isna(), False, True)
    result_df["has_entrez"] = np.where(result_df["entrez"].isna(), False, True)

    if drop == True:
        result_df.drop(
            ["itemLabel", "entrez", "ensg_wdt", "ensg_panglao"], axis=1, inplace=True
        )

    return result_df


def aggregate_altID_data(dataframe, group):
    """Summarize alternative IDs for final bar plot
    
    Args:
        dataframe (DataFrame): With either the histological or gene data.
        group (list): Columns to use for the groupby.
    
    Returns:
        DataFrame: Summarized counts and percentages.
    """
    aggregated = (
        dataframe.groupby(group)
        .agg(
            has_property=pd.NamedAgg("has_property", "sum"),
            total=pd.NamedAgg(group[0], "count"),
        )
        .reset_index()
    )

    aggregated["percentage_has_id"] = (
        aggregated["has_property"] / aggregated["total"]
    ) * 100

    return aggregated
