#include <ros.h>
#include <std_msgs/UInt16.h>
#include "Adafruit_VL53L1X.h"
#define USE_USBCON
#define IRQ_PIN 2
#define XSHUT_PIN 3
ros::NodeHandle nh;

std_msgs::UInt16 Int;
ros::Publisher range("range",&Int);

Adafruit_VL53L1X vl53 = Adafruit_VL53L1X(XSHUT_PIN, IRQ_PIN);
void setup()
{
  nh.initNode();
  nh.advertise(range);
  Adafruit_VL53L1X vl53 = Adafruit_VL53L1X(XSHUT_PIN, IRQ_PIN);
}

void loop()
{  
  int16_t distance;


  if (vl53.dataReady()) {
    // new measurement for the taking!
    distance = vl53.distance();
    
  Int.data = distance;
  range.publish( Int.data );
  nh.spinOnce();
  delay(1000);
}
}
