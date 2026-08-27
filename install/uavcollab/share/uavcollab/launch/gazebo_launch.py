import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, ExecuteProcess


def generate_launch_description():

    pkg_share = get_package_share_directory("uavcollab")
    worlds_dir = os.path.join(pkg_share, "worlds")

    old_resource_path = os.environ.get("GZ_SIM_RESOURCE_PATH", "")

    gz_resource_path = os.pathsep.join(filter(None, [
        worlds_dir,
        pkg_share,
        
    ]))

    return LaunchDescription([
        SetEnvironmentVariable(
            name="GZ_SIM_RESOURCE_PATH",
            value="/media/$USER/2454fe4a-d2e4-460e-b4f5-df3cde6b9592/training_pool/src/uavcollab/worlds"
        ),

        ExecuteProcess(
            cmd=[
                "gz", "sim", "-r",
                os.path.join(worlds_dir, "model.sdf")
            ],
            output="screen"
        )
    ])