// define pins for motors
#define N_MOTORS 6
const int turn_on_pins[N_MOTORS] = {2, 4, 7, 8, 12, 13};
const int pwm_pins[N_MOTORS] = {3, 5, 6, 9, 10, 11};
// have a delay between each motor signal because without this it doesn't work
const int delay_ms = 2;

// since unsigned chars also range from 0 to 255 this is perfect to fetch duties for each of the 6 motors
// duty1 is duties[0] and etc
unsigned char duties[6] = {127, 127, 127, 127, 127, 127};

void setup() {
  for(int i = 0; i < N_MOTORS; i ++){
    pinMode(pwm_pins[i], OUTPUT);
    pinMode(turn_on_pins[i], OUTPUT);
  }
  Serial.begin(9600);
}

// Turning motors is also sort of convoluted, this works, not entirely sure why
// The signals from motor 1 and motor 2 interfere with eachother as they are controlled with the same driver (this shouldn't happen really)
// This is a workaround

// duty ranges from 0 to 255
// 0 turns the motors CW while 255 CCW max speed. To stop use duty=127 or 128.

void run_motor(int motor_number, int duty){
  for(int i = 0; i < N_MOTORS; i ++){
    if(i != motor_number){
      digitalWrite(turn_on_pins[i], LOW);
    }
  }
  // if(duty == 127){
  //   digitalWrite(turn_on_pins[motor_number], LOW);
  // }
  // else{
    digitalWrite(turn_on_pins[motor_number], HIGH);
    analogWrite(pwm_pins[motor_number], duty);
  // }
  delay(delay_ms);
}

void loop() {
  // Check if there are at least 6 bytes available in the serial buffer
  if (Serial.available() >= N_MOTORS) {
    // Read 6 bytes and store them into the duties array
    for (int i = 0; i < N_MOTORS; i++) {
      duties[i] = Serial.read(); // Store each byte into the duties array
    }
  }
  
  for(int i = 0; i < N_MOTORS; i ++){
    run_motor(i, duties[i]);
  }
}
