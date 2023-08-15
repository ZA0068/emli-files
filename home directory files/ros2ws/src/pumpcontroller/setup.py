from setuptools import setup

package_name = 'pumpcontroller'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/pumpcontroller_launcher.py'])
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='EMLI_TEAM_24',
    maintainer_email='EMLI_TEAM_24@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller_node = pumpcontroller.controller_node:main', 
            'relay_node = pumpcontroller.relay_node:main',
            'state_node = pumpcontroller.state_node:main',
            'moist_publisher_node = pumpcontroller.moist_publisher_node:main',
            'pump_node = pumpcontroller.pump_node:main',
            'hourly_water_node = pumpcontroller.hourly_water_node:main',
            'alarm_publisher_node = pumpcontroller.alarm_publisher_node:main',
        ],
    },

)
