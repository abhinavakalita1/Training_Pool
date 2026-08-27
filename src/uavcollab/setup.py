import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'uavcollab'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
        data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include launch folder
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.[pxy][yma]*'))),
        
        # Include worlds root files (model.config and model.sdf)
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.*'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('urdf', '*.*'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('config', '*.*'))),
        
        # Explicitly map all your resource folders
        (os.path.join('share', package_name, 'worlds', 'meshes'), glob(os.path.join('worlds', 'meshes', '*'))),
        (os.path.join('share', package_name, 'worlds', 'thumbnails'), glob(os.path.join('worlds', 'thumbnails', '*'))),
        (os.path.join('share', package_name, 'worlds', 'thumbnails'), glob(os.path.join('worlds', 'materials', 'textures', '*'))),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='divy',
    maintainer_email='divysingh332@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # Exposes my_script.py as a ROS 2 node executable
            'my_script_node = uavcollab.my_script:main',
        ],
    },
)

