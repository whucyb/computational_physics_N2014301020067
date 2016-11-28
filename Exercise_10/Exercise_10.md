# Exercise 10

## Abstract
Use the python to study the solar system and planetary motion.

## Background

* The solar system<br>
![](http://solarsystem.nasa.gov/images/galleries/solar_system_Cover_rev_40-3_br.jpg)<br>
A solar system is a star and all of the objects that travel around it — planets, moons, asteroids, comets and meteoroids. Most stars host their own planets, so there are likely tens of billions of other solar systems in the Milky Way galaxy alone. Solar systems can also have more than one star. These are called binary star systems if there are two stars, or multi-star systems if there are three or more stars.
The solar system we call home is located in an outer spiral arm of the vast Milky Way galaxy. It consists of the sun (our star) and everything that orbits around it. This includes the eight planets and their natural satellites (such as our moon), dwarf planets and their satellites, as well as asteroids, comets and countless particles of smaller debris.

* According to Newton's law of gravitation the interaction force between the sun and a planet is given by<br>
![](http://latex.codecogs.com/gif.latex?F_G%3D%5Cfrac%7BGM_SM_P%7D%7Br%5E2%7D).<br>
From Newton's second law of motion we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D%5Cfrac%7BF_%7BG%2Cx%7D%7D%7BM_P%7D%3D-%5Cfrac%7BGM_Sx%7D%7Br%5E3%7D%20%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D%5Cfrac%7BF_%7BG%2Cy%7D%7D%7BM_P%7D%3D-%5Cfrac%7BGM_Sy%7D%7Br%5E3%7D).<br>
For circular motion we have<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BM_Pv%5E2%7D%7Br%7D%3DF_G%3D%5Cfrac%7BGM_SM_P%7D%7Br%5E2%7D),<br>
rearranging we find<br>
![](http://latex.codecogs.com/gif.latex?GM_S%3Dv%5E2r%3D4%5Cpi%5E2AU%5E3/yr%5E2),<br>
where we have used the fact that (since the orbit is circular) the velocity of the planet is ![](http://latex.codecogs.com/gif.latex?2%5Cpi%20r/%281%20yr%29%3D2%5Cpi%28AU/yr%29) (recall that r = 1 AU).<br>
Then, use the Euler-Cromer method we have<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7B4%5Cpi%5E2%20x_i%7D%7Br_%7Bi%7D%5E%7B3%7D%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci&plus;1%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7B4%5Cpi%5E2%20y_i%7D%7Br_%7Bi%7D%5E%7B3%7D%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci&plus;1%7D%5CDelta%20t)

* Kepler's laws of planetary motion

1. First law<br>
The orbit of every planet is an ellipse with the Sun at one of the two foci.<br>
![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Kepler-first-law.svg/203px-Kepler-first-law.svg.png)

2. Second law<br>
A line joining a planet and the Sun sweeps out equal areas during equal intervals of time.<br>
![](https://upload.wikimedia.org/wikipedia/commons/6/69/Kepler-second-law.gif)

3. Third law<br>
The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit.<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BT%5E2%7D%7Ba%5E3%7D%3Dconstant)

## Program
### [Click here to see the code.](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_10/Exercise_10.py)

### Question 4.8.

* Keep a = 1 AU，and change the value of e.<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_10/GIF_1.gif)<br>
(We can see that, when e > 0.7, the trajectory is not stable. Perhaps the reason is that the accumulated error exists.)

* Keep e = 0.7，and change the value of a.<br>
![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_10/GIF_2.gif)

* From the gifs above, we can see the value of ![](http://latex.codecogs.com/gif.latex?T%5E2/a%5E3) is arround 1. Then, the Kepler's third law for elliptical orbits has been verified.

### Question 4.9.

![](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/Exercise_10/GIF_3.gif)

## Conclusion


## Reference

* 《Computational Physics》 (Second Edition)
