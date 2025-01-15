# Kriging

## Motivations

Kriging is a statistical method of interpolation based on normally distributed variables in a physical space. This model is well-suited for the inference of unknown data that depends on neighboring known data points. More precisely, Kriging weights the prediction of the unknown variable according to its distance from each of the known measurements. To achieve this, the model leverages the variance-covariance matrices of the Gaussian variables as well as the physical distances between them.

## Principle
Let us denote, for all $i \in {1, ..., n}$, $x_i$ the geographical coordinates of the microsensor $i$ and $Z(x_i)$ the random variable representing its PM2.5 measure. Then the interpolation $\hat{Z}(x_0)$ is computed similarly as classic linear regressor:  
$\hat{Z}(x_0) = \sum_{i=1}^n w_i \times Z(x_i)$

But the essential feature of Kriging resides in the computation of the weights $w_i$, which depend on the distances between the target point and the known data points:  

$$
\begin{bmatrix}\hat{W}\\\mu\end{bmatrix} = \begin{bmatrix}
\operatorname{Var}_{x_i}& \mathbf{1}\\
\mathbf{1}^T& 0
\end{bmatrix}^{-1}\cdot \begin{bmatrix} \operatorname{Cov}_{x_ix_0}\\ 1\end{bmatrix}
$$
$\mu$ is a Lagrange multiplier used to honor the unbiasedness condition of the estimator.  
$\operatorname{Var}_{x_i}$ and $\operatorname{Cov}_{x_ix_0}$ are respectively the variogram and covariogram of the stochastic field formed by the microsensors.  

## Method

The procedure utilizing the Kriging model aims to compute a confidence interval for a microsensor's measurement of PM2.5 at time $t$, denoted $Z(x_0)$, based on a chosen number $n$ of neighboring measurements $(Z(x_i))_{i \in \{1, ..., n\}}$ taken at the same time $t$. If the observed measured value of PM2.5, $Z(x_0)$, falls within the prediction confidence interval, then the microsensor value is deemed valid.

## Results
to be filled