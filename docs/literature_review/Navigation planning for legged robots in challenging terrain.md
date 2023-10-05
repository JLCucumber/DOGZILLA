## Navigation planning for legged robots in challenging terrain

https://ieeexplore.ieee.org/abstract/document/7759199 - by RSL, ETH

#### Abstract

This paper contributes a novel framework for <u>**traversability estimation and path planning**</u> specifically **targeted at <u>*legged* robot</u> navigation in challenging terrain.**

So, if provided with those perceived terrain characteristics, these infomation can be put into this framework, and then we can estimate how traversable this terrain is for a Legged Robot. Later by path planning, we can converte everything into a series of footprints.

What’s more, this paper also provides **a very good planning structure** 



#### Intro

Concepts:

1. **Obstacle Negotiation**

   1. compute typical terrains (slope, roughness, steps)

2. **Traversability Map**
   This map is a robot-specific map used to compute cost of the robot’s footprint.
   It is generated based on or designed for obstacle negotiation in terrains with steps, gaps and stairs.

3. **Rough and Unstructured Terrain**

   1. Autonomous navigation in rough terrain

4. **Safe and Efficient Navigation**
   This is attributed to the understanding of the traversability of the environment.

5. **Estimating Traversability** in **Rough and Unstructured Terrain**

   

#### Related Work

1. **Chilian and Hirschmüller **- Terrain Navigation for legged robot
2. **Chestnutt** - gives a definition of a common planning problem for a legged robot
3. **Winkler** - He extended a planning and control architecture by incorporating **onboard** perception, locolization and computing equipment to re-plan actions and footholds **online**.
4. **BigDog** - It is very good at walking through rough outdoor terrain by a 2D costmap based on laser. But its planning framework is for such a terrain - generally flat and filled with large obstacles like trees and boulders.

#### 

#### Methodology

##### 1. Traversability Estimation

the travesability map mainly consider three terrain features: the local slope, terrain roughness and the local step height.

while computing those three values, they prefer circular region with a possibly  small diameter, for the tiny terrain features like: steps, small gaps and narrow corridors

In regard of footprint traversability (a second step after traversability map),  they specifically designed **a few constraints in the case of a legged robot**, not other robot traversing a terrain: 1) Steps and Gaps, 2) Terrain Inclination, 3) Local Roughness and Slope



##### 2. Planning Method

1.  circle footprint
    faster than rectangle, 
    guarantees the vadility of the solution path, but can be too conservative

###### Formular of Cost Function

###### Architecutre of the path planning algorithm

1. main components: mapping, global path planner, and short range planner



#### Results

1. **Simulation** 
   Fig. 5. An irregular terrain (top) **consisting of banks, piles, rocks and blanks** is used to test the planning framework for robustness and applicability in challenging terrain

   <img src="https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202309241529851.png" alt="image-20230924144731376" style="zoom: 33%;" />

2. **Real Platform**

   <img src="https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202309241529818.png" alt="image-20230924150612100" style="zoom:50%;" />



#### Further Improvement

The robot could choose different gait for each path segment.

Depending on the estimated traversability, the gait could be switched between **a) planning each footstep separately,  b) applying a static walking gait, or c)  using a more dynamic trotting gait.**



#### References

1. Sampling-based algorithms for optimal motion planning
2. Stereo camera based navigation of mobile robots on rough terrain
3. **Navigation Planning for Legged Robots**
4. Learning planning and control for quadruped locomotion over challenging terrain
5. Optimization and learning for rough terrain legged locomotion
6. J. Z. Kolter, M. P. Rodgers and A. Y. Ng, "A control architecture for quadruped locomotion over rough terrain", *IEEE International Conference on Robotics and Automation (ICRA)*, pp. 811-818, 2008.
7. M. A. Arain, I. Havoutis, C. Semini, J. Buchli and D. G. Caldwell, "A comparison of search-based planners for a legged robot", *9th Workshop on Robot Motion and Control (RoMoCo)*, pp. 104-109, 2013.
8. "Planning and execution of dynamic whole-body locomotion for a hydraulic quadruped on challenging terrain"

---



#### Sooooo…

This paper informed me how important the traversability of a terrain is in the research of LEGGED ROBOTICS, for reasons that legged robots is born to, as well as should aim to overcome challenging terrain. 

In short, if you do legged robots, you can’t avoid thinking of terrains, thinking of how toublesome to measure terrains and make your robots overcome it.

What this paper do, along its reference, is to teach me **a possible and useful way** to consider the traversability of a certain terrain.


