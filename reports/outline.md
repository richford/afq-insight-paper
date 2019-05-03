Target journal [PLoS Computational Biology](https://journals.plos.org/ploscompbiol/s/submission-guidelines)

# Introduction
## Tractometry vs averaging over tracts
(see AFQ-Browser paper for inspiration and political correctness)

## Existing methods
- https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.23082 (mancova)
- Sarica et al 2017
- https://www.nature.com/articles/ncomms5932 (for mass univariate approach)

# Results

## SGL in tractometry data
Setting up the problem and solving it
(Figure for pipeline)

## Classification (Sarica)
(Figure showing classification results) <= Done
(Figure showing sparsity pattern) Plot streamlines using DIPY

Link to an AFQ-Browser instance.

### Interpreting prediction failures
(Figure demonstrating failure cases)

## Regression (Age regression on Yeatman 2014 dataset)
(Figure showing regression results) <= Done
(Figure showing sparsity pattern) Plot streamlines using DIPY
(Figure summarizing the pattern as bars/boxplots per tract)

Discuss target transformation function and rationale

Discuss hyperoptimization choices
- Discuss sensitivity to choice
- Recommend hyperopt with rmse for consistency with sgl loss func
- Also anecdotally seems to be a compromise between med AE and r2

Link to an AFQ-Browser instance.

### Interpreting prediction failures

# Discussion
## A novel approach to tractometry analysis
## Open and reproducible
## Feature selection + prediction

### ALS

Discuss comparison with Sarica.

### Age regression
Discuss comparison with SOTA with other methods (and other MRI contrasts, T1w,
etc.)

## AFQ ecosystem

# Methods

## Data
(Raw measurement sources)
(AFQ pipeline)
(Insight preprocessing)

## Sparse Group Lasso
### Regression case
### Classification using logistic regression
## Computational implementation

### Proximal gradient methods
### Meta-parameter optimization
### Cross-validation scheme
(Figure for cross-validation scheme)
