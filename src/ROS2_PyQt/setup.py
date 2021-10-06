import os
from glob import glob
from setuptools import setup

package_name = 'ROS2_PyQt'
submodules = 'ROS2_PyQt/submodules'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files. This is the most important line here!
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='memoor',
    maintainer_email='memo.or99@hotmail.com',
    description='ROS2 nodes with GUI threading',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'start = ROS2_PyQt.main_gui:main'
        ],
    },
)
