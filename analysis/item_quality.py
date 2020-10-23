import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from wikidata_panglaodb.quality import (
    get_number_of_statements_for_items,
    get_genes_item_quality,
    aggregate_altID_data,
)
from wikidata_panglaodb.plotting import plot_gene_violin

sns.set(style="whitegrid", palette="muted")


def main():

    cells = pd.read_csv("results/true_matches/cells_checked.csv")
    organs = pd.read_csv("results/true_matches/organs_checked.csv")
    tissues = pd.read_csv("results/true_matches/tissues_checked.csv")
    mmu_genes = pd.read_csv("results/true_matches/mus_musculus_genes.csv")
    hsa_genes = pd.read_csv("results/true_matches/homo_sapiens_genes.csv")

    # Analysing number of statements

    cells_w_statements = get_number_of_statements_for_items(
        cells["id"].to_list(), has_property="P7963"
    )
    cells_w_statements["class"] = "Cells"
    organs_w_statements = get_number_of_statements_for_items(
        organs["id"].to_list(), has_property="P1554"
    )
    organs_w_statements["class"] = "Organs"
    tissues_w_statements = get_number_of_statements_for_items(
        tissues["id"].to_list(), has_property="P1554"
    )
    tissues_w_statements["class"] = "Tissues"

    histology_w_statements = pd.concat(
        [cells_w_statements, organs_w_statements, tissues_w_statements]
    )

    gene_items_raw = pd.concat(
        [get_genes_item_quality(mmu_genes), get_genes_item_quality(hsa_genes)]
    ).drop_duplicates(subset=["id"])

    gene_items = pd.melt(
        gene_items_raw,
        id_vars=["id", "statements", "species"],
        var_name="property",
        value_name="has_property",
    )

    histo_fig, histo_ax = plt.subplots(figsize=(10, 10))

    sns.boxplot(
        x="class",
        y="n_statements",
        data=histology_w_statements,
        palette="rocket",
        ax=histo_ax,
    )
    histo_ax.set_ylabel("# of statements")
    histo_ax.set_xlabel("")
    histo_fig.savefig("figs/histo_boxplots.png")

    plot_gene_violin(gene_items, file_to="figs/gene_violin.png")
    plot_gene_violin(
        gene_items, file_to="figs/gene_violin_w_miniplot.png", miniplot=True
    )

    # Summarizing alternative IDs

    gene_altids = aggregate_altID_data(gene_items, ["species", "property"])

    histo_altids = aggregate_altID_data(histology_w_statements, ["class"])

    histo_alt_fig, histo_alt_ax = plt.subplots(figsize=(10, 10))
    sns.barplot(
        x="class",
        y="percentage_has_id",
        data=histo_altids,
        palette="rocket",
        ax=histo_alt_ax,
    )

    gene_alt_fig, gene_alt_ax = plt.subplots(figsize=(10, 10))
    sns.barplot(
        x="property",
        y="percentage_has_id",
        hue="species",
        data=gene_altids,
        palette="husl",
        ax=gene_alt_ax,
    )
    gene_alt_ax.set_xticklabels(["Ensembl Gene ID", "Entrez"])
    gene_alt_ax.legend(title="")

    for ax in [gene_alt_ax, histo_alt_ax]:
        ax.set_xlabel("")
        ax.set_ylabel("% has alternative ID")
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())

    histo_alt_fig.savefig("figs/histo_alt_ids.png")
    gene_alt_fig.savefig("figs/gene_alt_ids.png")


if __name__ == "__main__":
    main()
