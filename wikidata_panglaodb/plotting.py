"""Plotting functions"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", palette="muted")


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
        matplotlib.Figure: A bar plot for the item type counts.

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
        color="rosybrown",
        # palette="magma",
        dodge=False,
        ax=ax,
    )
    p.set(xlabel=None)
    p.set_xticklabels(p.get_xticklabels(), rotation=45, horizontalalignment="right")

    return p


def plot_gene_violin(data, file_to, miniplot=False):
    """Make a violin plot for gene data
    
    Plots the distribution of the number of statements for reconciled gene data.

    Args:
        data (DataFrame): Gene data.
        file_to (str): Path where to save the final image.
        miniplot (bool). Wether or not have a miniplot.

    """
    fig, ax = plt.subplots(figsize=(10, 10))

    sns.violinplot(
        x="species",
        y="statements",
        cut=0,
        # hue="species",
        data=data,
        palette="Set2",
        split=True,
        scale="count",
        inner="quartiles",
        ax=ax,
    )
    ax.set_xlabel("")
    ax.set_ylabel("# of statements")

    if miniplot == True:
        ax2 = plt.axes([0.2, 0.6, 0.2, 0.2])
        sns.violinplot(
            x="species",
            y="statements",
            cut=0,
            # hue="species",
            data=data[data["statements"] < 70],
            palette="Set2",
            split=True,
            scale="count",
            inner="quartiles",
            ax=ax2,
        )
        ax2.set_xticklabels("")
        # ax2.set_yticklabels('')
        ax2.set_xlabel("")
        ax2.set_ylabel("")
        ax2.grid(False)
        ax.grid(False)
        fig.savefig(file_to)
    else:
        fig.savefig(file_to)
