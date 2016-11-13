# Exercise 08

## Abstract
Use python to study the oscillatory motion and chaos.

## Background
* Simple pendulum<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta)

* Euler method<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Comega%20_%7Bi&plus;1%7D%3D%5Comega%20_%7Bi%7D-%28g/l%29%5Ctheta%20_i%5CDelta%20t%20%5C%5C%20%5Ctheta%20_%7Bi&plus;1%7D%3D%5Ctheta%20_i&plus;%5Comega%20_i%5CDelta%20t%20%5C%5C%20t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t)

* Euler-Cromer method<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Comega%20_%7Bi&plus;1%7D%3D%5Comega%20_%7Bi%7D-%28g/l%29%5Ctheta%20_i%5CDelta%20t%20%5C%5C%20%5Ctheta%20_%7Bi&plus;1%7D%3D%5Ctheta%20_i&plus;%5Comega%20_%7Bi&plus;1%7D%5CDelta%20t%20%5C%5C%20t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t)

* Damped pendulum<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D)

* Driven, damped pendulum<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_D%5Csin%20%28%5COmega%20_Dt%29)

* Driven, damped, nonlinear pendulum<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Csin%20%5Ctheta%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_D%5Csin%20%28%5COmega%20_Dt%29)

## Program

### [Click here to see the code.]




### Problem 3.18.
Calculate Poincaré section for the pendulum as it undergoes the period-doubling route to chaos. Plot ![](http://latex.codecogs.com/gif.latex?%5Comega) versus ![](http://latex.codecogs.com/gif.latex?%5Ctheta), with one point plotted for each drive cycle, as in Figure 3.9. Do this for ![](http://latex.codecogs.com/gif.latex?F_D) = 1.4, 1.44, 1.465, using the other parameters as given in connection with Figure 3.10. You should find that after removing the points corresponding to the initial transient the attractor in the period-1 regime will contain only a single point. Likewise, if the behavior is period n, the attractor will contain n discrete points.<br>




### Problem 3.20.
Calculate the bifurcation diagrams for the pendulum in the vicinity of ![](http://latex.codecogs.com/gif.latex?F_D) = 1.35 to 1.5. Make a magnified plot of the diagram (as compared to Figure 3.11) and obtain an estimate of the Feigenbaum ![](http://latex.codecogs.com/gif.latex?%5Cdelta) parameter.

## Conclusion
There is chaos in oscillatory motion.

## Reference
* [Chapter 3 Oscillatory Motion and Chaos_Cai Hao_Wuhan University](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357)

* 《Computational Physics》 (Second Edition)
