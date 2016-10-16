# Exercise_05

## abstract
Use the Euler method to calculate the trajectory of cannon shell.

## problem
* problem 2.6<br>
Use the Euler method to calculate cannon shell trajectories ignoring both air drag angd the effect of air density (actually, ignoring the former automatically rules out the latter). Compare your results with those in Figure 2.4, and with the exact solution.
* problem 2.8<br>
In our model of the cannon shell trajectory we have assumed that the acceleration due to gravity, g, is a constant. It will, of course, depend on altitude. Add this to the model and calculate how much it affects the range.
* problem 2.9<br>
Calculate the trajectory of our cannon shell including both air drag and the reduced air density at high altitudes so that you can reproduce the result in Figure 2.5. Perform your calculation for different firing angles and determine the value of the angle that give the maximum range.

## Program
* [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/Exercise_05.py)

* Firstly, let's calculate the trajectory of cannon shell without air drag and assume that the acceleration due to gravity, g, is a constant.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 0.7km/s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/1.png)

* Then, let's consider the air drag.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 0.7km/s , ![](http://latex.codecogs.com/gif.latex?B_%7B2%7D/m) = 0.04/km
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/2.png)

* Now, let's ignore the air drag temporarily and consider that g, which depands on altitude, is not a constant.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 0.7km/s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/3.png)
We find that if the initial speed of the cannon shell is not too large, the effect of the change of the g is small.<br>
So let's increase the initial speed and assume that we can make it be 6km/s.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 6km/s
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/4.png)
Now, we can see the effect of the change of the g depanding on altitude obviously.

*  Assume that g is a constant again, and consider the effect of air density.
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 0.7km/s , ![](http://latex.codecogs.com/gif.latex?B_%7B2%7D/m) = 0.04/km
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/6.png)
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/7.png)
Then, let's increase the initial speed.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 6km/s , ![](http://latex.codecogs.com/gif.latex?B_%7B2%7D/m) = 0.04/km
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/8.png)

* Finally, let's consider all the effects considered above. 
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/9.png)
Then, let's increase the initial speed.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 6km/s , ![](http://latex.codecogs.com/gif.latex?B_%7B2%7D/m) = 0.04/km
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/10.png)

## Reference
* [Chapter 2 Realistic Projectile Motion_Cai Hao_
Wuhan University](https://www.evernote.com/shard/s140/sh/26f85380-ee6c-4b4b-b33f-6871804d91ff/fb8cc702cb0e8ed7fafb50b2de4596ca)

* 《Computational Physics》 (Second Edition)
