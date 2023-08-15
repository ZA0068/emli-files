import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import subprocess

class MoistPublisherNode(Node):
    def __init__(self):
        super().__init__('moist_publisher_node')
        self.moisture_value_publisher = self.create_publisher(String, 'moisture', 10)
        self.light_value_publisher = self.create_publisher(String, 'light', 10)
        self.moist_status_publisher = self.create_publisher(Bool, 'dry', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.thresh_hold = 70.0
        
    def get_moisture_value_from_script(self):
        script_path = "/home/EMLI_TEAM_24/Scripts/SPI Pico/Sensors/moisture_sensor.sh"
        try:
            output = subprocess.check_output(['bash', script_path], text=True).strip()
            if not output:  # Check if the output is empty
                self.get_logger().error("moisture_sensor.sh returned an empty string.")
                return -1.0
            return float(output)
        except Exception as e:
            self.get_logger().error(f"Error executing moisture_sensor.sh: {e}")
            return -1.0
        
    def get_light_value_from_script(self):
        script_path = "/home/EMLI_TEAM_24/Scripts/SPI Pico/Sensors/light_sensor.sh"
        try:
            output = subprocess.check_output(['bash', script_path], text=True).strip()
            if not output:
                return -1.0
            return float(output)
        except Exception as e:
            raise e
        
    def timer_callback(self):
        moisture_msg = String()
        light_msg = String()
        moist_msg = Bool()
        
        moisture_value = self.get_moisture_value_from_script()
        if moisture_value > 0.0:
            moisture_msg.data = str(moisture_value)
            self.moisture_value_publisher.publish(moisture_msg)
            moist_msg.data = moisture_value < self.thresh_hold
            self.moist_status_publisher.publish(moist_msg)
            
        light_value = self.get_light_value_from_script()
        if light_value > 0.0:
            light_msg.data = str(light_value)
            self.light_value_publisher.publish(light_msg)


def main(args=None):
    rclpy.init(args=args)
    moist_publisher = MoistPublisherNode()
    rclpy.spin(moist_publisher)
    moist_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()