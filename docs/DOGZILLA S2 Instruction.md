# DOGZILLA S2 Instruction

> ==***read_ Battery()***: read the current battery power. If the reading is successful, an integer of 1-100 will be returned, representing the percentage of remaining battery power. If the reading fails, 0 will be returned.==

## 3. Remote Control Course

## 4. Kinematics Analysis Theory

## 5. Raspberry Pisystem Configration

### 5.1 Remote connect to DOGZILLA

#### SSH Remote Login

1. Read IP : **192.168.8.88**

   <img src="https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202310082239185.jpg" alt="fce1d05805f81385c57e1cb88618858" style="zoom: 10%;" />

   

2. **Putty SSH tool**
   Open the putty software and use the SSH service to remotely log in to the Raspberry Pi operating system.

   > SSH remote login needs to **ensure that the computer host and the Raspberry Pi are in the same LAN** before they can be used normally.
   >
   > If the Raspberry Pi is in hotspot mode, please **connect the computer to the hotspot signal of DOGZILLA.**

   <img src="https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202310082241694.png" alt="image-20231008224125625" style="zoom:50%;" />

​	Once connected, input  username: **pi**, and password: **yahboom**

​	Success !!

![image-20231009192616183](C:/Users/JLCucumber/AppData/Roaming/Typora/typora-user-images/image-20231009192616183.png)



### 5.2 Now let’s try to connect it by VNC

1. Open RealVNC Viewer, input 192.168.8.88
2. Get something like this, press continue
   <img src="C:/Users/JLCucumber/AppData/Roaming/Typora/typora-user-images/image-20231009192913271.png" alt="image-20231009192913271" style="zoom: 50%;" />

3. Then you need to input server passport: yahboom
4. There you go!

<img src="C:/Users/JLCucumber/AppData/Roaming/Typora/typora-user-images/image-20231009193052977.png" alt="image-20231009193052977" style="zoom: 25%;" />



### 5.3 How to run samples on Jupter Lab?

The use of the JupyterLab environment requires that the computer and the Raspberry Pi **be in the same LAN for normal use**. The DOGZILLA factory system starts the JupyterLab service by default.



1. Once connect to the Dog’s WiFi, input **on your computer** on the brouser DOGZILLA’s IP address: `192.168.8.88:8888` . And you should see something like this:
   ![image-20231009202033201](C:/Users/JLCucumber/AppData/Roaming/Typora/typora-user-images/image-20231009202033201.png)

2. Input password: yahboom. Then you’ll successfully enter the jupyter lab:
   ![image-20231009202516538](C:/Users/JLCucumber/AppData/Roaming/Typora/typora-user-images/image-20231009202516538.png)

3. Congratulations! Now you have get in contact to the python source code of DOGZILLA. Hopefully you can use them to do your programming stuff on this little dog.



### 5.4 How to transfer files between PC and Pi?

> Sometimes we need to transfer files between two different systems, Windows and Raspberry Pi. Since these are two different file systems, the so-called **ssh service needs to be used to transfer files across systems.**

1. install WinSCP, after installation, you should see something like this.
   <img src="C:/Users/JLCucumber/AppData/Roaming/Typora/typora-user-images/image-20231009194735404.png" alt="image-20231009194735404" style="zoom:33%;" />
2. Again, bear in mind of the IP address: **192.168.8.88**
3. Then, you need to login. Fill those blanks like this:
   - File protocol：Select SFTP for file protocol, 
   - Host name: IP address of Raspberry Pi, 
   - Port number: 22 by default, 
   - User name: username of Raspberry Pi (pi), 
   - Password: login password (yahboom).

> **Please note that you have to connect the DOGZILLA WIFI before hand.**

4. After logging in, you should see something on the right side page:
   ![image-20231009195337882](C:/Users/JLCucumber/AppData/Roaming/Typora/typora-user-images/image-20231009195337882.png)



#### 5.4.1 Use of file transfer

There are three operation modes for file transfer:

1. The first one is to directly **pull the file** from the left to the right, or from the right to the left, and the system will automatically copy a file for transmission.
2. The second is to select the file with the mouse, and then press the **F5** key, the selected file will be copied to the other side.
3. The third is to select the file and click the **right mouse button**. If it is transferred from the win computer to the Raspberry Pi, click **upload**.

