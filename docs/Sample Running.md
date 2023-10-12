# Sample Running

1. **Turn on the camera [√]**

   <img src="https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202310102245644.png" alt="image-20231010215134210" style="zoom: 25%;" />

2. **Color Recognition [√]**

   <img src="https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202310102245487.png" alt="image-20231010221521972" style="zoom: 25%;" />

3. Face Detection [√]
   <img src="https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202310102245790.png" alt="image-20231010221745393" style="zoom: 33%;" />

4. **Face Tracking [x]**

   Problem: cannot find the correct CaptureDeviceId number

   I don’t think it’s a essentail problem since other samples which used the camera works well.

5. Handshake on detecting face [√]

6. **Turn on the lidar [x]**

   input: pi@yahboom:~$ ros2 launch oradar_lidar ms200_scan_view.launch.py

   problem: Package 'oradar_lidar' not found: "package 'oradar_lidar' not found, searching: ['/opt/ros/foxy']"

   I think it’s the problem on the package not being sourced, so I need to check some ROS2 commands

7. **Voice module Test [x]**

   I don’t understand how samples in this module works. I tried calling it in thousands of ways, no responds.

   





## Problems

1. The camera stream delay is quite long. 
2. I need to get familiar with some ROS2 commands.

