import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from std_msgs.msg import String

class RelayNode(Node):
    def __init__(self):
        super().__init__('relay_node')
        self.subscription_alarm = self.create_subscription(
            Bool,
            'alarm',
            self.alarm_callback,
            10
        )
        self.subscription_moisture = self.create_subscription(
            Bool,
            'dry',
            self.moisture_callback,
            10
        )
        self.alarm = False
        self.dry = False
        self.publisher = self.create_publisher(String, 'led_state', 10)
        self.timer = self.create_timer(0.5, self.publish_led_state)

    def alarm_callback(self, msg):
        if msg.data:
            self.alarm = True
        else:
            self.alarm = False
            
    def moisture_callback(self, msg):
        if msg.data:
            self.dry = True
        else:
            self.dry = False
        
    def publish_led_state(self):
        msg = String()
        if self.alarm:
            msg.data = "red"
        elif self.dry and not self.alarm:
            msg.data = "yellow"
        else:
            msg.data = "green"
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RelayNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()