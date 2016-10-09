# Exercise 04
## Abstract
Learn a numerical approach, and try to make use of it to solve physics problems involving ordinary differential equations.
## Background
### Radioactive decay
We know that ![](http://latex.codecogs.com/gif.latex?%5E%7B235%7DU) is unstable and would decay. When it comes to a large number of ![](http://latex.codecogs.com/gif.latex?%5E%7B235%7DU) nuclei, we can have the rate equation
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7BN_%7BU%7D%7D%7B%5Ctau%7D),where ![](http://latex.codecogs.com/gif.latex?%5Ctau) is the time constant for the decay.<br>
Solve the differential equation above, and we can obtain the analytical solution
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%3DN_%7BU%7D%280%29e%5E%7B-t/%7B%5Ctau%7D%7D),
where ![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%280%29) is the number of nuclei present at t=0.
### Euler method
From the Taylor expansion for ![](http://latex.codecogs.com/gif.latex?N_%7BU%7D),<br>
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%28%5CDelta%20t%29%3DN_%7BU%7D%280%29&plus;%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%28%5CDelta%20t%29%5E2&plus;...),<br>
if we take ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t) to be small and then simply ignore the therms that involved second and higher powers of ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t), we can have the approximation value of ![](http://latex.codecogs.com/gif.latex?N_%7BU%7D) that
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%28%5CDelta%20t%29%5Capprox%20N_%7BU%7D%280%29&plus;%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5CDelta%20t).<br>
The same result can be obtained from the definition of a derivative that<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5Cequiv%20%5Clim_%7B%5CDelta%20t%5Crightarrow%200%7D%5Cfrac%7BN_%7BU%7D%28t&plus;%5CDelta%20t%29-N_%7BU%7D%28t%29%7D%7B%5CDelta%20t%7D%5Capprox%5Cfrac%7BN_%7BU%7D%28t&plus;%5CDelta%20t%29-N_%7BU%7D%28t%29%7D%7B%5CDelta%20t%7D),
where in the last approximation we have assumed that ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t) is small but nonzero, and we can rearrange this to obtain
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%28t&plus;%5CDelta%20t%29%5Capprox%20N_%7BU%7D%28t%29&plus;%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5CDelta%20t).<br>
So if we insert 
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7BN_%7BU%7D%7D%7B%5Ctau%7D) 
into it, we can obtain
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%28t&plus;%5CDelta%20t%29%5Capprox%20N_%7BU%7D%28t%29-%5Cfrac%7BN_%7BU%7D%28t%29%7D%7B%5Ctau%7D%5CDelta%20t).<br>
## Problem 1.5
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D),<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D),<br>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant , ![](http://latex.codecogs.com/gif.latex?%7B%5Ctau%20%7D). Solve the system of equations for the numbers of nuclei, ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D), as functions of time. Consider different initial confitions, such as ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D%3D100), ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D%3D0), etc., and take ![](http://latex.codecogs.com/gif.latex?%5Ctau%20%3D1) s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D) are constant. In such a steady state, the time derivatives ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) and ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) should vanish.


### The analytical solution
According to the rate equations<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D),<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D),<br>
we can obtain the analytical solution<br>
![](http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20N_%7BA%7D%3D%5Cfrac%7BN_%7BA0%7D&plus;N_%7BB0%7D%7D%7B2%7D&plus;%5Cfrac%7BN_%7BA0%7D-N_%7BB0%7D%7D%7B2%7De%5E%7B-%5Cfrac%7B2%7D%7B%5Ctau%20%7Dt%7D%20%5C%5C%20N_%7BB%7D%3D%5Cfrac%7BN_%7BA0%7D&plus;N_%7BB0%7D%7D%7B2%7D-%5Cfrac%7BN_%7BA0%7D-N_%7BB0%7D%7D%7B2%7De%5E%7B-%5Cfrac%7B2%7D%7B%5Ctau%20%7Dt%7D%20%5Cend%7Bmatrix%7D%5Cright.)，<br>
where ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) is the number of nuclei A and ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) is the number of nuclei B present at t = 0.

### The program
* Use the Euler method to obtain the numerical solution<br>
[Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/Exercise_04.py)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_1.png)<br>
The figure shows that ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D) finally become constant and the time derivatives ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) and ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) finally become 0, which is consistent with the idea that the system reaches a steady state.

* Contrast numerical solution with analytical solution and analyze the influence of the value of ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t) on the accuracy of the numerical solution

1. ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t)=0.01s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_8.png)<br>

2. ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t)=0.05s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_9.png)<br>

3. ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t)=0.1s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_10.png)<br>

4. ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t)=0.2s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_11.png)<br>

5. ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t)=0.5s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_12.png)<br>
We can see that if the value of ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t) is small enough, the numerical solution would be very close to the analytical solution, and the smaller the ![](http://latex.codecogs.com/gif.latex?%5CDelta%20t) is, the numerical solution is more accurate.

* Keep the ![](http://latex.codecogs.com/gif.latex?%5Ctau) = 1s，and change the value of ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D/N_%7BA0%7D)

1. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 0
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_1.png)<br>

2. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 50 
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_2.png)<br>

3. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 100 
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_3.png)<br>

4. ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) = 100 , ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) = 200 
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_4.png)<br>
We can see whatever the value of ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D/N_%7BA0%7D) is, the system can finally reach a steady state.

* Keep ![](http://latex.codecogs.com/gif.latex?N_%7BA0%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB0%7D) the same, and change the value of the ![](http://latex.codecogs.com/gif.latex?%5Ctau)

1. ![](http://latex.codecogs.com/gif.latex?%5Ctau) = 1s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_1.png)<br>

2. ![](http://latex.codecogs.com/gif.latex?%5Ctau) = 2s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_5.png)<br>

3. ![](http://latex.codecogs.com/gif.latex?%5Ctau) = 5s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_6.png)<br>

We can see that when the ![](http://latex.codecogs.com/gif.latex?%5Ctau) = 5s, it is not suitable to keep the total time still be 10s. <br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_04/figure_7.png)<br>
Because if the the time constant ![](http://latex.codecogs.com/gif.latex?%5Ctau) becomes larger, the time, after which the ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D) are constant, will be larger, too.

### Two time constant ![](http://latex.codecogs.com/gif.latex?%5Ctau_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?%5Ctau_%7BB%7D)

## Conclusion
