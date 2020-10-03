<!-- badges start -->
[![license](https://img.shields.io/badge/license-BSD%202--Clause-green)](https://github.com/jvfe/wikidata_panglaodb/blob/master/LICENSE)
[![pytest status](https://github.com/jvfe/wikidata_panglaodb/workflows/wikidata_panglaodb/badge.svg)](https://github.com/jvfe/wikidata_panglaodb/actions)
<!-- badges end -->

# Analysing the extent of cell type information present in Wikidata: A case study on PanglaoDB

Research compendium for the project "Analysing the extent of cell type information present in Wikidata: A case study on PanglaoDB".

## Repository brief descrition

Research-related directories:

* **analysis**: Scripts and notebooks used for the main analysis. It also includes the subdirectories:

    * **data**: Raw data from PanglaoDB and Wikidata is stored here.
    * **results**: Processed data is stored here.

* **manuscripts**: Manuscripts for this research project, each manuscript is a submodule of a GitHub repository that uses 
    [Manubot](https://github.com/manubot/manubot).

* **improvements**: One-use code, creating Wikidata items from PanglaoDB's metadata and improving existing items.

Software-related directories, they are structured similarly to a Python package:

* **wikidata_panglaodb**: This is the source code for all author-defined functions used in the analysis.
* **tests**: These are the unit tests for the wikidata_panglaodb "package" functions.
* **docs**: This is a directory containing documentation for the wikidata_panglaodb functions, it is served as
    a [live website](http://jvfe.github.io/wikidata_panglaodb) in our github pages branch.

## Reproducing and developing

### Reproducing the analyses

Pre-requisites:

* Python>=3.7
* A unix based terminal interface.

Download the [repository's zip file](https://github.com/jvfe/wikidata_panglaodb/archive/master.zip) or clone it using:

```bash
git clone --recurse-submodules https://github.com/jvfe/wikidata_panglaodb
```

Then, at the project's root directory (wikidata_panglaodb/):

```bash
pip install .
```

And then run the scripts in the analysis/ subdirectory.

### Collaborating

Pre-requisites:

* Git
* A unix based terminal interface
* [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

Initiate the environment:

```bash
conda env create -f environment.yaml
conda activate wdt_panglaodb
```

Download the base package in editable mode:

```bash
pip install -e .
```

**If you've already collaborated before but changes have been made to the conda enviroment/repository, run:**

```bash
git pull origin master
conda activate wdt_panglaodb
conda env update --file environment.yaml
```