If you upload a file from the Raspberry Pi to the win computer, press the right mouse button to select the file and select **Download**





### 5.5 Some networking stuff..

1. **What if I want to connect to another WiFi?**

   **Before connecting to the WiF**i signal, please press 10.3 to **turn off the hotspot signal**. 

   If you need to start up to connect to the WiFi signal, please follow 10.4 to turn off the hotspot mode.

2. Some more information…
   [DOGZILLA Instruction:  Hotspot mode and WiFi connection](http://www.yahboom.net/study/DOGZILLA)





### 5.6 Write System File…

you don’t really need to rewrite your raspberry Pi



## 6. OpenCV basic Course

## 7. DOGZILLA Control Course

### 7.1 Basic Control

The functions of the DOGZILLA Python library be used in this course:

- ***forward(step)***：Go forward, step is the step width. The larger the value, the larger the width of each step and the faster the speed. The step range is  [0, 25].
- ***back(step)***：Back, step is the step width. The larger the value, the larger the width of each step and the faster the speed. The step range is  [0, 25].
- ***left(step)***：Left translation, step is the step width. The larger the value, the larger the width of each step and the faster the speed. The step range is  [0, 18].
- ***right(step)***：Right translation, step is the step width. The larger the value, the larger the width of each step and the faster the speed. The step range is  [0, 18].
- ***turnleft(step)***: Spin left, step is the step width. The larger the value, the larger the width of each step and the faster the speed. The step range is  [0, 100].
- ***turnright(step)***：Spin right, step is the step width. The larger the value, the larger the width of each step and the faster the speed. The step range is  [0, 100].

- ***stop()***：Stop.



### 7.2 Gait Conditioning

**move(direction, step)**：Translate back and forth.

- direction：Input the string, input the range ['x ',' x ',' y ',' y '],' x 'or' x 'to move the robot dog forward or backward, and' y 'or' y 'to move the robot dog left or right.
- step：**Input range X: [- 25,25], Y: [- 18,18],** this parameter represents the translation step size. According to the direction, positive value represents forward or left shift, and negative value represents backward or right shift. When the input value exceeds the range, move according to the limit value.

**turn(step)**：Rotate.

- The remainder **range of step is [- 100, 100]**. This parameter represents the rotation speed, in ° / s. positive values are left turns and negative values are right turns.

**pace(mode)**：Change the step frequency, speed = step frequency x step width.

- mode：**Input string, input range ['normal ',' slow ',' high ']**, normal is the default step frequency, low is the slow step frequency, and high is the high-speed step frequency.



### 7.3 Body Control

The functions of dogzilla Python library involved in this course.

1. ***translation(direction, data)***：Body position translation.

   - direction：Single character or character list, 'x' represents back to back translation, 'y' represents back to left translation, 'z' represents height.

   - data：which means the translation distance of the fuselage position(mm). The value range is X: [- 35,35], Y: [- 18,18], Z: [75115]

2. ***attitude(direction, data)***：Fuselage attitude adjustment.

   - direction：Single character or character list, 'R' represents roll angle, 'p' represents pitch angle, 'y' represents yaw angle 

   - data：Represents the adjustment range of fuselage attitude, in °.r:[-20,20], p:[-15,15], y:[11,11]



### 7.4 Performing Actions

***action(action_id)***：Perform preset actions.

- action_id：Input range [1, 255], where 255 represents stopping the operation and restoring the initial posture; 1 ~ 19 correspond to 19 actions, and the corresponding relationship is shown in the following figure.

![image-20220823163407037](https://raw.githubusercontent.com/JLCucumber/HelloWorld/main/img/202310092107849.png)

***perform(mode)***：In the performance mode, the robot dog will cycle through the preset actions.

- mode：Pass in 1, open the action rotation, and perform the above actions in sequence. Pass in 0 and stop action rotation.



## 8. Advanced Course

## 9. Developer Mode

## 10. ROS Basic Course

## 11. ROS and OpenCV Visual Course

## 12. ROS robot dog basic

## 14. Lidar Course [TODO]



## 15. Voice Control [TODO]

