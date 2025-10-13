int in1 = 5;

void setup() {
  pinMode(in1, OUTPUT);
  digitalWrite(in1, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readString();
    command.trim();
    if (command == "ptt_on") {
      digitalWrite(in1, HIGH);
    } else if (command == "ptt_off") {
      digitalWrite(in1, LOW);
    }
  }
}
