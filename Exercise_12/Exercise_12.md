# Exercuse 12

## Abstract
Use python to solve Laplace's equation

## Background
* Laplace's equation

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20x%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20y%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20z%5E2%7D%3D0)

* Jacobi method

![](http://latex.codecogs.com/gif.latex?V_%7Bnew%7D%28i%2Cj%29%3D%5Cfrac%7B1%7D%7B4%7D%5BV_%7Bold%7D%28i&plus;1%2Cj%29&plus;V_%7Bold%7D%28i-1%2Cj%29&plus;V_%7Bold%7D%28i%2Cj&plus;1%29&plus;V_%7Bold%7D%28i%2Cj-1%29%5D)

In numerical linear algebra, the Jacobi method (or Jacobi iterative method) is an algorithm for determining the solutions of a diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges. This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is named after Carl Gustav Jacob Jacobi.

* Gauss-Seidel method

![](http://latex.codecogs.com/gif.latex?V_%7Bnew%7D%28i%2Cj%29%3D%5Cfrac%7B1%7D%7B4%7D%5BV_%7Bold%7D%28i&plus;1%2Cj%29&plus;V_%7Bnew%7D%28i-1%2Cj%29&plus;V_%7Bold%7D%28i%2Cj&plus;1%29&plus;V_%7Bnew%7D%28i%2Cj-1%29%5D)

In numerical linear algebra, the Gauss–Seidel method, also known as the Liebmann method or the method of successive displacement, is an iterative method used to solve a linear system of equations. It is named after the German mathematicians Carl Friedrich Gauss and Philipp Ludwig von Seidel, and is similar to the Jacobi method. Though it can be applied to any matrix with non-zero elements on the diagonals, convergence is only guaranteed if the matrix is either diagonally dominant, or symmetric and positive definite. It was only mentioned in a private letter from Gauss to his student Gerling in 1823. A publication was not delivered before 1874 by Seidel.

* SOR method

![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5C%5C%20V_%7Bnew%7D%28i%2Cj%29%3D%5Calpha%20%5CDelta%20V%28i%2Cj%29&plus;V_%7Bold%7D%28i%2Cj%29%20%5C%5C%20%5C%5C%20%5CDelta%20V%28i%2Cj%29%5Cequiv%20V%5E%7B*%7D%28i%2Cj%29-V_%7Bold%7D%28i%2Cj%29%20%5C%5C%20%5C%5C%20%5Calpha%20%5Capprox%20%5Cfrac%7B2%7D%7B1&plus;%5Cpi/L%7D)

In numerical linear algebra, the method of simultaneous over-relaxation (SOR) is a variant of the Gauss–Seidel method for solving a linear system of equations, resulting in faster convergence. A similar method can be used for any slowly converging iterative process.
It was devised simultaneously by David M. Young, Jr. and by Stanley P. Frankel in 1950 for the purpose of automatically solving linear systems on digital computers. Over-relaxation methods had been used before the work of Young and Frankel. An example is the method of Lewis Fry Richardson, and the methods developed by R. V. Southwell. However, these methods were designed for computation by human calculators, and they required some expertise to ensure convergence to the solution which made them inapplicable for programming on digital computers. These aspects are discussed in the thesis of David M. Young, Jr.

## Problem 5.1.

![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2C-0.3%5Cleq%20x%5Cleq%200.3%5C%20and%5C%20-0.3%5Cleq%20y%5Cleq%200.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)

## Problem 5.3.

1. ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20-0.3%5Cleq%20y%5Cleq%200.3%5C%5C%20-1%20%26%20%2Cx%3D0.3%5C%20and%5C%20-0.3%5Cleq%20y%5Cleq%200.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)

2. ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D0%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)

3. ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0%5C%5C%20-1%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)

4. ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)

5. ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0.3%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D-0.3%5C%5C%20-1%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D-0.3%5C%5C%20-1%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)

6. ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0.3%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D-0.3%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D-0.3%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)

