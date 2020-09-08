import pandas as pd
import matplotlib.pyplot as plt
from wikidata_panglaodb.quality import summarize_histology, plot_matched_item_types


def main():

    cells = pd.read_csv("results/true_matches/cells_checked.csv").drop_duplicates(
        subset=["id"]
    )
    organs = pd.read_csv("results/true_matches/organs_checked.csv").drop_duplicates(
        subset=["id"]
    )
    tissues = pd.read_csv("results/true_matches/tissues_checked.csv").drop_duplicates(
        subset=["id"]
    )

    histo_summary = summarize_histology([cells, tissues, organs], [215, 246, 29])
    histo_summary.index = ["cells", "tissues", "organs"]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 9))

    ax1 = plot_matched_item_types(cells, histo_summary, "cells", ax=ax1)
    ax2 = plot_matched_item_types(organs, histo_summary, "organs", ax=ax2)
    ax3 = plot_matched_item_types(tissues, histo_summary, "tissues", ax=ax3)

    ax1.set_title("Cell types")
    ax2.set_title("Organs")
    ax3.set_title("Tissues")

    fig.tight_layout()
    fig.savefig("figs/reconciled_item_types.png")


if __name__ == "__main__":
    main()
