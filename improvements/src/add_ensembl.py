import pandas as pd


def main():

    path = "../../analysis/results/true_matches/"
    human = pd.read_csv(f"{path}homo_sapiens_genes.csv")
    mouse = pd.read_csv(f"{path}mus_musculus_genes.csv")

    genes = pd.concat([human, mouse])

    genes_missing_ensg = genes[genes["ensg_wdt"].isnull()]

    stated_in = "Q99936939"
    reference_url = "https://github.com/oscar-franzen/PanglaoDB"
    retrieved = "+2020-09-09T00:00:00Z/11"

    for _, row in genes_missing_ensg.iterrows():

        item = row["item"]
        ensg = row["ensg_panglao"]

        statement = f'{item}|P594|"{ensg}"|'
        references = f'S248|{stated_in}|S854|"{reference_url}"|S813|{retrieved}\n'

        with open("../quickstatements/ensembl_genes.qs", "a") as qs:
            qs.write(statement + references)


if __name__ == "__main__":
    main()
