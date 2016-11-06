# Exercise 07

## Abstract
Use python to study the oscillatory motion and chaos.

## Background

## Program

### [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/%20Exercise_07.py)

### Simple Pendulum - Euler method
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_1.png)

### Simple Pendulum - Euler-Cromer method
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_2.png)

### Damped Pendulum
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_3.png)

### Driven Pendulum
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_4.png)

### Nonlinear Pendulum
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_5-1.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_5-2.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_5-3.png)

### Problem 3.12.
In constructing the Poincaré section in Figure 3.9 we plotted points only at times that were in phase with the drive force; that is, at times ![](http://latex.codecogs.com/gif.latex?t%5Capprox%202%5Cpi%20n/%5COmega%20_D), where n is an interger. At these values of t the driving force passed throught zero [see (3.18)]. However, we could just as easily have chosen to make the plot at times corresponding to a maximum of the drive force, or at times ![](http://latex.codecogs.com/gif.latex?%5Cpi/4) out-of-phase with this force, etc. Construct the Poincaré sections for these cases and compare them with Figure 3.9.

* Firstly, construct the phase-space trajectory.<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7.png)
 
* Then, construct the Poincaré section at times in phase with the driving force and out-of-phase with this force.<br>
![](http://latex.codecogs.com/gif.latex?q%3D1/2%2Cl%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_0%3D0.2%2C%5Comega_0%3D0)

 1. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-1.png)

 2. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi&plus;%5Cpi/4)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-2.png)
 
 3. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi&plus;%5Cpi/2)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-3.png)
 
 4. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi&plus;3%5Cpi/4)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-4.png)
 
 5. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi&plus;%5Cpi)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-5.png)
 
 6. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi&plus;5%5Cpi/4)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-6.png)
 
 7. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi&plus;3%5Cpi/2)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-7.png)
 
 8. ![](http://latex.codecogs.com/gif.latex?%5COmega%20_%7BD%7Dt%3D2n%5Cpi&plus;7%5Cpi/4)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-8.png)
 
* Finally, put these figures together.<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_7-9.png)<br>
From these Poincaré sections, we can find that:<br>
For periodic system, there are only several points in Poincaré sections.<br>
For chaotic system, there are vast points constructing curves in Poincaré sections.

### Problem 3.13.
Write a program to calculate and compare the behavior of two, nearly indentical pedulums. Use it to calculate the divergence of two nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent from the slope of a plot of ![](http://latex.codecogs.com/gif.latex?log%28%5CDelta%20%5Ctheta%20%29) as a function of t.<br>

1. ![](http://latex.codecogs.com/gif.latex?q%3D1/2%2Cl%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.05%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-2.png)

2. ![](http://latex.codecogs.com/gif.latex?q%3D1/2%2Cl%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.1%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-1.png)

3. ![](http://latex.codecogs.com/gif.latex?q%3D1/2%2Cl%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.2%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6.png)

4. ![](http://latex.codecogs.com/gif.latex?q%3D1/2%2Cl%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.4%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-3.png)

5. ![](http://latex.codecogs.com/gif.latex?q%3D1/2%2Cl%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.8%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-4.png)

### Problem 3.14.
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent compare with that found in Figure 3.7?

1. ![](http://latex.codecogs.com/gif.latex?l%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.2%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001%2Cq%3D0.1)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-5.png)

2. ![](http://latex.codecogs.com/gif.latex?l%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.2%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001%2Cq%3D0.3)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-6.png)

3. ![](http://latex.codecogs.com/gif.latex?l%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.2%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001%2Cq%3D0.5)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6.png)

4. ![](http://latex.codecogs.com/gif.latex?l%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.2%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001%2Cq%3D0.7)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-7.png)

5. ![](http://latex.codecogs.com/gif.latex?l%3Dg%3D9.8%2C%5COmega_D%3D2/3%2C%5Ctheta_%7B1%7D%280%29%3D0.2%2C%5CDelta%20%5Ctheta%280%29%20%3D0.001%2Cq%3D0.9)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_07/figure_6-8.png)
