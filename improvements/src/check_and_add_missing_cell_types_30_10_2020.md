# Continuation of manual checks

I am proceeding with the manual checks started yesterday. 

## Matches considered false

* myocyte (Q428914) is too general for "Multinuclear myocytes". There is no description of multinuclear myocyte on the PanglaoDB description file. I`ll just create a new item. 

* bundle of His (Q1577202) is similar, but different of His bundle cells. I`ll create a new item. 

* "Transient cells" is not defined on the description file. To be safe, I`ll exclude it from de list

* "Spermatocyte and Spermatozoa" is a combinatorial class. I`ll create an Wikidata class for any cell that is either a Spermatocyte or Spermatozoa.

* Gonadotropins, Pituitary (Q76787944) refers to the hormones, and not to "Anterior pituitary gland cell". Wikidata has a anterior pituitary (Q356002) but not an Anterior pituitary gland cell. I`ll create it. 

* I need to create theca cell too.

* Acinar cells is matched to acinar cells (Q70219504), which is linked to MeSH D061354 -> Cells lining the saclike dilatations known as acini of various glands or the lungs. In Panglao, "Acinar cells" are the exocrine cells of the pancreas that produce and transport enzymes that are passed into the duodenum where they assist in the digestion of food. acinar cell (Q66590269) is crossreferenced to the matching term in the [Britannica](https://www.britannica.com/science/acinar-cell), so it is a better match.

* epiblast (Q519516) is the tissue that contains Epiblast cells. I`ll create an item for "Epiblast cells". 

* Trichocyte (Q7840744) refers to an algae cell type, which is probably not what is intended in PanglaoDB. As there is no description, I'll exclude it from the list

Changes to make:
* Multinuclear myocytes: Q101003165
* His bundle cells: Q101003168
* Transient cells: EXCLUDE 
* Spermatocyte and Spermatozoa: Q101003191
* Granulocytes: Q223143
* Theca cells: Q101003314
* Acinar cells: Q66590269
* Neuroendocrine cells: Q10599959
* Epiblast cells: Q101003525


And now I`ve finished checking the matches considered False. There are a lot of non-matches that still need checking. 

## Cell types not matched

* Need to create:
    - Immature neurons
    - Cortical interneurons

* Neural stem/precursor cells seems to be best matched to neural stem cells (Q2944097).
* Erythroid-like and erythroid precursor cells is a bit different from erythroid precursor cells (Q70074894). I`ll create a new item. 

* "Cardiac stem and precursor cells" seems to be best matched to Endogenous cardiac stem cell (Q5376332)




Changes to make:
* Immature neurons : Q101003994
* Cortical interneurons: Q101004030
* Neural stem/precursor cells: Q2944097
* Oligodendrocyte progenitor cells: Q7086819
* T cell naive: Q6959842
* Cardiomyocytes: Q1047227
* T memory cells: Q2304808
* Clara cells: Q645712
* Peripheral blood mononuclear cells: Q736033
* Juxtaglomerular cells: Q2596226
* Cardiac stem and precursor cells: Q5376332
* Thymocytes: Q7799635
* Tuft cells: Q25325383
 
There might be many changes yet to make. I`ll make a list of the cell types that need to be added to add them as a batch edit.

Cells to add to Wikidata: 
* Proximal tubule cells
* Human myeloid-derived suppressor cells
* Mouse myeloid-derived suppressor cells
* Myeloid dendritic cells
* Plasmacytoid dendritic cells
* T follicular helper cells
* Osteoclasts and osteoblasts (combinatorial class)
* Glutaminergic neurons
* Meningeal cells
* Erythroid-like and erythroid precursor cells (superclass of erythroid precursor cells (Q70074894))
* Crypt base columnar cells
* Urothelial cells


I stopped at line 26, Tuft cells, ot the not mathed table. 


