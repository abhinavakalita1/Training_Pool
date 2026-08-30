"""
Bridges ROS 2 <-> Gazebo topics for the ackermann_rover model.

Run this in a SEPARATE terminal, after gz sim is already running with either
world (model.world or world1.world) — same pattern as PX4 connecting to the
running gz server. This launch file doesn't care which world is up; it only
talks to whatever model is publishing on /model/<model_name>/... in Gazebo,
so it works unmodified for both.

Usage:
    ros2 launch uavcollab ackermann_bridge_launch.py
    ros2 launch uavcollab ackermann_bridge_launch.py model_name:=ackermann_rover

Then drive it:
    ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0}, angular: {z: 0.2}}"
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
    ros2 topic echo /odom
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    model_name_arg = DeclareLaunchArgument(
        "model_name",
        default_value="ackermann_rover",
        description="Name of the Ackermann model as defined in the .world file "
                     "(the <model name=\"...\"> in model.world / world1.world).",
    )
    model_name = LaunchConfiguration("model_name")

    bridge_node = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        name="cmd_vel",
        output="screen",
        arguments=[
            # ROS -> Gazebo: drive commands
            [
                "/model/", model_name, "/cmd_vel",
                "@geometry_msgs/msg/Twist",
                "[gz.msgs.Twist",
            ],
            # Gazebo -> ROS: odometry
            [
                "/model/", model_name, "/odometry",
                "@nav_msgs/msg/Odometry",
                "]gz.msgs.Odometry",
            ],
            # Gazebo -> ROS: tf
            [
                "/model/", model_name, "/pose",
                "@tf2_msgs/msg/TFMessage",
                "]gz.msgs.Pose_V",
            ],
        ],
        remappings=[
            (["/model/", model_name, "/cmd_vel"], "/cmd_vel"),
            (["/model/", model_name, "/odometry"], "/odom"),
            (["/model/", model_name, "/pose"], "/tf"),
        ],
    )

    return LaunchDescription([
        model_name_arg,
        bridge_node,
    ])
