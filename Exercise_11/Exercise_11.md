# Exercise 11

## Abstract
Use the python to study the chaotic tumbling of Hyperion.

## Background

To simulate the motion of Hyperion we will first make few simplifying assumptions.Our goal will not be to perform a relastic simulations.Rather,our objective is simply to show that the motion of such an irregularly shaped moon can be chaotic.With that goal in mind we consider the model with two bodies.We have two particles  and ,connected by a massless rod in orbit around a massive object located at the origin. 
There are two forces acting on each of the masses,the force of gravity from Saturn and the force from the rod.Since we are interested in the motion about the center of mass,the force from the rod does not contribute.

. 
The coordinateed of the center of mass are ,so that  is the vector from the center of mass to .The torque on  is then: 

With a similiar expression for .The total torque on the moon is just ,and this is related to the time derivtive of  by: 

where  is the moment of inertia.Putting this all together yields, after some algebra. 

where  is the distance from the center fo mass to Saturn









## Program
### [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_10/Exercise_11.py)

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
