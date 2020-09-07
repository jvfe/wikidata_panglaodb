"""Wikidata related functions"""

import requests
import pandas as pd
from collections import defaultdict

# Make it return if item has a particular key
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
