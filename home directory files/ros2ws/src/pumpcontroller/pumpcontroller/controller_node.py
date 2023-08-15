import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import subprocess

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        
        self.button_count_publisher = self.create_publisher(String, 'button_count', 10)
        self.pump_control_publisher = self.create_publisher(Bool, 'pump_control', 10)
        self.led_subscription = self.create_subscription(String, 'led_state', self.led_listener_callback, 10)
        self.base_path = "/home/EMLI_TEAM_24/Scripts/ESP8266 remote controller/"
        self.timer = self.create_timer(0.5, self.button_state_callback)

    def button_state_callback(self):
        script_path = self.base_path + "get_button_count.sh"
        output = subprocess.check_output([script_path]).decode("utf-8").strip()
        
        button_count, motor_status = output.split(",")
        button_count = str(int(button_count.strip()))
        motor_status = bool(int(motor_status))

        button_msg = String()
        motor_activate_msg = Bool()
        
        button_msg.data = button_count
        motor_activate_msg.data = motor_status
        
        self.button_count_publisher.publish(button_msg)
        self.pump_control_publisher.publish(motor_activate_msg)

    def led_listener_callback(self, msg):        
        if "red" in msg.data:
            script_path = self.base_path + "switch_red.sh"
        elif "yellow" in msg.data:
            script_path = self.base_path + "switch_yellow.sh"
        else:
            script_path = self.base_path + "switch_green.sh"
        subprocess.run(['bash', script_path])

def main(args=None):
    rclpy.init(args=args)
    controller_node = ControllerNode()
    rclpy.spin(controller_node)
    controller_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()