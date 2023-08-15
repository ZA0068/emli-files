import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool

class StateNode(Node):
    def __init__(self):
        super().__init__('state_node')
        self.initialize_states()
        self.create_subscribers_and_publishers()
        self.timer = self.create_timer(1.0, self.update_states_and_publish)

    def initialize_states(self):
        self.alarm_state = False
        self.plant_alarm_state = False
        self.pump_alarm_state = False
        self.pump_12hr = False
        self.pump_if_dry = False
        self.one_hour_passed = False
        self.is_dry = False
        self.motor_status = False

    def create_subscribers_and_publishers(self):
        self.pump_control_subscriber = self.create_subscription(Bool, 'pump_control', self.pump_control_callback, 10)
        self.plant_alarm_subscriber = self.create_subscription(Bool, 'plant_alarm', self.plant_alarm_callback, 10)
        self.pump_alarm_subscriber = self.create_subscription(Bool, 'pump_alarm', self.pump_alarm_callback, 10)
        self.subscriber_12h = self.create_subscription(Bool, 'twelve_hours_check', self.pump_12_h, 10)
        self.subscriber_1h = self.create_subscription(Bool, 'one_hour_check', self.one_hour_check_callback, 10)
        self.moisture_subscriber = self.create_subscription(Bool, 'dry', self.dry_callback, 10)

        self.alarm_publisher = self.create_publisher(Bool, 'alarm', 10)
        self.pump_publisher = self.create_publisher(Bool, 'pump_activation', 10)
        self.timer = self.create_timer(0.5, self.update_states_and_publish)

    def one_hour_check_callback(self, msg):
        self.one_hour_passed = msg.data
        self.update_pump_if_dry()

    def dry_callback(self, msg):
        self.is_dry = msg.data
        self.update_pump_if_dry()

    def update_pump_if_dry(self):
        self.pump_if_dry = self.one_hour_passed and self.is_dry

    def pump_12_h(self, msg):
        self.pump_12hr = msg.data

    def pump_control_callback(self, msg):
        self.motor_status = msg.data

    def plant_alarm_callback(self, msg):
        self.plant_alarm_state = msg.data

    def pump_alarm_callback(self, msg):
        self.pump_alarm_state = msg.data

    def update_states_and_publish(self):
        pump_msg = Bool()
        alarm_msg = Bool()
        
        self.alarm_state = self.plant_alarm_state or self.pump_alarm_state

        if self.alarm_state:
            pump_msg.data = False
        else:
            pump_msg.data = self.motor_status or self.pump_12hr or self.pump_if_dry
            
        alarm_msg.data = self.alarm_state
        
        self.alarm_publisher.publish(alarm_msg)
        self.pump_publisher.publish(pump_msg)

def main(args=None):
    rclpy.init(args=args)
    state_node = StateNode()
    rclpy.spin(state_node)
    state_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
