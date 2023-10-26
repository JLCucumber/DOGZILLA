# **Learning quadrupedal locomotion over challenging terrain**

> [[Learning quadrupedal locomotion over challenging terrain](https://doi.org/10.1126/scirobotics.abc5986)]

**Conventional Systems’ Drawback**

Overall, conventional systems for legged locomotion on rough terrain escalate in complexity as more scenarios are taken into account, have become extremely laborious to develop and maintain, and remain vulnerable to situations that are beyond the design implementation of their controller (corner cases). 



**Reinforcement Learning’s Drawback**

However, application of RL to legged locomotion has largely been confined to laboratory environments and conditions. Our prior work demonstrated end-to-end learning of locomotion and recovery behaviors, but only on flat ground, in the laboratory (*12*). [[Learning quadrupedal locomotion over challenging terrain](https://doi.org/10.1126/scirobotics.abc5986)]



**Their work**

This paper present a robust controller for blind quadrupedal locomotion in challenging natural environments / we present a robust controller for blind quadrupedal locomotion on challenging terrain

-  uses only proprioceptive measurements from **joint encoders and an inertial measurement unit**

  -  the most durable and reliable sensors on legged machines. 

- we used a sequence model, specifically a **temporal convolutional network (TCN)** 

  - produces actuation based on an extended history of proprioceptive states.

  - Common in prior work:  using **a multilayer perceptron (MLP)** that operates on a snapshot of the robot’s current state

  -  learns to **implicitly** reason about contact and slippage events

    - not use **explicit** contact and slip estimation modules, which are known to lack robustness in challenging situations;

    

**Their Results**

- The controller is consistently effective in **zero-shot** generalization settings. 
- Simulation: rigid terrains and a small set of procedurally generated terrain profiles, such as hills and steps
- Physical: deformable terrains (mud, moss and snow), dynamic footholds (stepping on a rolling board), overground impediments (thick vegetation, rubble, gushing water)



**Prior Applications of Model-Free RL to Leged Locomotion**

> Prior efforts have established a number of practices for successful transfer of legged locomotion controllers from simulation to physical machines. 

1. J. Hwangbo, J. Lee, A. Dosovitskiy, D. Bellicoso, V. Tsounis, V. Koltun, M. Hutter, Learning agile and dynamic motor skills for legged robots. *Sci. Rob.* **4**, eaau5872 (2019

   > Realistic modeling of the physical system, including the actuators.

2. Z. Xie, P. Clary, J. Dao, P. Morais, J. Hurst, M. van de Panne, Learning locomotion skills for Cassie: Iterative design and sim-to-real, in *Conference on Robot Learning* (PMLR, 2019).

   > Vary parameters between simulation and reality

3. J. Tan, T. Zhang, E. Coumans, A. Iscen, Y. Bai, D. Hafner, S. Bohez, V. Vanhoucke, Sim-to-real: Learning agile locomotion for quadruped robots (Robotics: Science and Systems, 2018).

