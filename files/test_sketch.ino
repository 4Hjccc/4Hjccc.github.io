
#include <Servo.h>
Servo myservo;

int pos = 0;    // variable to store the servo position
int label;
int waiting=1;

void setup() {
  Serial.begin(9600);
  Serial.write("Sketch begins.\r\n");
  Serial.flush();
  myservo.attach(9);
  myservo.write(60);
}

void loop() {

  if (Serial && Serial.available()) {

    label = Serial.read();
    
    if (waiting == 1) {
      waiting=0;
      //       Serial.flush();
      //      analogWrite(redPin, color[0]);
      if (label == 49) {
        myservo.write(0);
        delay(2000);
        for (pos = 0; pos <= 75; pos += 1) { // goes from 0 degrees to 180 degrees
          // in steps of 1 degree
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(5);                       // waits 15ms for the servo to reach the position
        }
        delay(1000);
        Serial.write("Label 1 detected.\r\n");
      }

      else if (label == 50) {
        myservo.write(180);
        delay(2000);
        for (pos = 180; pos <= 75; pos -= 1) { // goes from 0 degrees to 180 degrees
          // in steps of 1 degree
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(20);                       // waits 15ms for the servo to reach the position
        }
        delay(1000);
        Serial.write("Label2 detected.\r\n");
      }
      while (Serial.available()) {
        Serial.println((char)label);
        int throwaway = Serial.read();
        Serial.write("Throwing away.\r\n");
      }

      Serial.flush();
      
    }
  }
  else {
    //    Serial.println("asdf");
    waiting=1;
    for (pos = 60; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(3);                       // waits 15ms for the servo to reach the position
    }
    for (pos = 90; pos >= 60; pos -= 1) { // goes from 180 degrees to 0 degrees
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(3);                       // waits 15ms for the servo to reach the position
    }
//    delay(200);
  }

  
}
