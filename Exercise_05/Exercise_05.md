# Exercise_05

## abstract
Use the Euler method to calculate the trajectory of cannon shell.

## Background
* From Newton's second law, we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D0%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%5E%7B2%7D%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-g),<br>
and then write each of these second-order quations as two first-order differential equations<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_x%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_x%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D0%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_y%20%5C%5C%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_y%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-g),<br>
finally use the Euler method, we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t).<br>
The drag force on the cannon shell is given by 
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_%7B2%7Dv%5E%7B%7D2), where ![](http://latex.codecogs.com/gif.latex?v%3D%5Csqrt%7Bv_%7Bx%7D%5E%7B2%7D&plus;v_%7By%7D%5E%7B2%7D%7D) is the speed of the shell, and we find<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20F_%7Bdrag%2Cx%7D%3DF_%7Bdrag%7Dcos%5Ctheta%20%3DF_%7Bdrag%7D%28v_x/v%29%3D-B_2vv_x%20%5C%5C%20F_%7Bdrag%2Cy%7D%3DF_%7Bdrag%7Dsin%5Ctheta%20%3DF_%7Bdrag%7D%28v_y/v%29%3D-B_2vv_y),<br>
then we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta%20t).<br>

* If we consider the air density<br>
isothermal model![](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%5Crho%20_0e%5E%7B-y/y_0%7D),<br>
adiabatic model![](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%5Crho%20_0%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%20%7D),<br>
and from ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E%7B*%7D%3D%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7DF_%7Bdrag%7D%28y%3D0%29),<br>
we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7D%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7D%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta%20t).<br>

* If we consider that the acceleration due to gravity, g, depands on altitude, we have<br>
![](http://latex.codecogs.com/gif.latex?g%3Dg_0%28%5Cfrac%7BR%7D%7BR&plus;y%7D%29%5E2)

* The landing point of the shell
Through the calculation, we will get the last point above ground(n) and the point that would have been below ground(n+1). If we let ![](http://latex.codecogs.com/gif.latex?r%3D-y_n/y_%7Bn&plus;1%7D) then a linear interpolation gives<br>
![](http://latex.codecogs.com/gif.latex?x_l%3D%5Cfrac%7Bx_n&plus;rx_%7Bn&plus;1%7D%7D%7Br&plus;1%7D), and ![](http://latex.codecogs.com/gif.latex?y_l%3D0).

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

*  Assume that g is a constant again, and consider the effect of air density.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 0.7km/s , ![](http://latex.codecogs.com/gif.latex?B_%7B2%7D/m) = 0.04/km , ![](http://latex.codecogs.com/gif.latex?y_0%3Dk_BT/mg) = 10km , a = 6.5K/km , ![](http://latex.codecogs.com/gif.latex?%5Calpha) = 2.5 , ![](http://latex.codecogs.com/gif.latex?T_0) = 300K
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/figure_1-1.png)
Let's enlarge the figure to see the landing point clearly.
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/figure_1-3.png)

* Finally, let's consider all the effects considered above.<br>
![](http://latex.codecogs.com/gif.latex?v_%7Bo%7D) = 0.7km/s , ![](http://latex.codecogs.com/gif.latex?B_%7B2%7D/m) = 0.04/km , ![](http://latex.codecogs.com/gif.latex?y_0%3Dk_BT/mg) = 10km , a = 6.5K/km , ![](http://latex.codecogs.com/gif.latex?%5Calpha) = 2.5 , ![](http://latex.codecogs.com/gif.latex?T_0) = 300K
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/figure_1-2.png)
Let's enlarge the figure to see the landing point clearly.
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_05/figure_1-4.png)

## Conclusion
It is complex to calculate the trajectory of cannon shell.

## Reference
* [Chapter 2 Realistic Projectile Motion_Cai Hao_
Wuhan University](https://www.evernote.com/shard/s140/sh/26f85380-ee6c-4b4b-b33f-6871804d91ff/fb8cc702cb0e8ed7fafb50b2de4596ca)

* 《Computational Physics》 (Second Edition)
