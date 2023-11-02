# Related Works / Literature Review

> What is the difference between related works and literature Review?

## What is quadruped robots?

#### From Wheels to Legs 

In the last three decades, mobile robot has made much attention because of exploring the complex environment, space, rescure operation, accomplishing a task without human effort, etc. The mobile robot can be generally divided into three main parts: wheeled robot, tracked robot, and legged robot.[^1] Wheeled robots are one of the most frequently seen robots in human world. Due to their easy locomotion design and low cost of energy, the application fields of wheeled robots are various, such as autonomous transpotation in warehouse, last-mile delivery in the logistics industry, and service provider in service industry.[^2] With a higher cost of efficiency, tracked robots provide a better mobility than wheeled platforms, which enables its deployment in various off-road tasks, such as disaster management, military operations, and agriculture.[^3] 

However, some significant drawbacks of wheeled and tracked robots drived researchers to explore a new mobile system: legged robots. While wheels are exceling on prepared plain surfaces, tracks traversing through uneven terrains, there is still about half the earth’ surface unaccessible to them, whereas a large part of it can reachable by animals on foot.[^4] To be more specific, the problem for wheels and tracks is that they both need a continuous path of support, while legs are using isolated footholds for movement. This feature enables a legged system to overcome discrete or extremely rough terrains by generating the optimal foothold on a partially flat area, and a ladder serves as a good instance for this[^4]. Besides the traversability issue, factors such as biologically inspiration from animals also facilitated the development of legged robots.

The family of legged robots consists of several branches, among which the quadrupedal robot is the best choice related to mobility and stability of locomotion[^4]. Reasons are that the four-leggged structure provides better balancing and support for quadruped robots, and this structure is easier to design, control and maintain. 

However, it is worth mentioning that there is not a historic shift from wheeled and tracked to legged in the development of gound mobile robotics. In other words, all of these types of robots are popular in both research and industry field. However, this review will particularly focus on the robot’s traversability in challenging terrains, and there is indeed a logical shift from wheels to legs.



---

#### Characteristics of Quadruped Robots

In addition to the bio-inspired curiosity of creating a animal-like robot, researchers also put their thought on the potential advantage of quadruped robots over wheeled and tracked robots. Some of them are discussed below.



**Isolated Footholds**

As mentioned above, one biggest feature of a legged mechanism is that they use isolated footholds to control mainbody. This feature allows it to traverse through even the worst terrain, once optimal footholds are found.

**Active Suspension**

Another characteristic of a legged system is that they provide an active suspension, which means they can moderate the impact on mainbody to the minimum while traversing a complex terrain, by coordinating limb movement. This allows the payload to travel smoothly, and thus conducts desirable tasks such as collecting data, despite pronounced variation in the terrain. [^4] 

**Obstacle Surmounting**

The ability of overcoming obstacles might be unnecessary in mild terrains with obstacles, as the robot only needs to “avoid” them. However, the most challenging terrains (e.g., surrounded obstacles or gaps) requires robots to execute skillful behaviours such as leaping over a gap.[^5] Quadruped robots intrinsically possess execellent obstacle overcoming skills, simply by stepping on or jumping over the obstacles. In terms of moderate terrains (e.g., mild slope, low obstacles), this feature also improves the robot performance by reducing bump and body fluctuation.



In summary, due to its multi-limb, multi-degree of freedom feature, and discrete motion trajectory, quadruped robot is more maneuverable and adaptable in a unstructural environment and has better flexibility, stability, and fault tolerance than a wheeled or a tracked robot.



---

#### Development of Quadrupedal Robots

By sorting the development of quadrupedal robots, we can learn how those quadruped robots were developed, the background drive of the birth of today’s quadrupedal robots, and better understand the common design ideas that lies in the various quadrupedal robot structure.

##### 1900s

##### Mid 1900s 

- First Autonomous Quadruped robot: phony pony, USA, 1960s
- A significant milestone in the quadruped robot’s development: inspired by spider, 1976

##### 2000s



##### Current Types

> So far, the technological complexity to build and control such vehicles has prevented these systems from being applied in real world scenarios and only few teams managed to develop machines that work beyond laboratory test-bench settings
>
> With major advances over the recent years, pushed by various large scale research programs or investment from industry, our community is about to overcome the last technical hurdles and make legged robots available for real world applications.

##### DOGZILLA S2 (I’m Here)

###### Why this?





## What is terrain tasks? / Locomotion

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
[^5]: [Jumping over obstacles with MIT Cheetah 2](https://www.sciencedirect.com/science/article/abs/pii/S0921889020305431)
