#include <ros.h>
#include <std_msgs/Int32.h>
#include "Adafruit_VL53L1X.h"

#define IRQ_PIN 2
#define XSHUT_PIN 3
ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher range("chatter", Int32);

Adafruit_VL53L1X vl53 = Adafruit_VL53L1X(XSHUT_PIN, IRQ_PIN);
void setup()
{
  nh.initNode();
  nh.advertise(range);
  Adafruit_VL53L1X vl53 = Adafruit_VL53L1X(XSHUT_PIN, IRQ_PIN);
}

void loop()
{  int16_t distance;

  if (vl53.dataReady()) {
    // new measurement for the taking!
    distance = vl53.distance();
    
  str_msg.data = distance;
  range.publish(Int32);
  nh.spinOnce();
  delay(1000);
