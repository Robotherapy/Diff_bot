from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'diff_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Core package info
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),

        # Config files (YAML, etc.)
        (os.path.join('share', package_name, 'config'), glob('config/*')),

        # World files for Gazebo / Ignition
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),

        # Robot description (URDF, Xacro, meshes, etc.)
        (os.path.join('share', package_name, 'description'), glob('description/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robotherapy',
    maintainer_email='robotherapyy@gmail.com',
    description='Differential drive robot simulation and description package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Example: 'teleop_node = diff_bot.teleop:main',
        ],
    },
)

