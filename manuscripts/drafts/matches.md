
Histological entities from PanglaoDB, that is, cell types, tissue types and organs, were reconciled with Wikidata items using the [reconciler](https://pypi.org/project/reconciler/)
python package and an associated Python stemming function from NLTK [@isbn:9780596516499] for string matching.  
After reconciliation, items were manually checked for false matches - items with the same name but that don‘t represent the same concept. Finally, we obtained the reconciled csv data, and it‘s summary can be seen on Table 1. 

Depicted in Table 1 are also matches for gene data, which were acquired using manual intersection of both sources, via a Pandas inner merge. This data didn't go through reconciliation because of it's size, but since both ends are dealing with identifiers (Gene Symbol), the item matching should work much better than with histological entities, which are described in natural language.

|         |   # of unique matches  |   # of matched items |   % of total items that were matched |   % of matches that were perfect |   % of matches that don‘t have P31 | Totals |
|:----------|-------------------:|-----------------:|---------------:|---------------------------:|------------------:|---------:|
| Cells     |                 81 |               85 |        37.6744 |                    38.8235 |           55.2941 |      215 |
| Tissues   |                 85 |               86 |        34.5528 |                    67.4418 |           39.5348 |      246 |
| Organs    |                 22 |               30 |        75.8621 |                    60      |           40      |       29 |
| Human Genes |              35423 |            35427 |        60.8475 |                   nan      |          nan      |    58216 |
| Mouse Genes |              25124 |            25127 |        46.705  |                   nan      |          nan      |    53793 |

Table 1: Summary of the matched entities from PanglaoDB.

Afterwards, we analysed which types these reconciled items belonged to in Wikidata, which is indicated by their “instance of” (P31) property. 
Most items were missing this information (Figure 1).

![](../../analysis/figs/reconciled_items.png)
Figure 1: Percentage of reconciled entities, divided by which item type they belong to. Most reconciled items don‘t count with a “instance of” property,
therefore the item type is classified as “None”. 