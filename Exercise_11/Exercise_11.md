# Exercise 11

## Abstract
Use the python to study the chaotic tumbling of Hyperion.

## Background
* Hyperion<br>
![](https://upload.wikimedia.org/wikipedia/commons/9/94/Hyperion_true.jpg)<br>
Hyperion, also known as Saturn VII, is a moon of Saturn discovered by William Cranch Bond, George Phillips Bond and William Lassell in 1848. It is distinguished by its irregular shape, its chaotic rotation, and its unexplained sponge-like appearance. It was the first non-round moon to be discovered.<br>
The moon is named after Hyperion, the Titan god of watchfulness and observation – the elder brother of Cronus, the Greek equivalent of Saturn – in Greek mythology. It is also designated Saturn VII. The adjectival form of the name is Hyperionian.<br>
Hyperion's discovery came shortly after John Herschel had suggested names for the seven previously-known satellites of Saturn in his 1847 publication Results of Astronomical Observations made at the Cape of Good Hope. William Lassell, who saw Hyperion two days after William Bond, had already endorsed Herschel's naming scheme and suggested the name Hyperion in accordance with it. He also beat Bond to publication.

* Simulation<br>
To simulate the motion of Hyperion we will first make few simplifying assumptions. Our goal will not be to perform a relastic simulations. Rather, our objective is simply to show that the motion of such an irregularly shaped moon can be chaotic. With that goal in mind we consider the model with two particles. We have two particles ![](http://latex.codecogs.com/gif.latex?m_1) and ![](http://latex.codecogs.com/gif.latex?m_2), connected by a massless rod in orbit around a massive object located at the origin.<br>
There are two forces acting on each of the masses, the force of gravity from Saturn and the force from the rod. Since we are interested in the motion (and thus the torque) about the center of mass, the force from the rod does not contribute. THe gravitational force on ![](http://latex.codecogs.com/gif.latex?m_1) can be written as<br>
![](http://latex.codecogs.com/gif.latex?%5Cvec%7BF_1%7D%3D-%5Cfrac%7BGM_%7BSat%7Dm_1%7D%7Br_%7B1%7D%5E%7B3%7D%7D%28x_1%5Chat%7Bi%7D&plus;y_1%5Chat%7Bj%7D%29),<br>
where ![](http://latex.codecogs.com/gif.latex?M_%7BSat%7D) is the mass of Saturn, ![](http://latex.codecogs.com/gif.latex?r_1) is the distance from Saturn to ![](http://latex.codecogs.com/gif.latex?m_1), and ![](http://latex.codecogs.com/gif.latex?%5Chat%7Bi%7D) and ![](http://latex.codecogs.com/gif.latex?%5Chat%7Bj%7D) are unit vectors in the x and y directions. The coordinateed of the center of mass are ![](http://latex.codecogs.com/gif.latex?%28x_c%2Cy_c%29), so that ![](http://latex.codecogs.com/gif.latex?%28x_1-x_c%29%5Chat%7Bi%7D&plus;%28y_1-y_c%29%5Chat%7Bj%7D) is the vector from the center of mass to ![](http://latex.codecogs.com/gif.latex?m_1). The torque on ![](http://latex.codecogs.com/gif.latex?m_1) is then<br> 
![](http://latex.codecogs.com/gif.latex?%5Cvec%7B%5Ctau_1%7D%3D%5B%28x_1-x_c%29%5Chat%7Bi%7D&plus;%28y_1-y_c%29%5Chat%7Bj%7D%5D%5Ctimes%20%5Cvec%7BF_1%7D),<br>
with a similiar expression for ![](http://latex.codecogs.com/gif.latex?%5Cvec%7B%5Ctau_2%7D). The total torque on the moon is just ![](http://latex.codecogs.com/gif.latex?%5Cvec%7B%5Ctau_1%7D&plus;%5Cvec%7B%5Ctau_2%7D), and this is related to the time derivtive of ![](http://latex.codecogs.com/gif.latex?%5Comega) by<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Cvec%7B%5Comega%20%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7B%5Cvec%7B%5Ctau_1%7D&plus;%5Cvec%7B%5Ctau_2%7D%7D%7BI%7D),<br>
where ![](http://latex.codecogs.com/gif.latex?I%20%3Dm_1%5Cleft%20%7C%20r_1%20%5Cright%20%7C%5E2&plus;m_2%5Cleft%20%7C%20r_2%20%5Cright%20%7C%5E2) is the moment of inertia. Putting this all together yields, after some algebra,<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Comega%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5Capprox%20-%5Cfrac%7B3GM_%7BSat%7D%7D%7Br_%7Bc%7D%5E%7B5%7D%7D%28x_csin%5Ctheta%20-y_ccos%5Ctheta%20%29%28x_ccos%5Ctheta%20&plus;y_csin%5Ctheta%29),<br>
where ![](http://latex.codecogs.com/gif.latex?r_c) is the distance from the center of mass to Saturn.









## Program
### [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/Exercise_11.py)

### Question 4.19.
Study the behavior of our model for Hyperion for dofferent initial conditions. Estimate the Lyapunov exponent from calculations of ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta), such as those shown in Figure 4.19. Examine how this exponent varies as a function of the eccentricity of the orbit.<br>
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
Our results for the divergence of the two trajectories ![](http://latex.codecogs.com/gif.latex?%5Ctheta_1%28t%29) and ![](http://latex.codecogs.com/gif.latex?%5Ctheta_2%28t%29) in the chaotic regime, shown on the right in Figure 4.19, are complicated by the way we dealt with the angle ![](http://latex.codecogs.com/gif.latex?%5Ctheta). In Figure 4.19 we followed the practice employed in Chapter3 and restricted ![](http://latex.codecogs.com/gif.latex?%5Ctheta) to the range ![](http://latex.codecogs.com/gif.latex?-%5Cpi) to ![](http://latex.codecogs.com/gif.latex?&plus;%5Cpi), since angles outside this range are equivalent to angles within it. However, when during the course of a calculation the angle passes out of this range and is then "reset" (by adding or substracting ![](http://latex.codecogs.com/gif.latex?2%5Cpi)), this shows up in the results for ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta) as a discontinuous (and distracting) jump. Repeat the calculation of ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta) as in Figure 4.19, but do not restrict the value of ![](![](http://latex.codecogs.com/gif.latex?%5Ctheta)). This should remove the large ![](http://latex.codecogs.com/gif.latex?%28%5CDelta%20%5Ctheta%5Csim%202%5Cpi%20%29) jumps in ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta) in Figure 4.19, but the smaller and more frequent dips will remain. What is the origin of these dips?
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/figure_1.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_11/figure_2.png)

## Conclusion

The chaotic tumbling of Hyperion is complex.

## Reference

* 《Computational Physics》 (Second Edition)

* Wikipedia

* NASA
