// declare constants and variables
const int ledBattery = A2;
const int ledBatteryOut = 10;

int batteryValue = 100;
int batteryOut = 0;

const int ledInPin = A3;
const int led1outPin = 3;

int led1value = 0;
int led1out = 0;


const int ledIn2Pin = A3;
const int led2outPin = 5;

int led2value = 0;
int led2out = 0;

const int ledIn3Pin = A3;
const int led3outPin = 6;

int led3value = 0;
int led3out = 0;


void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  // diclare pin mode
  pinMode(led3outPin, OUTPUT);
  pinMode(led2outPin, OUTPUT);
  pinMode(led1outPin, OUTPUT);
  pinMode(ledBatteryOut, OUTPUT);
  attachInterrupt(10, indicator , RISING); 
  
}

void loop() {
  led1out = 254;
  // default interrupt setting
  digitalWrite(ledBatteryOut, LOW);
  // power saver when battery is lower than 0.75V or 154 units
  // read the analog in value:
  led1value = analogRead(ledInPin);
  // read battery value 
  batteryValue = analogRead(ledBattery);
   
  // map it to the range of the analog out:
  batteryOut = map(batteryValue, 0, 1023, 0, 255);

  
  // led1out = map(led1value, 0, 1023, 0, 255);
  // power indicator intensity if battery is 15% or lower
   if (batteryValue <= 154 ) {
    digitalWrite(ledBatteryOut, HIGH);
     led1out = 127;
   }
  /*}else{
    led1out = 254; //check
    analogWrite(ledBatteryOut, 0);
  } */
  
  
  // change the analog out value:
  if (led1value < 341 && led1value > 0){
    analogWrite(led1outPin, led1out);
    analogWrite(led2outPin, 0);
    analogWrite(led3outPin, 0);
    
  } else if (led1value >= 341 && led1value < 682){
    analogWrite(led1outPin, led1out);
    analogWrite(led2outPin, led1out);
    analogWrite(led3outPin, 0);
  } else if (led1value >= 682){
    analogWrite(led1outPin, led1out);
    analogWrite(led2outPin, led1out);
    analogWrite(led3outPin, led1out);
  }else{
    analogWrite(led1outPin, 0);
    analogWrite(led2outPin, 0);
    analogWrite(led3outPin, 0);
  }

  // print the results to the serial monitor:
  float voltageSensor = led1value * (5.0 / 1024.0);
  float voltageBattery = batteryValue * (5.0 / 1024.0);
  // print sensor
  Serial.print("sensor Units= ");
  Serial.print(led1value);
  Serial.print("\t sensor Voltage= ");
  Serial.print(voltageSensor);
  Serial.print("\t output = ");
  Serial.println(led1out);
 // print battery
  Serial.print("Battery Units = ");
  Serial.print(batteryValue);
  Serial.print("\t Battery Voltage= ");
  Serial.print(voltageBattery);
  Serial.print("\t Current = ");
  Serial.println(batteryOut);

  delay(1000);
}

void indicator(){                    
    led1out = 127;
    analogWrite(ledBatteryOut, 127);
}                             
