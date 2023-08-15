import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import os

class HourlyWaterNode(Node):
    def __init__(self):
        super().__init__('hourly_water_node')

        self.prev_value_12h = get_last_log_value("motorcontrol12h.log")
        self.prev_value_1h = get_last_log_value("motorcontrol1h.log")

        self.publisher_12h = self.create_publisher(Bool, 'twelve_hours_check', 10)
        self.publisher_1h = self.create_publisher(Bool, 'one_hour_check', 10)
        self.timer = self.create_timer(2, self.publish_values)


    def publish_values(self):
        msg_12 = Bool()
        msg_1 = Bool()

        current_value_12h = get_last_log_value("motorcontrol12h.log")
        msg_12.data = self.prev_value_12h != current_value_12h
        self.prev_value_12h = current_value_12h

        current_value_1h = get_last_log_value("motorcontrol1h.log")
        msg_1.data = self.prev_value_1h != current_value_1h
        self.prev_value_1h = current_value_1h

        self.publisher_12h.publish(msg_12)
        self.publisher_1h.publish(msg_1)

def get_last_log_value(log_file):
    script_file_path = "/home/EMLI_TEAM_24/log/" + log_file
    if not os.path.isfile(script_file_path):
        return 0

    with open(script_file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        return 0

    return int(lines[-1].strip())

def main(args=None):
    rclpy.init(args=args)
    hourly_water_node = HourlyWaterNode()
    rclpy.spin(hourly_water_node)
    hourly_water_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
