# Datasets

This directory contains the datasets used by **VazhehKav** for data preparation, experimentation, and machine learning model development.

Dataset files are intentionally excluded from this repository because of their size and third-party ownership. Download the required files from their original sources and place them in this directory before running the relevant notebooks.

## 1. ParsOffensive Dataset

| Property | Details |
|---|---|
| Source | [golnaz76gh/pars-offensive-dataset](https://github.com/golnaz76gh/pars-offensive-dataset) |
| Required File | `ParsOffensive.xlsx` |
| Format | Excel (`.xlsx`) |
| Language | Persian |
| Task | Offensive language detection |
| Labels | `Offensive`, `Neutral` |

ParsOffensive is described in its source repository as a manually annotated dataset containing 8,433 Persian Instagram comments.

Download `ParsOffensive.xlsx` from the [original repository](https://github.com/golnaz76gh/pars-offensive-dataset) and place it in this directory.

Expected structure:

```text
data/
├── README.md
└── ParsOffensive.xlsx
```

### Citation

If you use ParsOffensive in research or publish results based on it, cite the associated paper:

> Ali Nazarizadeh, Minoo Sayyadpour, Omid Ebrahimkhani, Amirmasoud Iravani, Golnaz Ghannadan Shirazi, and Mojgan Behravan. "Parsoffensive: Persian Offensive Comments Dataset." *Proceedings of the 11th International Conference on Web Research (ICWR)*, 2025, pp. 100–104. https://doi.org/10.1109/ICWR65219.2025.11006224

**BibTeX:**

```bibtex
@inproceedings{nazarizadeh2025parsoffensive,
    author    = {Nazarizadeh, Ali and Sayyadpour, Minoo and Ebrahimkhani, Omid and Iravani, Amirmasoud and Ghannadan Shirazi, Golnaz and Behravan, Mojgan},
    title     = {Parsoffensive: Persian Offensive Comments Dataset},
    booktitle = {Proceedings of the 11th International Conference on Web Research (ICWR)},
    year      = {2025},
    pages     = {100--104},
    doi       = {10.1109/ICWR65219.2025.11006224}
}
```

## 2. Digikala Comments and Products Dataset

| Property | Details |
|---|---|
| Source | [Digikala Comments and Products on Kaggle](https://www.kaggle.com/datasets/radeai/digikala-comments-and-products) |
| Language | Persian |
| Data Type | E-commerce comments and product information |
| Purpose | Recommendation prediction and experimentation |

This dataset provides Persian e-commerce comments and related product information. The Kaggle page describes a collection of more than 6 million comments and 1.2 million products. These figures, as well as the available files and columns, may change between dataset versions.

### Required File

The relevant project notebook currently expects the comments CSV at:

```text
data/digikala-comments.csv
```

Download the comments file from the [Kaggle dataset page](https://www.kaggle.com/datasets/radeai/digikala-comments-and-products).

If the downloaded file has a different name, rename it to `digikala-comments.csv` or update the corresponding input path in the notebook.

Keep product information files separate unless a notebook explicitly requires them.

## Download and Setup

1. Open the original dataset source pages linked above.
2. Download the datasets required by the notebooks you intend to run.
3. Place the downloaded files in this `data/` directory.
4. Make sure the filenames match the paths expected by the notebooks.
5. Install the project's Python dependencies before running the notebooks.

**Important:** Dataset filenames, formats, and schemas may change between releases. Check the original source pages and the corresponding notebook input paths if you encounter loading errors.

## Licensing and Responsible Use

The datasets referenced in this directory are maintained by third parties. VazhehKav does not claim ownership of these datasets or grant additional rights to use or redistribute them.

Before using or redistributing any dataset, review its original source for:

- License and usage terms.
- Attribution and citation requirements.
- Redistribution restrictions.
- Commercial-use permissions.

The ParsOffensive source repository provides a recommended academic citation, but does not clearly specify a dataset license. Contact the dataset maintainers for clarification when necessary.

**Dataset files are excluded through the repository's `.gitignore`.** Only this README and other explicitly permitted project files should be committed. Do not upload downloaded datasets to this repository unless their licenses and source terms explicitly allow redistribution.
