import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
from collections import deque
import subprocess

class PlotterNode(Node):
    def __init__(self):
        super().__init__('plotter_node')

        self.maxlen = 10
        
        self.data_queues = {
            'moisture': deque(maxlen=self.maxlen),
            'light': deque(maxlen=self.maxlen),
            'plant_alarm': deque(maxlen=self.maxlen),
            'alarm': deque(maxlen=self.maxlen),
            'pump_alarm': deque(maxlen=self.maxlen),
            'led_state': deque(maxlen=self.maxlen),
            'button_count': deque(maxlen=self.maxlen),
            'pump_control': deque(maxlen=self.maxlen),
            'pump_activation': deque(maxlen=self.maxlen),
            'one_hour_check': deque(maxlen=self.maxlen),
            'twelve_hours_check': deque(maxlen=self.maxlen)
        }
        self.led_state_mapping = {
            'red': 0,
            'yellow': 1,
            'green': 2
        }
        self.create_subscription(String, 'moisture', self.moisture_callback, 10)
        self.create_subscription(String, 'light', self.light_callback, 10)
        self.create_subscription(Bool, 'plant_alarm', self.plant_alarm_callback, 10)
        self.create_subscription(Bool, 'alarm', self.alarm_callback, 10)
        self.create_subscription(Bool, 'pump_alarm', self.pump_alarm_callback, 10)
        self.create_subscription(String, 'led_state', self.led_states_callback, 10)
        self.create_subscription(String, 'button_count', self.button_count_callback, 10)
        self.create_subscription(Bool, 'pump_control', self.pump_control_callback, 10)
        self.create_subscription(Bool, 'pump_activation', self.pump_activation_callback, 10)
        self.create_subscription(Bool, "one_hour_check", self.one_hour_callback, 10)
        self.create_subscription(Bool, "twelve_hours_check", self.twelve_hours_callback, 10)

        self.create_timer(0.5, self.publish_data_from_queues)

    def post_to_database(self, field, value):
        script_path = "/home/EMLI_TEAM_24/bin/Influx-database-logging/post_to_database.sh"
        database_name = "rpi_sensors"
        try:
            subprocess.run([script_path, field, str(value), database_name], check=True)
        except subprocess.CalledProcessError as e:
            self.get_logger().error(f"Failed to post data to InfluxDB: {e}")

    def moisture_callback(self, msg):
        self.data_queues['moisture'].append(float(msg.data))

    def light_callback(self, msg):
        self.data_queues['light'].append(float(msg.data))

    def plant_alarm_callback(self, msg):
        self.data_queues['plant_alarm'].append(msg.data)

    def alarm_callback(self, msg):
        self.data_queues['alarm'].append(msg.data)

    def pump_alarm_callback(self, msg):
        self.data_queues['pump_alarm'].append(msg.data)

    def led_states_callback(self, msg):
        if msg.data in self.led_state_mapping:
            mapped_value = self.led_state_mapping[msg.data]
            self.data_queues['led_state'].append(mapped_value)
        else:
            self.get_logger().warn(f"Received unexpected led_state value: {msg.data}")


    def button_count_callback(self, msg):
        self.data_queues['button_count'].append(msg.data)

    def pump_control_callback(self, msg):
        self.data_queues['pump_control'].append(msg.data)

    def pump_activation_callback(self, msg):
        self.data_queues['pump_activation'].append(msg.data)

    def one_hour_callback(self, msg):
        self.data_queues['one_hour_check'].append(msg.data)

    def twelve_hours_callback(self, msg):
        self.data_queues['twelve_hours_check'].append(msg.data)

    def publish_data_from_queues(self):
        for topic, data_deque in self.data_queues.items():
            if data_deque:
                self.post_to_database(topic, data_deque[-1])


def main(args=None):
    rclpy.init(args=args)
    plotter_node = PlotterNode()
    rclpy.spin(plotter_node)
    plotter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
