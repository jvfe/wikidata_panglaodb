
Histological entities from PanglaoDB, that is, cell types, tissue types and organs, were reconciled with Wikidata items using the [reconciler](https://pypi.org/project/reconciler/)
python package and an associated Python stemming function from NLTK [@isbn:9780596516499] for string matching.  
After reconciliation, items were manually checked for false matches - items with the same name but that don't represent the same concept. Finally, we obtained the reconciled csv data, and it's summary can be seen on Table 1.

|         |   # of unique matches  |   # of matched items |   % of total items that were matched |   % of matches that were perfect |   % of matches that don't have P31 |
|:--------|-------------------:|-----------------:|---------------:|---------------------------:|------------------:|
| Cells   |                 81 |               85 |        37.6744 |                    38.8235 |           55.2941 |
| Tissues |                 79 |               87 |        32.1138 |                    62.069  |           37.931  |
| Organs  |                 22 |               30 |        75.8621 |                    53.3333 |           46.6667 |
Table 1: Summary of the reconciled histological entities from PanglaoDB.

Afterwards, we analysed which types these reconciled items belonged to in Wikidata, which is indicated by their "instance of" (P31) property. 
Most items were missing this information (Figure 1).

![](../../analysis/figs/reconciled_items.png)
Figure 1: Percentage of reconciled entities, divided by which item type they belong to. Most reconciled items don't count with a "instance of" property,
therefore the item type is classified as "None". 