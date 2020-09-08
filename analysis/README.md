# Analysis directory

Here you will find all scripts used in the actual analysis. To run them,
make sure you ran `pip install .` at the root directory.

Simple data transformation scripts are plain text python files, scripts containing extensive information and 
associated plots are jupyter notebooks.

## Brief description

* **preprocessing.py**: Downloads metadata from PanglaoDB into the data/panglaodb directory, also reconciles said data and outputs 
    the matches to the results/all_matches directory. For genes, since a manual merge is used, the matches are outputted to results/true_matches.

* **similarity_check.py**: Checks the reconciled/all_matches data for similarity matching, outputting the filtered data to results/true_matches.

* **analyse_matches.py**: Summarize the manually curated matches. 

* **item_quality.py**: Item quality assesment on the manually curated matches and associated plots.