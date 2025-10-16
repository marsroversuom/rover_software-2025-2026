// define pins for motors
#define N_MOTORS 6
const int turn_on_pins[N_MOTORS] = {2, 4, 7, 8, 12, 13};
const int pwm_pins[N_MOTORS] = {3, 5, 6, 9, 10, 11};
// have a delay between each motor signal because without this it doesn't work
const int delay_ms = 2;

// since unsigned chars also range from 0 to 255 this is perfect to fetch duties for each of the 6 motors
// duties1 is duties[0] and etc
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

// duties ranges from 0 to 255
// 0 turns the motors CW while 255 CCW max speed. To stop use duties=127 or 128.
void run_left_motors(){
  digitalWrite(turn_on_pins[3], LOW);
  digitalWrite(turn_on_pins[4], LOW);
  digitalWrite(turn_on_pins[5], LOW);

  digitalWrite(turn_on_pins[0], HIGH);
  digitalWrite(turn_on_pins[1], HIGH);
  digitalWrite(turn_on_pins[2], HIGH);
  analogWrite(pwm_pins[0], duties[0]);
  analogWrite(pwm_pins[1], duties[1]);
  analogWrite(pwm_pins[2], duties[2]);
  delay(delay_ms);
}

void run_right_motors(){
  digitalWrite(turn_on_pins[0], LOW);
  digitalWrite(turn_on_pins[1], LOW);
  digitalWrite(turn_on_pins[2], LOW);

  digitalWrite(turn_on_pins[3], HIGH);
  digitalWrite(turn_on_pins[4], HIGH);
  digitalWrite(turn_on_pins[5], HIGH);
  analogWrite(pwm_pins[3], duties[3]);
  analogWrite(pwm_pins[4], duties[4]);
  analogWrite(pwm_pins[5], duties[5]);
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
  run_left_motors();
  run_right_motors();
}
