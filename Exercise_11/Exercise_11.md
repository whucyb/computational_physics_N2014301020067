# Exercise 11

## Abstract
Use the python to study the chaotic tumbling of Hyperion.

## Background

To simulate the motion of Hyperion we will first make few simplifying assumptions. Our goal will not be to perform a relastic simulations. Rather, our objective is simply to show that the motion of such an irregularly shaped moon can be chaotic. With that goal in mind we consider the model with two particles. We have two particles ![](http://latex.codecogs.com/gif.latex?m_1) and ![](http://latex.codecogs.com/gif.latex?m_2), connected by a massless rod in orbit around a massive object located at the origin.<br>
There are two forces acting on each of the masses, the force of gravity from Saturn and the force from the rod. Since we are interested in the motion (and thus the torque) about the center of mass, the force from the rod does not contribute. THe gravitational force on ![](http://latex.codecogs.com/gif.latex?m_1) can be written as<br>
![](http://latex.codecogs.com/gif.latex?%5Cvec%7BF_1%7D%3D-%5Cfrac%7BGM_%7BSat%7Dm_1%7D%7Br_%7B1%7D%5E%7B3%7D%7D%28x_1%5Chat%7Bi%7D&plus;y_1%5Chat%7Bj%7D%29),<br>
where ![](http://latex.codecogs.com/gif.latex?M_%7BSat%7D) is the mass of Saturn, ![](http://latex.codecogs.com/gif.latex?r_1) is the distance from Saturn to ![](http://latex.codecogs.com/gif.latex?m_1), and ![]() and ![]() are unit vectors in the x and y directions. The coordinateed of the center of mass are ![](http://latex.codecogs.com/gif.latex?%28x_c%2Cy_c%29), so that ![](http://latex.codecogs.com/gif.latex?%28x_1-x_c%29%5Chat%7Bi%7D&plus;%28y_1-y_c%29%5Chat%7Bj%7D) is the vector from the center of mass to ![](http://latex.codecogs.com/gif.latex?m_1). The torque on ![](http://latex.codecogs.com/gif.latex?m_1) is then<br> 
![](http://latex.codecogs.com/gif.latex?%5Cvec%7B%5Ctau_1%7D%3D%5B%28x_1-x_c%29%5Chat%7Bi%7D&plus;%28y_1-y_c%29%5Chat%7Bj%7D%5D%5Ctimes%20%5Cvec%7BF_1%7D),<br>
with a similiar expression for ![](http://latex.codecogs.com/gif.latex?%5Cvec%7B%5Ctau_2%7D). The total torque on the moon is just ![](http://latex.codecogs.com/gif.latex?%5Cvec%7B%5Ctau_1%7D&plus;%5Cvec%7B%5Ctau_2%7D), and this is related to the time derivtive of ![](http://latex.codecogs.com/gif.latex?%5Comega) by<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Cvec%7B%5Comega%20%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7B%5Cvec%7B%5Ctau_1%7D&plus;%5Cvec%7B%5Ctau_2%7D%7D%7BI%7D),<br>
where ![](http://latex.codecogs.com/gif.latex?I%20%3Dm_1%5Cleft%20%7C%20r_1%20%5Cright%20%7C%5E2&plus;m_2%5Cleft%20%7C%20r_2%20%5Cright%20%7C%5E2) is the moment of inertia. Putting this all together yields, after some algebra,<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Comega%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5Capprox%20-%5Cfrac%7B3GM_%7BSat%7D%7D%7Br_%7Bc%7D%5E%7B5%7D%7D%28x_csin%5Ctheta%20-y_ccos%5Ctheta%20%29%28x_ccos%5Ctheta%20&plus;y_csin%5Ctheta%29),<br>
where ![](http://latex.codecogs.com/gif.latex?r_c) is the distance from the center of mass to Saturn.









## Program
### [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/Exercise_11.py)

### Question 4.19.
Study the behavior of our model for Hyperion for dofferent initial conditions. Estimate the Lyapunov exponent from calculations of \Delta \theta, such as those shown in Figure 4.19. Examine how this exponent varies as a function of the eccentricity of the orbit.
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/1.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/2.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/3.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/4.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/5.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/6.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/7.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/8.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/9.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/10.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/11.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/12.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/13.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/14.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/15.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/16.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/17.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/18.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/19.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/20.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/21.png)

### Question 4.20.
Our results for the divergence of the two trajectories \theta1(t) and \theta2(t) in the chaotic regime, shown on the right in Figure 4.19,are complicated by the way we dealt with the angle \theta. In Figure 4.19 we followed the practice employed in Chapter3 and restricted \theta to the range -\pi to +\pi, since angles outside this range are equivalent to angles within it. However, when during the course of a calculation the angle passes out of this range and is then "reset" (by adding or substracting 2\pi), this shows up in the results for \Delta \theta as a discontinuous (and distracting) jump. Repeat the calculation of \Delta \theta as in Figure 4.19, but do not restrict the value of \theta. This should remove the large (\Delta \theta~2\pi) jumps in \Delta \theta in Figure 4.19, but the smaller and more frequent dips will remain. What is the origin of these dips?

## Conclusion

The chaotic tumbling of Hyperion is complex.

## Reference

* 《Computational Physics》 (Second Edition)

* Wikipedia

* NASA
