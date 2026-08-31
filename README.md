***Setup***

**Clone this repo in your workspace and build the package**

```cd ros2_ws ```

```git clone https://github.com/abhinavakalita1/Training_Pool.git ```

```colcon build ```


this is for default world (world1.world)
<br>
```ros2 launch uavcollab gazebo_launch.py ```

this is world as an argument<br>
```ros2 launch uavcollab gazebo_launch.py world:=model.world``` (this launches nb_park_world)<br>
```ros2 launch uavcollab gazebo_launch.py world:=world1.world ```(this launches my_park_world)
<br><br>
run ```gedit ~/.bashrc```<br><br>
add the following:<br>
```export GZ_SIM_RESOURCE_PATH=$HOME/PX4-Autopilot/Tools/simulation/gz/models```<br>
```export GZ_SIM_RESOURCE_PATH=$HOME/PX4-Autopilot/Tools/simulation/gz/worlds```<br>
```export GZ_SIM_RESOURCE_PATH=$HOME/training_pool/src/uavcollab/worlds```
<br><br>
save the file.<br><br>
Open a new terminal and go to the PX4-Autopilot workspace<br>t
```PX4_GZ_STANDALONE=1 PX4_SIM_MODEL=gz_x500 PX4_GZ_WORLD=my_park_world PX4_GZ_MODEL_POSE="-45,0,5,0,0,0" ./build/px4_sitl_default/bin/px4```<br>
change the name of the world file and initial starting position accordingly
