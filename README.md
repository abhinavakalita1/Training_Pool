this is for default world (world1.world)
ros2 launch uavcollab gazebo_launch.py 

this is world as an argument
ros2 launch uavcollab gazebo_launch.py world:=model.world (this launches nb_park_world)
ros2 launch uavcollab gazebo_launch.py world:=world1.world (this launches my_park_world)

run gedit ~/.bashrc
add the following:
export GZ_SIM_RESOURCE_PATH=$HOME/PX4-Autopilot/Tools/simulation/gz/models
export GZ_SIM_RESOURCE_PATH=$HOME/PX4-Autopilot/Tools/simulation/gz/worlds
export GZ_SIM_RESOURCE_PATH=$HOME/training_pool/src/uavcollab/worlds
save the file.
Open a new terminal and go to the PX4-Autopilot workspace
PX4_GZ_STANDALONE=1 PX4_SIM_MODEL=gz_x500 PX4_GZ_WORLD=my_park_world PX4_GZ_MODEL_POSE="-45,0,5,0,0,0" ./build/px4_sitl_default/bin/px4
change the name of the world file and initial starting position accordingly
