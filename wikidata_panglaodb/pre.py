"""Preprocessing and download functions"""

from reconciler import reconcile
import pandas as pd
import numpy as np


def downloads_panglao(data_urls):
    """Downloads metadata from PanglaoDB

    Gets the unique values of metadata entities and writes 
    those to text files.

    Args:
        data_urls (dict(list)): A dictionary with the urls of each metadata file.

    Returns:
        tuple: A tuple containing the DataFrames tissues, genes, cells_organs_germlayers
            and cells_w_descriptions.
    """

    tissues = pd.read_csv(
        data_urls["tissues"], usecols=[2, 4], names=["tissue", "species"]
    ).drop_duplicates()

    genes = pd.read_csv(data_urls["genes"], names=["ensg_panglao", "symbol"])
    genes["species"] = np.where(
        genes["ensg_panglao"].str.startswith("ENSMUS"), "Mus musculus", "Homo sapiens"
    )

    cells_organs_germlayers = pd.read_csv(
        data_urls["cells_organs_germlayers"],
        names=["cell_type", "germ_layer", "organ"],
    )

    cells_w_descriptions = pd.read_csv(
        data_urls["cells_w_descriptions"],
        names=["cell_type", "description", "synonyms"],
    )

    return tissues, genes, cells_organs_germlayers, cells_w_descriptions


def reconcile_more_types(dataframe_column, type_qids):
    """Reconcile dataframe column against one type QID or more

    This functions loops through all qids given in the type_qids list and reconciles the pandas
    column to them, returning a concatenated dataframe with all the matches.

    Args:
        dataframe_column (Series): A pandas dataframe column with the values to reconcile.
        type_qids (list): A list of the QIDs value you want to reconcile against.

    Returns: 
        DataFrame: A dataframe containing all possible matches for each item type.

    """

    all_matches = []
    for type in type_qids:
        try:
            current = reconcile(dataframe_column, type_id=type, top_res="all")
            all_matches.append(current)
        except Exception:
            pass
    try:
        full_df_matches = pd.concat(all_matches)
    except ValueError:
        pass
    else:
        return full_df_matches


def chunk_dataframe(df, base_size):
    """Splits a dataframe into many chunks of length base_size
    
    This is useful to reconcile large dataframes, since the requests will 
    be lighter and you'll have the capacity to space them out.

    Args:
        df (DataFrame): A large dataframe to split.
        base_size (int): The number of rows of each chunk.

    Returns:
        list(DataFrame): A list of DataFrames, each of length base_size.
    """

    length_of_list = int(len(df) / base_size)

    chunks = [
        df.iloc[i * base_size : (i + 1) * base_size].copy()
        for i in range(length_of_list + 1)
    ]

    return chunks

