import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'warehouse_gz'

def generate_data_files():
    data_files = [
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sim.launch.py']),
        ('share/' + package_name + '/launch', ['launch/spawn.launch.py']),
        ('share/' + package_name + '/launch', ['launch/gazebo_model.launch.py']),
        ('share/' + package_name + '/config', ['config/warehouse.yaml']),
        ('share/' + package_name + '/config', ['config/bridge_parameters.yaml']),
        ('share/' + package_name + '/maps', glob('maps/*.map')),
        ('share/' + package_name + '/worlds', []),
        (
            'share/' + package_name + '/warehouse_gz',
            ['warehouse_gz/gen_world.py', 'warehouse_gz/map_utils.py'],
        ),
    ]
    for root, dirs, files in os.walk('models'):
        for file in files:
            data_files.append((os.path.join('share', package_name, root), [os.path.join(root, file)]))
    return data_files

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=generate_data_files(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dan',
    maintainer_email='Danweiner9@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'fleet_controller = warehouse_gz.robot_controller:main',
            'demo_dynamic_tasks = warehouse_gz.demo_dynamic_tasks:main',
            'demo_dynamic_robots = warehouse_gz.demo_dynamic_robots:main',
        ],
    },
)
