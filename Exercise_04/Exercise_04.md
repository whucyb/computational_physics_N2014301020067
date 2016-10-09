# Exercise 04
## Problem 1.5
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D),<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D),<br>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant , ![](http://latex.codecogs.com/gif.latex?%7B%5Ctau%20%7D). Solve the system of equations for the numbers of nuclei, ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D), as functions of time. Consider different initial confitions, such as ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D%3D100), ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D%3D0), etc., and take ![](http://latex.codecogs.com/gif.latex?%5Ctau%20%3D1) s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D) are constant. In such a steady state, the time derivatives ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) and ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) should vanish.
## Abstract

## Background

## Result
* ![](http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20N_%7BA%7D%3DC_%7B1%7D&plus;C_%7B2%7De%5E%7B-%5Cfrac%7B2%7D%7B%5Ctau%20%7Dt%7D%5C%5C%20N_%7BB%7D%3DC_%7B1%7D-C_%7B2%7De%5E%7B-%5Cfrac%7B2%7D%7B%5Ctau%20%7Dt%7D%20%5Cend%7Bmatrix%7D%5Cright.)
* ![](http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20N_%7BA%7D%3D%5Cfrac%7BN_%7BA0%7D&plus;N_%7BB0%7D%7D%7B2%7D&plus;%5Cfrac%7BN_%7BA0%7D-N_%7BB0%7D%7D%7B2%7De%5E%7B-%5Cfrac%7B2%7D%7B%5Ctau%20%7Dt%7D%20%5C%5C%20N_%7BB%7D%3D%5Cfrac%7BN_%7BA0%7D&plus;N_%7BB0%7D%7D%7B2%7D-%5Cfrac%7BN_%7BA0%7D-N_%7BB0%7D%7D%7B2%7De%5E%7B-%5Cfrac%7B2%7D%7B%5Ctau%20%7Dt%7D%20%5Cend%7Bmatrix%7D%5Cright.)
* [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/Exercise_04.py)
1. ![](http://latex.codecogs.com/gif.latex?%5Ctau) = 1s
  1. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 0
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_1.png)<br>
  2. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 50 
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_2.png)<br>
  3. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 100 
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_3.png)<br>
  4. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 200 
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_4.png)<br>

## Conclusion
