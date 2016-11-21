# Exercise 09

## Abstract
Use the python to study the billiard problem, another kind of chatic system.

## Background
When the collision occurs,<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%20%7D%3D%28%5Cvec%7Bv%7D_%7Bi%7D%5Ccdot%20%5Chat%7Bn%7D%29%5Chat%7Bn%7D%20%5C%5C%20%5Cvec%7Bv%7D_%7Bi%2C%5Cparallel%20%7D%3D%5Cvec%7Bv%7D_%7Bi%7D-%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%20%7D)<br>
hence, the velocity after reflection from the wall is<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cvec%7Bv%7D_%7Bf%2C%5Cperp%20%7D%3D-%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%20%7D%20%5C%5C%20%5Cvec%7Bv%7D_%7Bf%2C%5Cparallel%20%7D%3D%5Cvec%7Bv%7D_%7Bi%2C%5Cparallel%20%7D)

## Program
### [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/Exercise_09.py)

### Question 3.31.
Study the behavior for other types of tables. One interesting possibility is a square table with a circular interior wall located either in the center, or slightly off-center. Another possibility is an elliptical table.
* Square table<br>
![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/0.png)

* Circular stadium<br>
![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/1.png)

* Stadium billiard<br>

1. ![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.001)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/2.png)

2. ![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.01)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/3.png)
![](http://latex.codecogs.com/gif.latex?x_0%3D0%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.01)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/3-1.png)

3. ![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/4.png)

* Elliptical table<br>

1. ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bx%5E2%7D%7B25%7D&plus;%5Cfrac%7By%5E2%7D%7B16%7D%3D1)<br>

 1. ![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/5.png)
 
 2. ![](http://latex.codecogs.com/gif.latex?x_0%3D1.5%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/6.png)
 
 3. ![](http://latex.codecogs.com/gif.latex?x_0%3D3%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/7.png)
 
 4. ![](http://latex.codecogs.com/gif.latex?x_0%3D4.5%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/8.png)
 
 5. ![](http://latex.codecogs.com/gif.latex?x_0%3D4.8%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/9.png)

2. ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bx%5E2%7D%7B4%7D&plus;%5Cfrac%7By%5E2%7D%7B3%7D%3D1)<br>
 
 1. ![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/10.png)
 
 2. ![](http://latex.codecogs.com/gif.latex?x_0%3D0.5%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/11.png)
 
 3. ![](http://latex.codecogs.com/gif.latex?x_0%3D1%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/12.png)
 
 4. ![](http://latex.codecogs.com/gif.latex?x_0%3D1.5%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/12.png)
 
 5. ![](http://latex.codecogs.com/gif.latex?x_0%3D1.8%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6%2C%5Calpha%20%3D0.1)<br>
 ![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/14.png)

* A square table with a circulai interior wall located in the center<br>
![](http://latex.codecogs.com/gif.latex?x_0%3D0.2%2Cy_0%3D0%2Cv_0%3D1%2C%5Ctheta_0%3D%5Cpi/6)<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_09/15.png)

## Conclusion
The trajectory of the billiard is beautiful!

## Reference
* [Chapter 3 Oscillatory Motion and Chaos_Cai Hao_Wuhan University](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357)

* 《Computational Physics》 (Second Edition)
