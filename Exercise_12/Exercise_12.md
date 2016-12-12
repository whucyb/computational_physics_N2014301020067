# Exercise 12

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

## Problem 5.1. & 5.3.

[Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/1.py)

* The first boundary condition is

![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2C-0.3%5Cleq%20x%5Cleq%200.3%5C%20and%5C%20-0.3%5Cleq%20y%5Cleq%200.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/4.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/5.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/6.png)

* The second boundary condition is
 
![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20-0.3%5Cleq%20y%5Cleq%200.3%5C%5C%20-1%20%26%20%2Cx%3D0.3%5C%20and%5C%20-0.3%5Cleq%20y%5Cleq%200.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/1.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/2.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/3.png)

* Now, let's cosider other boundary conditions.

 1. <br>
 ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D0%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/7.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/8.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/9.png)

 2. <br>
 ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0%5C%5C%20-1%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/10.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/11.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/12.png)

 3. <br>
 ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/10-1.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/11-1.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/12-1.png)

 4. <br>
 ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0.3%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D-0.3%5C%5C%20-1%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D-0.3%5C%5C%20-1%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/13.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/14.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/15.png)

 5. <br>
 ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D0.3%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D-0.3%5C%5C%201%20%26%20%2Cx%3D-0.3%5C%20and%5C%20y%3D-0.3%5C%5C%201%20%26%20%2C%20x%3D0.3%5C%20and%5C%20y%3D0.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/13-1.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/14-1.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/15-1.png)
 
 6. <br>
 ![](http://latex.codecogs.com/gif.latex?V%3D%5Cbegin%7Bcases%7D%200%20%26%20%2Cx%3D%5Cpm%201%20%5C%20or%5C%20y%3D%5Cpm%201%20%5C%5C%20%5Cfrac%7B10y%7D%7B3%7D%20%26%20%2Cx%3D-0.3%5C%20and%5C%20-0.3%3C%20y%5Cleq%200.3%5C%5C%20-%5Cfrac%7B10y%7D%7B3%7D%20%26%20%2C%20x%3D0.3%5C%20and%5C%20-0.3%5Cleq%20y%3C%200.3%5C%5C%20%5Cfrac%7B10x%7D%7B3%7D%20%26%20%2C-0.3%5Cleq%20x%3C%200.3%5C%20and%5C%20y%3D-0.3%5C%5C%20-%5Cfrac%7B10x%7D%7B3%7D%20%26%20%2C%20-0.3%3C%20x%5Cleq%200.3%5C%20and%5C%20y%3D0.3%5C%5C%200%20%26%20%2Cother%20%5Cend%7Bcases%7D)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/16.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/17.png)
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/18.png)
 
## problem 5.7.

[Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/2.py)

![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_12/figure_1.png)

We can see that the speeds of convergence of Jacobi method and Gauss-Seidel method are almost same while the SOR method has a faster speed of convergence. What's more, for Jacobi method and Gauss-Seidel method, ![](http://latex.codecogs.com/gif.latex?N_%7Biter%7D%5Cpropto%20L%5E2), while for SOR method, ![](http://latex.codecogs.com/gif.latex?N_%7Biter%7D%5Cpropto%20L).

## Conclusion

Use relaxation method can solve Laplace's equation.

## Reference

* 《Computational Physics》 (Second Edition)

* Wikipedia
