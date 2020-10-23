import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from wikidata_panglaodb.quality import (
    summarize_histology,
    summarize_matches,
)
from wikidata_panglaodb.plotting import plot_matched_item_types


def main():
    cells = pd.read_csv("results/true_matches/cells_checked.csv")
    organs = pd.read_csv("results/true_matches/organs_checked.csv")
    tissues = pd.read_csv("results/true_matches/tissues_checked.csv")
    genes_panglaodb = pd.read_csv("data/panglaodb/genes.csv")
    mmu_genes = pd.read_csv("results/true_matches/mus_musculus_genes.csv").rename(
        columns={"itemLabel": "input_value", "item": "id"}
    )
    hsa_genes = pd.read_csv("results/true_matches/homo_sapiens_genes.csv").rename(
        columns={"itemLabel": "input_value", "item": "id"}
    )

    histo_totals = [215, 246, 29]
    histo_summary = summarize_histology([cells, tissues, organs], histo_totals)
    histo_summary.index = ["cells", "tissues", "organs"]
    histo_summary["totals"] = histo_totals

    gene_quant_by_species = (
        genes_panglaodb.groupby("species").count()["symbol"].to_list()
    )

    gene_summary = summarize_matches([hsa_genes, mmu_genes], gene_quant_by_species)
    gene_summary.index = ["genes_hsa", "genes_mmu"]

    print("Match summary:\n", pd.concat([histo_summary, gene_summary]))

    # Item types that were matched
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 9))

    ax1 = plot_matched_item_types(cells, histo_summary, "cells", ax=ax1)
    ax2 = plot_matched_item_types(organs, histo_summary, "organs", ax=ax2)
    ax3 = plot_matched_item_types(tissues, histo_summary, "tissues", ax=ax3)

    ax1.set_title("Cell types")
    ax2.set_title("Organs")
    ax3.set_title("Tissues")
    for axis in [ax1, ax2, ax3]:
        axis.yaxis.set_major_formatter(mtick.PercentFormatter())

    fig.tight_layout()
    fig.savefig("figs/reconciled_item_types.png")


if __name__ == "__main__":
    main()
