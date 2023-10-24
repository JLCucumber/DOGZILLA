# Week 7_Coding



Connecting [done]



## Test Lidar Module



Check launch file content of lidar

- Structure:

![image-20231023205737453](../../../../../AppData/Roaming/Typora/typora-user-images/image-20231023205737453.png)





**Error: 'oradar_lidar' not found: "package 'oradar_lidar' not found, searching: ['/opt/ros/foxy']"**

> <img src="../../../../../AppData/Roaming/Typora/typora-user-images/image-20231023211649838.png" alt="image-20231023211649838" style="zoom: 50%;" />

- Fix: Build the environment (ROS 2)

  - `cd ~/cartographer_ws2`

  - `colcon build`， should see something like this:
    - <img src="../../../../../AppData/Roaming/Typora/typora-user-images/image-20231023211917726.png" alt="image-20231023211917726" style="zoom:33%;" />
  - `source install/setup.bash`





#### \*\*\***Problem: can not connect to lidar device**

> <img src="../../../../../AppData/Roaming/Typora/typora-user-images/image-20231023213728111.png" alt="image-20231023213728111" style="zoom:50%;" />

Tried fix methods:

1. change variable names into recommended styles (Don’t think will work)

Things to remember:

1. Every time you modify something: rebuild the workspace, and update source



#### Problem: colcon build fail [fixed]

> <img src="../../../../../AppData/Roaming/Typora/typora-user-images/image-20231024110852000.png" alt="image-20231024110852000" style="zoom: 33%;" />
>
> <img src="../../../../../AppData/Roaming/Typora/typora-user-images/image-20231024110923838.png" alt="image-20231024110923838" style="zoom:33%;" />
>
> F**ixed by using RealVNC rather than use Putty.**
>
> <img src="../../../../../AppData/Roaming/Typora/typora-user-images/image-20231024114315161.png" alt="image-20231024114315161" style="zoom:33%;" />
>
> 



> ### Running Lidar Sample [Skip]
>
> > OK… let’s stop doing that and try to run the simplist sample given by the lidar README, instead of the dog README
> >
> > 1. Build
> >
> > <img src="../../../../../AppData/Roaming/Typora/typora-user-images/image-20231024113008039.png" alt="image-20231024113008039" style="zoom:50%;" />
> >
> > 2. Skip this test

























Test Obstacle Avoidance



