import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import subprocess

class PumpNode(Node):

    def __init__(self):
        super().__init__('pump_node')
        self.subscription = self.create_subscription(
            Bool,
            'pump_activation',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        if msg.data: 
            self.execute_pump_request_script()

    def execute_pump_request_script(self):
        script_path = "/home/EMLI_TEAM_24/Scripts/SPI Pico/Actuators/pump_request.sh"
        try:
            subprocess.run(["bash", script_path], check=True)
            self.get_logger().info("Pump request script executed successfully.")
        except subprocess.CalledProcessError as e:
            self.get_logger().error(f"Error executing pump request script: {e}")

def main(args=None):
    rclpy.init(args=args)
    pump_node = PumpNode()
    rclpy.spin(pump_node)
    pump_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()