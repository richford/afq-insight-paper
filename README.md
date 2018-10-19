# Introducing AFQ-Insight

This is the technical description of AFQ-Insight, a tool for
multidimensional analysis and detection of informative features
in diffusion MRI measurements of human white matter. It includes
applications in the study of amyotrophic lateral sclerosis (ALS) and
dyslexia.

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

To reproduce the results in this repository, you must have Python (>=
3.6) installed. If you don't already have Python installed, we recommend
the free [Anaconda Python](https://www.anaconda.com/download/).

We rely on the following Python packages:

* [`numpy`](http://www.numpy.org/)
* [`matplotlib`](https://matplotlib.org/)
* [`AFQ-Insight`](https://github.com/richford/afq-insight) (which has
  it's own dependencies)

We recommend you install these dependencies using
```
make install
```
You can also install these libraries on your own (e.g. `pip install
<package>` or `conda install <package>`).

## Data

To download
