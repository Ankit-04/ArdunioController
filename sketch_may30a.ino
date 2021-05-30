
void setup() {
  pinMode(2,INPUT_PULLUP);
  pinMode(3,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);
  pinMode(5,INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int pin2 = digitalRead(2);
  int pin3 = digitalRead(3);
  int pin4 = digitalRead(4);
  int pin5 = digitalRead(5);
  Serial.println(String(pin2) + String(pin3) + String(pin4) + String(pin5));
  Serial.flush();
}
