import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, ExecuteProcess


def generate_launch_description():

    pkg_share = get_package_share_directory("uavcollab")
    worlds_dir = os.path.join(pkg_share, "worlds")
    
    lst = pkg_share.split('/')
    
    del lst[-4:]
    lst+=["src","uavcollab"]
    pkg_share = "/".join(lst)
    worlds_dir=pkg_share+"/worlds"

    old_resource_path = os.environ.get("GZ_SIM_RESOURCE_PATH", "")
    
    del lst[-3:]
    my_path = "/".join(lst)
    


    px4_autopilot_dir = os.path.expanduser("/home/abhinava/PX4-Autopilot")  # adjust to your actual path
    px4_gz_models = px4_autopilot_dir + "/Tools/simulation/gz/models"
    px4_gz_worlds = px4_autopilot_dir + "/Tools/simulation/gz/worlds"

    
    gz_resource_path = os.pathsep.join(filter(None, [
        worlds_dir,
        pkg_share,
        px4_gz_models,
        px4_gz_worlds,
    ]))
    return LaunchDescription([
        SetEnvironmentVariable(
            name="GZ_SIM_RESOURCE_PATH",
            value=gz_resource_path,

        ),

        ExecuteProcess(
            cmd=[
                "gz", "sim", "-r",
                os.path.join(worlds_dir, "model.sdf")
            ],
            output="screen"
        )
    ])
