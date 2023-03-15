#include <ros.h>
#include <std_msgs/String.h>
#include "Adafruit_VL53L1X.h"

#define IRQ_PIN 2
#define XSHUT_PIN 3
ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

char hello[13] = "hello world!";
Adafruit_VL53L1X vl53 = Adafruit_VL53L1X(XSHUT_PIN, IRQ_PIN);
void setup()
{
  nh.initNode();
  nh.advertise(chatter);
  Adafruit_VL53L1X vl53 = Adafruit_VL53L1X(XSHUT_PIN, IRQ_PIN);
}

void loop()
{  int16_t distance;

  if (vl53.dataReady()) {
    // new measurement for the taking!
    distance = vl53.distance();
    
  str_msg.data = distance;
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1000);
}
