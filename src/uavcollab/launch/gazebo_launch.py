import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution


def generate_launch_description():
    pkg_share = get_package_share_directory("uavcollab")

    lst = pkg_share.split('/')
    del lst[-4:]
    lst += ["src", "uavcollab"]
    pkg_share = "/".join(lst)
    worlds_dir = pkg_share + "/worlds"

    px4_autopilot_dir = os.path.expanduser("/media/divy/5c85a034-6379-4cd7-a75b-c4ed0b105d26/PX4/PX4-Autopilot")
    px4_gz_models = px4_autopilot_dir + "/Tools/simulation/gz/models"
    px4_gz_worlds = px4_autopilot_dir + "/Tools/simulation/gz/worlds"

    gz_resource_path = os.pathsep.join(filter(None, [
        worlds_dir,
        pkg_share,
        px4_gz_models,
        px4_gz_worlds,
    ]))

    world_arg = DeclareLaunchArgument(
        "world",
        default_value="world1.world",
        description="Name of the .world file (inside worlds/) to launch",
    )

    world_path = PathJoinSubstitution([worlds_dir, LaunchConfiguration("world")])

    return LaunchDescription([
        world_arg,
        SetEnvironmentVariable(
            name="GZ_SIM_RESOURCE_PATH",
            value=gz_resource_path,
        ),
        ExecuteProcess(
            cmd=["gz", "sim", "-r", world_path],
            output="screen",
        ),
    ])
