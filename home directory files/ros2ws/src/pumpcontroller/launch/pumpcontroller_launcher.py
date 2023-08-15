from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pumpcontroller',
            executable='controller_node',
            name='controller_node',
        ),
        Node(
            package='pumpcontroller',
            executable='alarm_publisher_node',
            name='alarm_publisher_node',
        ),
        Node(
            package='pumpcontroller',
            executable='state_node',
            name='state_node',
        ),
        Node(
            package='pumpcontroller',
            executable='relay_node',
            name='relay_node',
        ),
        Node(
            package='pumpcontroller',
            executable='pump_node',
            name='pump_node',
        ),
        Node(
            package='pumpcontroller',
            executable='hourly_water_node',
            name='hourly_water_node',
        ),
        Node(
            package='pumpcontroller',
            executable='moist_publisher_node',
            name='moist_publisher_node',
        )
    ])