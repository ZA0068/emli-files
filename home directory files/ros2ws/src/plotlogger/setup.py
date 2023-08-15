from setuptools import setup

package_name = 'plotlogger'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/plotlogger_launcher.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='EMLI_TEAM_24',
    maintainer_email='EMLI_TEAM_24@todo.todo',
    description='Plots from the sensor values from Raspberry Pi Pico',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'logger_node = plotlogger.logger_node:main',
            'plotter_node = plotlogger.plotter_node:main',
        ],
    },
)