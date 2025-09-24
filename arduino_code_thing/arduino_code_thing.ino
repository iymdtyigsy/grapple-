String command;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT); // Tube control pin
  pinMode(3, OUTPUT); // Oil control pin
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "TUBE_ON") {
      digitalWrite(2, HIGH);
      Serial.println("TUBE_DOWN");
    }
    else if (command == "TUBE_OFF") {
      digitalWrite(2, LOW);
      Serial.println("TUBE_UP");
    }
    else if (command == "OIL_ON") {
      digitalWrite(3, HIGH);
      Serial.println("OIL_STARTED");
    }
    else if (command == "OIL_OFF") {
      digitalWrite(3, LOW);
      Serial.println("OIL_STOPPED");
    }
  }
}
