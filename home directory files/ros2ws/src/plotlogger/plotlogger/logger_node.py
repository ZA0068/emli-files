import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
from collections import deque
from datetime import datetime

class LoggerNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        self.log_file = '/home/EMLI_TEAM_24/log/sensorlogging.log'
        
        self.maxlen = 10
        self.data_queues = {
            'moisture': deque(maxlen=self.maxlen),
            'light': deque(maxlen=self.maxlen),
            'plant_alarm': deque(maxlen=self.maxlen),
            'alarm': deque(maxlen=self.maxlen),
            'pump_alarm': deque(maxlen=self.maxlen),
            'led_state': deque(maxlen=self.maxlen),
            'pump_control': deque(maxlen=self.maxlen),
            'button_count': deque(maxlen=self.maxlen),
            'pump_activation': deque(maxlen=self.maxlen),
            'one_hour_check': deque(maxlen=self.maxlen),
            'twelve_hours_check': deque(maxlen=self.maxlen),
            'dry': deque(maxlen=self.maxlen)
        }
        
        self.create_subscription(String, 'moisture', self.moisture_callback, 10)
        self.create_subscription(String, 'light', self.light_callback, 10)
        self.create_subscription(Bool, 'plant_alarm', self.plant_alarm_callback, 10)
        self.create_subscription(Bool, 'alarm', self.alarm_callback, 10)
        self.create_subscription(Bool, 'pump_alarm', self.pump_alarm_callback, 10)
        self.create_subscription(String, 'led_state', self.led_states_callback, 10)
        self.create_subscription(Bool, 'pump_activation', self.active_pump_callback, 10)
        self.create_subscription(String, 'button_count', self.button_state_callback, 10)
        self.create_subscription(Bool, 'pump_control', self.pump_control_callback, 10)
        self.create_subscription(Bool, "one_hour_check", self.one_hour_callback, 10)
        self.create_subscription(Bool, "twelve_hours_check", self.twelve_hours_callback, 10)
        self.create_subscription(Bool, 'dry', self.dry_callback, 10)
        
        self.create_timer(1, self.save_data_to_log)

    def append_data(self, topic_name, data):
        self.data_queues[topic_name].append(data)

    def moisture_callback(self, msg):
        self.append_data('moisture', f"Moisture value: {msg.data} %")

    def light_callback(self, msg):
        self.append_data('light', f"Light intensity: {msg.data} lux")

    def alarm_callback(self, msg):
        status = "active" if msg.data else "inactive"
        self.append_data('alarm', f"The alarm is {status}")

    def plant_alarm_callback(self, msg):
        status = "active" if msg.data else "inactive"
        self.append_data('plant_alarm', f"The plant alarm is {status}")

    def pump_alarm_callback(self, msg):
        status = "active" if msg.data else "inactive"
        self.append_data('pump_alarm', f"The pump alarm is {status}")

    def led_states_callback(self, msg):
        self.append_data('led_state', f"LED State: {msg.data}")

    def active_pump_callback(self, msg):
        status = "active" if msg.data else "inactive"
        self.append_data('pump_activation', f"Pump status: {status}")

    def button_state_callback(self, msg):
        self.append_data('button_count', f"Button press count: {msg.data}")

    def pump_control_callback(self, msg):
        status = "Activate" if msg.data else "Inactive"
        self.append_data('pump_control', f"Pump command: {status}")

    def one_hour_callback(self, msg):
        status = "Yes" if msg.data else "No"
        self.append_data('one_hour_check', f"Is one hour check active?: {status}")

    def twelve_hours_callback(self, msg):
        status = "Yes" if msg.data else "No"
        self.append_data('twelve_hours_check', f"Is twelve hours pump active?: {status}")

    def dry_callback(self, msg):
        status = "Dry" if msg.data else "Wet"
        self.append_data('dry', f"Moisture status: {status}")

    def save_data_to_log(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        separator = "-" * 80
        self.append_to_log(separator)
        for __topic__, data_deque in self.data_queues.items():
            if data_deque:
                log_entry = f"[{timestamp}] " + data_deque[-1]
                self.append_to_log(log_entry)

    def append_to_log(self, msg):
        with open(self.log_file, 'a') as f:
            f.write(msg + '\n')
        
        with open(self.log_file, 'r') as f:
            lines = f.readlines()
            if len(lines) > 9000:
                lines = lines[-9000:]
        
        with open(self.log_file, 'w') as f:
            f.writelines(lines)

def main(args=None):
    rclpy.init(args=args)
    logger_node = LoggerNode()
    rclpy.spin(logger_node)
    logger_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
