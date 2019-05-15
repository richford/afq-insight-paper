# Introducing AFQ-Insight

This is the technical description of AFQ-Insight, a tool for
multidimensional analysis and detection of informative features
in diffusion MRI measurements of human white matter. It includes
applications in the study of amyotrophic lateral sclerosis (ALS) and
aging.

## Project Organization

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── bin                <- Compiled model code can be stored here (not tracked by git)
    ├── config             <- Configuration files, e.g., for doxygen or for your model if needed
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── docs               <- Poster presentation and home of the github pages data
    ├── notebooks          <- Jupyter notebooks
    ├── reports            <- Manuscript source, e.g., LaTeX, Markdown, etc., or any project reports
    │   └── figures        <- Figures for the manuscript or reports
    └── src                <- Source code for this project
        ├── data           <- scripts and programs to process data
        ├── external       <- Any external source code, e.g., pull other git projects, or external libraries
        ├── models         <- Source code for your own model
        ├── tools          <- Any helper scripts go here
        └── visualization  <- Scripts for visualisation of your results, e.g., matplotlib, related.

## Prerequisites

### Docker-based installation

We recommend that you use the supplied docker image to reproduce the results of this paper.
To build the docker image, type
```bash
make docker-build
```

After that, you can run the jupyter notebooks in the `notebooks` directory by typing
```bash
make docker-lab
```
and then navigating to the URL supplied in the output of that command. When you're done,
type <kbd>Ctrl</kbd>+<kbd>C</kbd> (twice to confirm) to return to your host machine shell.

If you want to obtain an interactive shell in the Docker image, type
```bash
make docker-shell
```

When you're done, type `exit` to return to your host machine shell.

### Docker-less installation

If you don't want to use Docker, you must have Python (>=
3.6) installed. If you don't already have Python installed, we recommend
the free [Anaconda Python](https://www.anaconda.com/download/).

You will then need to install dependencies using either
```bash
pip install -r requirements.txt
```
or
```bash
conda env create
conda activate afq-insight-paper
```

## Data

To download the source data, type
```bash
make data
```
