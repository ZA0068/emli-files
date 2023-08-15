from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='plotlogger',
            executable='logger_node',
            name='logger_node'
        ),
        Node(
            package='plotlogger',
            executable='plotter_node',
            name='plotter_node'
        ),
    ])