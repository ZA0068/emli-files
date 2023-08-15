import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import subprocess

class AlarmPublisherNode(Node):
    def __init__(self):
        super().__init__('alarm_publisher_node')
        self.plant_alarm_publisher = self.create_publisher(Bool, 'plant_alarm', 10)
        self.pump_alarm_publisher = self.create_publisher(Bool, 'pump_alarm', 10)
        self.path = "/home/EMLI_TEAM_24/Scripts/SPI Pico/Sensors/"
        self.timer = self.create_timer(0.5, self.publish_alarms)

    def execute_script(self, script_name):
        command = ['bash', self.path + script_name]
        try:
            output = subprocess.check_output(command, timeout=5).strip()
            if not output:
                return -1
            value = int(output)
            return value
        except:
            return -1


    def publish_alarms(self):
        plant_alarm_msg = Bool()
        pump_alarm_msg = Bool()
        
        plant_alarm_status = self.execute_script('plant_alarm_sensor.sh')
        if plant_alarm_status != -1:
            plant_alarm_msg.data = bool(plant_alarm_status)
            self.plant_alarm_publisher.publish(plant_alarm_msg)
        
        pump_alarm_status = self.execute_script('pump_alarm_sensor.sh')
        if pump_alarm_status != -1:
            pump_alarm_msg.data = not bool(pump_alarm_status)
            self.pump_alarm_publisher.publish(pump_alarm_msg)

def main(args=None):
    rclpy.init(args=args)
    alarm_publisher = AlarmPublisherNode()
    rclpy.spin(alarm_publisher)
    alarm_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
