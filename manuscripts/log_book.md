
What we did, tried, and accomplished during each day of the project.

### 03/09

* Downloaded cell type, organ, tissue and gene data from the wikidata query service.
    * Gene queries used: [Homo sapiens](https://w.wiki/bWc), [Mus musculus](https://w.wiki/bWe)
    * [Cell query used](https://w.wiki/b2v)
    * [Tissues query used](https://w.wiki/bMn)
    * [Organs query used](https://w.wiki/bMp)

### 04/09

* Reconciled cell type, tissue and organ using the preprocessing script and associated functions,
    returning all matches.

### 05/09

* Made a script, similarity_check.py, to better match Panglao's items to wikidata QIDs, ran the script and
    the results are in results/true_matches/.

### 06/09

* Refactored the similarity function, to use less repetition

* Added matching section for genes in preprocessing.py, the matching is done using a manual merge
    with the wikidata query.

### 07/09

* Started work on manual item checking

#### Manual item checking

* cells_checked:

    * Q7840744 - Trychocyte - represents the Algae cell type, not the human cell type (Q7840748), match removed.
    * Not false matched but something of note, Q7116107, Q3326185 and Q66592566 all represent the same concept,
        oxyphil cells.

* tissues_checked:

    * Q5173237 refer to the outer layer of rocks, removed.
    * Q1475019 and Q18816500 (Colon) refer to the grammatical figure, both removed.
    * Q96377210 (Embryo) is a song, removed.
    * Q719458 (Brain) and Q1409015 (heart) refers to the foods, removed.
    * Q2281500 (Rib) is a deformation on a surface, removed.
    * Q67208213 (Thymus) is a spice, removed.
    * Q1615371 (stomacher) is a decorative item, removed.
    * Q1155702 (skin) is a graphical interface, removed.
    * Q97671426 (Skin) is a British TV series, removed.
    * Q5262664 (DermIS) is an information system, removed.
    * Q85782674 (Lungs) is a play, removed.
    * **Plant structures removed**
        * Q1120914 (Placenta)
        * Q1293511 (Cortex)
        * Q148515 (ovary)
    * **Chinese medicine or religion items removed**
        * Q7543099 (Small intestine)
        * Q6704252 and Q6704255 (Lung)
        * Q6140833 (Kidney) 
        * Q7578442 (Spleen)
        * Q6140977 (Liver)
        * Q7618690 (Stomach)
        * Q5691852 (Heart)

* organs_checked:

    * Q1155702 (skin) is a graphical interface, removed.
    * Q97671426 (Skin) is a British TV series, removed.
    * Q85782674 (Lungs) is a play, removed.
    * Q67208213 (Thymus) is a spice, removed.
    * Q96377210 (Embryo) is a song, removed.
    * Q1120914 (Placenta) is a plant structure, removed.
    * **Food items removed**
        * Q1409015 (Heart)
        * Q494268 (blood)
    * **Chinese medicine or religion items removed**
        * Q6140833 (Kidney) 
        * Q5691852 (Heart)
        * Q6140977 (Liver)

* Started working on the item quality assesment - halted until manual item matching is finished

### 08/09

* Started working on analysing matches:
    * Changed module name wdt to quality, since it'll contain all item quality-related functions.
    * Made summary tables for all reconciled panglaodb entities (cells, tissues and organs)
    * Made plots for item types of the reconciled items.

### 09/09

* Analysed gene item matches, percentage that matched, etc. Added this in the draft. This warranted the refactoring of a quality module function,
    now dismembered in two functions.

* Continued work on the item quality assessment.

### 16/09

* Fixed number of statements for outlier Q18033537, since the number it had previously (400+) was 
    [due to multiple wrong statements](https://www.wikidata.org/w/index.php?title=Q18033537&diff=1277410676&oldid=1245096003)

* Discussed visualizations.

### 17/09

* Continued work on item quality assessment, building initial visualizations.

### 18/09

* Built all initial draft visualizations, now need to refactor and test the code in item_quality.py.

### 20/09

* Refactoring and testing functions associated with the item quality assessment.

### 21/09

* Updating table in analyse_matches.py to print totals as well.

* Started working primarily in the manuscript. Progress for this can be followed [here](https://github.com/jvfe/paper_wdt_panglao)

### 02/10

* Created improvements/ directory, code used for improving wikidata items and creating new ones.
* Isolated PanglaoDB's data that was missing from Wikidata.