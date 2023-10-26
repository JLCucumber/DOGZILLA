# Related Works / Literature Review

> What is the difference between related works and literature Review?

## What is quadruped robots?

#### From Wheels to Legs 

In the last three decades, mobile robot has made much attention because of exploring the complex environment, space, rescure operation, accomplishing a task without human effort, etc. The mobile robot can be generally divided into three main parts: wheeled robot, tracked robot, and legged robot.[^1] Wheeled robots are one of the most frequently seen robots in human world. Due to their easy locomotion design and low cost of energy, the application fields of wheeled robots are various, such as autonomous transpotation in warehouse, last-mile delivery in the logistics industry, and service provider in service industry.[^2] With a higher cost of efficiency, tracked robots provide a better mobility than wheeled platforms, which enables its deployment in various off-road tasks, such as disaster management, military operations, and agriculture.[^3] 

However, some significant drawbacks of wheeled and tracked robots drived researchers to explore a new mobile system: legged robots. While wheels are exceling on prepared plain surfaces, tracks traversing through uneven terrains, there is still about half the earth’ surface unaccessible to them, whereas a large part of it can reachable by animals on foot.[^4] To be more specific, the problem for wheels and tracks is that they both need a continuous path of support, while legs are using isolated footholds for movement. This feature enables a legged system to overcome discrete or extremely rough terrains by generating the optimal foothold on a partially flat area, and a ladder serves as a good instance for this[^4]. Besides the traversability issue, factors such as biologically inspiration from animals also facilitated the development of legged robots.

The family of legged robots consists of several branches, among which the quadrupedal robot is the best choice related to mobility and stability of locomotion[^4]. Reasons are that the four-leggged structure provides better balancing and support for quadruped robots, and this structure is easier to design, control and maintain. 

#### Characteristics of Quadruped Robots

- mechanical legs provide the robots with excellent **maneuverability and versatility**
  which determine the core application performance such as job adaptability, walking speed, and load capacity
- Legged locomotion can extend the operational domain of robots to some of the most challenging environments on Earth. 



#### Development of Quadrupedal Robots

##### 1900s

##### Mid 1900s 

- First Autonomous Quadruped robot: phony pony, USA, 1960s
- A significant milestone in the quadruped robot’s development: inspired by spider, 1976

##### 2000s



##### Current Types

##### DOGZILLA S2 (I’m Here)

###### Why this?





## What is terrain tasks? 

Although wheeled robots and tracked robots can work efficiently in plane terrain, they can nearly impossible to function satisfactorily in cluttered, complex and hazardous environments. 

#### Why it is important in Legged Robot field?

#### What kinds of challenges are in terrain tasks?





## What are the methodologies to solve terrain tasks?

#### Type 1: Conventional Control Method

##### How Many Kinds of Control Method are used? 

##### How are They Achieved?

##### What They didn’t Achieve?

**Conventional Systems’ Drawback**

Overall, conventional systems for legged locomotion on rough terrain escalate in complexity as more scenarios are taken into account, have become extremely laborious to develop and maintain, and remain vulnerable to situations that are beyond the design implementation of their controller (corner cases). [[Learning quadrupedal locomotion over challenging terrain](https://doi.org/10.1126/scirobotics.abc5986)]

#### Type 2: Learning-Based Method (RL)

##### How Many Kinds of Learning-Based Method are used?

##### How are They Achieved?

##### How They are Superior to Convtentional Control Methods?

#### How RL Method is preferable?



## Related Works done by RL-method

#### Category A

##### Paper 1: [[Learning quadrupedal locomotion over challenging terrain](https://doi.org/10.1126/scirobotics.abc5986)]

This paper present a robust controller for blind quadrupedal locomotion in challenging natural environments / we present a robust controller for blind quadrupedal locomotion on challenging terrain

##### Paper 2: [ ]

…

…

#### Category B

#### Category C

#### …

#### Current Problems for RL-based Terrain Solutions

However, application of RL to legged locomotion has largely been confined to laboratory environments and conditions. Our prior work demonstrated end-to-end learning of locomotion and recovery behaviors, but only on flat ground, in the laboratory (*12*). [[Learning quadrupedal locomotion over challenging terrain](https://doi.org/10.1126/scirobotics.abc5986)]







[^1]: [A review of quadruped robots and environment perception](https://ieeexplore.ieee.org/abstract/document/7554355/)
[^2]: [Wheeled mobile robots: state of the art overview and kinematic comparison among three omnidirectional locomotion strategies](https://link.springer.com/article/10.1007/s10846-022-01745-7)
[^3]: [Analysis of an all-terrain tracked robot with innovative suspension system](https://www.sciencedirect.com/science/article/pii/S0094114X23000113)
[^4]: [Legged robots that balance](https://books.google.co.uk/books?hl=zh-CN&lr=&id=EXRiBnQ37RwC&oi=fnd&pg=PR10&dq=legged+robots+that+balance&ots=PdaruHI39_&sig=TX4bjzT8L0YSvu1sMlXnmQdqgCU)
