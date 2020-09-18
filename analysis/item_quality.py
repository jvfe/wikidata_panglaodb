# %% [markdown]
# # Analysing item matches and item quality


# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from wikidata_panglaodb.quality import get_number_of_statements_for_items

sns.set(style="whitegrid", palette="muted")

# %%
cells = pd.read_csv("results/true_matches/cells_checked.csv").drop_duplicates(
    subset=["id"]
)
organs = pd.read_csv("results/true_matches/organs_checked.csv").drop_duplicates(
    subset=["id"]
)
tissues = pd.read_csv("results/true_matches/tissues_checked.csv").drop_duplicates(
    subset=["id"]
)
mmu_genes = pd.read_csv("results/true_matches/mus_musculus_genes.csv")
hsa_genes = pd.read_csv("results/true_matches/homo_sapiens_genes.csv")
# %%
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

# %%


def get_genes_item_quality(df, drop=True):

    result_df = df.copy().rename(columns={"item": "id"})

    result_df["has_ensg"] = np.where(result_df["ensg_wdt"].isna(), False, True)
    result_df["has_entrez"] = np.where(result_df["entrez"].isna(), False, True)

    if drop == True:
        result_df.drop(
            ["itemLabel", "entrez", "ensg_wdt", "ensg_panglao"], axis=1, inplace=True
        )

    return result_df


# %%
gene_items_raw = pd.concat(
    [get_genes_item_quality(mmu_genes), get_genes_item_quality(hsa_genes)]
).drop_duplicates(subset=["id"])

gene_items = pd.melt(
    gene_items_raw,
    id_vars=["id", "statements", "species"],
    var_name="property",
    value_name="has_property",
)
# %%
hist_fig, hist_ax = plt.subplots(figsize=(10, 10))

sns.boxplot(
    x="class",
    y="n_statements",
    data=histology_w_statements,
    palette="rocket",
    ax=hist_ax,
)
hist_ax.set_ylabel("# of statements")
hist_ax.set_xlabel("")
hist_fig.savefig("figs/histo_boxplots.png")


def plot_gene_violin(miniplot=False):

    fig, ax = plt.subplots(figsize=(10, 10))

    sns.violinplot(
        x="species",
        y="statements",
        cut=0,
        # hue="species",
        data=gene_items,
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
            data=gene_items[gene_items["statements"] < 70],
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
        fig.savefig("figs/gene_violin_w_miniplot.png")
    else:
        fig.savefig("figs/gene_violin.png")


plot_gene_violin()
plot_gene_violin(miniplot=True)

# %%
# Plots for alternative IDs

gene_altids = (
    gene_items.groupby(["species", "property"])
    .agg(
        has_property=pd.NamedAgg("has_property", "sum"),
        total=pd.NamedAgg("species", "count"),
    )
    .reset_index()
)

gene_altids["percentage_has_id"] = (
    gene_altids["has_property"] / gene_altids["total"]
) * 100

histo_altids = (
    histology_w_statements.groupby("class")
    .agg(
        has_property=pd.NamedAgg("has_property", "sum"),
        total=pd.NamedAgg("class", "count"),
    )
    .reset_index()
)

histo_altids["percentage_has_id"] = (
    histo_altids["has_property"] / histo_altids["total"]
) * 100

# %%
histo_alt_fig, histo_alt_ax = plt.subplots(figsize=(10, 10))
sns.barplot(
    x="class",
    y="percentage_has_id",
    data=histo_altids,
    palette="rocket",
    ax=histo_alt_ax,
)
histo_alt_ax.set_xlabel("")
histo_alt_ax.set_ylabel("% has alternative ID")
histo_alt_ax.yaxis.set_major_formatter(mtick.PercentFormatter())
histo_alt_fig.savefig("figs/histo_alt_ids.png")
# %%
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
gene_alt_ax.set_xlabel("")
gene_alt_ax.set_ylabel("% has alternative ID")
gene_alt_ax.legend(title="")
gene_alt_ax.yaxis.set_major_formatter(mtick.PercentFormatter())
gene_alt_fig.savefig("figs/gene_alt_ids.png")
