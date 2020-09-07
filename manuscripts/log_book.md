
What we did, tried, and accomplished during each day of the project.

### 03/09

* Downloaded cell type, organ, tissue and gene data from the wikidata query service.
    * Gene queries used: [Homo sapiens](https://w.wiki/bMk), [Mus musculus](https://w.wiki/bMm)
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