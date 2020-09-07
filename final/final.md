# Quantum Mechanics

姓名：陈叶波
学号：2014301020067
班级：物理学基地一班

## Abstract
![](http://img5.imgtn.bdimg.com/it/u=1121746923,460278542&fm=23&gp=0.jpg)
There are only a few problems in quantum mechanics that can be solved exactly, most notably the harmonic oscillator, a particle in a box, and the hydrogen atom. Nearly all other nontrivial quantum problems either have no known analytic solutions or can be attacked analytically only with extreme difficult. This is why perturbation methods play such an important role in quantum theory and also why numerical methods are an attractive alternative. In this final project, let us use python to solve some problems with quantum mechanics.
## Background
* Quantum mechanics
![](https://upload.wikimedia.org/wikipedia/commons/6/6e/Solvay_conference_1927.jpg)
Quantum mechanics is the science of the very small. It explains the behaviour of matter and its interactions with energy on the scale of atoms and subatomic particles.
By contrast, classical physics only explains matter and energy on a scale familiar to human experience, including the behaviour of astronomical bodies such as the Moon. Classical physics is still used in much of modern science and technology. However, towards the end of the 19th century, scientists discovered phenomena in both the large (macro) and the small (micro) worlds that classical physics could not explain. Coming to terms with these limitations led to two major revolutions in physics which created a shift in the original scientific paradigm: the theory of relativity and the development of quantum mechanics. This article describes how physicists discovered the limitations of classical physics and developed the main concepts of the quantum theory that replaced it in the early decades of the 20th century. These concepts are described in roughly the order in which they were first discovered. For a more complete history of the subject, see History of quantum mechanics.
![](https://upload.wikimedia.org/wikipedia/commons/c/c8/Schroedingers_cat_film.svg)
Light behaves in some respects like particles and in other respects like waves. Matter—particles such as electrons and atoms—exhibits wavelike behaviour too. Some light sources, including neon lights, give off only certain frequencies of light. Quantum mechanics shows that light, along with all other forms of electromagnetic radiation, comes in discrete units, called photons, and predicts its energies, colours, and spectral intensities. Since one never observes half a photon, a single photon is a quantum, or smallest observable amount, of the electromagnetic field. More broadly, quantum mechanics shows that many quantities, such as angular momentum, that appeared to be continuous in the zoomed-out view of classical mechanics, turn out to be (at the small, zoomed-in scale of quantum mechanics) quantized. Angular momentum is required to take on one of a set of discrete allowable values, and since the gap between these values is so minute, the discontinuity is only apparent at the atomic level.
Many aspects of quantum mechanics are counterintuitive and can seem paradoxical, because they describe behaviour quite different from that seen at larger length scales. In the words of quantum physicist Richard Feynman, quantum mechanics deals with "nature as She is absurd". For example, the uncertainty principle of quantum mechanics means that the more closely one pins down one measurement (such as the position of a particle), the less accurate another measurement pertaining to the same particle (such as its momentum) must become.
* Time-independent Schrödinger equation
![](https://upload.wikimedia.org/wikipedia/commons/9/99/Erwin_Schrodinger2.jpg)
The time-independent Schrödinger equation for a psrticle in three dimensins is
$-\frac{\hbar ^2}{2m}\nabla ^2\psi + V(\vec{r})\psi = E \psi$
where $\hbar$ is Planck's constant, m is the mass of the particle, V is the potential energy, E is the energy of the particle, and $\psi$ is the wave function.
## Shooting method

Consider the time-independent Schrödinger equation for a psrticle in one dimensin, and the potential energy is
$V(x) = \begin{cases}
0 & \ -L  \leq x \leq L \\
\infty & \ other
\end{cases}
$.
In order to simplify the simulation, we choose $\hbar = 1, m = 1, L = 1$, $V(x) = \begin{cases}
0 & \ -1  \leq x \leq 1 \\
V_0 & \ other
\end{cases}
$.
* [Click here to see the code](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/final/1.py)

* Firstly, set $\psi_0 = 1$, $\psi_{-1} = 1$, and $V_0 = 1000$, use several values of the energy to calculate the $\psi(x)$.
![](http://img2.ph.126.net/g4i1JrE2I2lzfdbxNyGQ-Q==/6632123296862655227.gif)
Then, we can find that the lowest even parity level is between 1.1563 and 1.1564.
![](http://img2.ph.126.net/pjYPeu4UDlV7UQW2XUtYdQ==/6631844020909203482.png)
Further, change the value of $V_0$, we can finally abtain that the lowest even parity level is 1.19636.
![](http://img1.ph.126.net/v0xJPzCQe2A-PR-TYHusdA==/6631944076467325498.png)
We know that the theoretical value of the lowest odd parity level is $\pi ^2 / 8 = 1.2337$, which shows that there exists an error.

* Secondly, set $\psi_0 = 1$, $\psi_{-1} = 1$, and $V_0 = 1000$, use several values of the energy to calculate the $\psi(x)$.
![](http://img1.ph.126.net/jB0zDFEzsIvPlKKnO-LH7w==/6632139789537071854.gif)
Then, we can find that the lowest odd parity level is between 4.6699 and 4.6700.
![](http://img0.ph.126.net/QnBheYt9UOm8YtnsMTYrNg==/6631890200397567207.png)
Further, change the value of $V_0$, we can finally abtain that the lowest odd parity level is 4.83261.
![](http://img2.ph.126.net/qYGlgVR3xctO4LRlGH_7Qg==/6632148585630094535.png)
We know that the theoretical value of the lowest odd parity level is $\pi ^2 / 2 = 4.934$, which shows that there exists an error.
What's more, we can see that if the value of $V_0$ becomes larger, the value of the energy level we calculated will be more precise.
## Failure works
### Matching method
* [Click here to see the code](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/final/2.py)
![](http://img0.ph.126.net/gENsy6bt2q_F3tD6MMPn5w==/6632213456816148432.gif)
$\psi_L$ and $\psi_R$ can not match, and i think there's somethingwrong with the paraments of Lennard-Jones potential the textbook gived.
### A variatioanal approach
* [Click here to see the code](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/final/3.py)
![](http://img0.ph.126.net/c-Vs11eRd-NOst69tZaxnQ==/6632069420792894604.gif)
The program cannot calculate the ground energy.
### Time-dependent Schrödinger equation: direct solutions
* [Click here to see the code](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/final/4.py)
![](http://img2.ph.126.net/RyTJv1NEqBjHPqlY2tLCcQ==/6631952872560352766.gif)
It looks absolutely wrong.
### Ising model
* [Click here to see the code](https://github.com/whucyb/computational_physics_N2014301020067/blob/master/final/5.py)
* ![](http://img1.ph.126.net/aMVQAprwbeyyE-4MMrFWHA==/6631946275490582410.gif)
Sorry, i do not know why it doesn't work.
## Conclusion
We can use the shooting method to find energy levels. However, this method has a relatively large error.
I have so many failure works, and i just have made only one program which can work! But, i think it let me know that computatioal physics is not such an easy subject as i thought and i still have a long long way to go.
## Reference
* 《Computational Physics》 (Second Edition)
* Wikipedia

