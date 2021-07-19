// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int newButtonState;
bool lightOn = false;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  newButtonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed
  if (buttonState != newButtonState) {

    if (!lightOn) {
      lightOn = true;
      digitalWrite(ledPin, HIGH);
    } else {
    lightOn = false;
    digitalWrite(ledPin, LOW);
    }
  }
}
