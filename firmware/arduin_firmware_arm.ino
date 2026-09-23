const int stepPin_1 = 2;
const int dirPin_1  = 5;
const int spr_j1    = 3200;

const int stepPin_2 = 3;
const int dirPin_2  = 6;

const int stepPin_3 = 4;
const int dirPin_3  = 7;
const int spr_j3    = 5600;

const int SPR = 5600 ;
const int SPEED = 400;  
const int MIN_SPEED = 1200; 
const int HOME_SPEED = 600;
const int enablePin = 8;

const int x_limpin = 9;
const int y_limpin = 10;
const int z_limpin = 11;

int pos1 = 0;
int pos2 = 0;
int pos3 = 0;


int stepPins[] = {stepPin_1, stepPin_2, stepPin_3};
int dirPins[]  = {dirPin_1, dirPin_2, dirPin_3};

void setup() {
  pinMode(enablePin, OUTPUT);
  digitalWrite(enablePin, LOW);

  pinMode(stepPin_1, OUTPUT);
  pinMode(stepPin_2, OUTPUT);
  pinMode(stepPin_3, OUTPUT);
  pinMode(dirPin_1,  OUTPUT);
  pinMode(dirPin_2,  OUTPUT);
  pinMode(dirPin_3,  OUTPUT);

  pinMode(x_limpin, INPUT_PULLUP);
  pinMode(y_limpin, INPUT_PULLUP);
  pinMode(z_limpin, INPUT_PULLUP);


  Serial.begin(115200);
}

//Homing of the joints:
void homing1(){
  digitalWrite(dirPin_1, LOW);
   while (digitalRead(x_limpin) == 1){
    digitalWrite(stepPin_1, HIGH);
    delayMicroseconds(MIN_SPEED);
    digitalWrite(stepPin_1, LOW);
    delayMicroseconds(MIN_SPEED);
  }

  digitalWrite(dirPin_1, HIGH);
  for(int i = 0; i > 250; i++){
    digitalWrite(stepPin_1, HIGH);
    delayMicroseconds(MIN_SPEED);
    digitalWrite(stepPin_1, LOW);
    delayMicroseconds(MIN_SPEED);
  }

  pos1 = 0;
}

void homing2(){
  digitalWrite(dirPin_2, LOW);
   while (digitalRead(y_limpin) == 1){
    digitalWrite(stepPin_2, HIGH);
    delayMicroseconds(HOME_SPEED);
    digitalWrite(stepPin_2, LOW);
    delayMicroseconds(HOME_SPEED);
  }

  digitalWrite(dirPin_2, HIGH);
  for(int i = 0; i > 250; i++){
    digitalWrite(stepPin_2, HIGH);
    delayMicroseconds(MIN_SPEED);
    digitalWrite(stepPin_2, LOW);
    delayMicroseconds(MIN_SPEED);
  }

  pos2 = 0;
}

void homing3(){
  digitalWrite(dirPin_3, HIGH);

  while (digitalRead(z_limpin) == 1){
    digitalWrite(stepPin_3, HIGH);
    delayMicroseconds(HOME_SPEED);
    digitalWrite(stepPin_3, LOW);
    delayMicroseconds(HOME_SPEED);
  }

  digitalWrite(dirPin_3, HIGH);
  for(int i = 0; i > 250; i++){
    digitalWrite(stepPin_3, HIGH);
    delayMicroseconds(MIN_SPEED);
    digitalWrite(stepPin_3, LOW);
    delayMicroseconds(MIN_SPEED);
  }

  pos3 = 0;
}

//Moving the joints:
void moveAllJointsSimultaneous(float deg1, float deg2, float deg3) {
  float degrees[] = {deg1, -deg2, deg3};
  long sollSteps[3];

  for (int i = 0; i < 3; i++) {
    long spr = (i == 0) ? spr_j1 : ((i == 2)? spr_j3:SPR);
    sollSteps[i] = round((degrees[i] / 360.0) * spr);
    
    digitalWrite(dirPins[i], sollSteps[i] > 0 ? LOW : HIGH);
  }

  long absSteps[3] = { abs(sollSteps[0]), abs(sollSteps[1]), abs(sollSteps[2]) };

  long maxSteps = max(absSteps[0], max(absSteps[1], absSteps[2]));

  if (maxSteps == 0) return;

  long accelSteps = maxSteps * 0.20;
  long decelSteps = accelSteps;

  long counter[3] = {0, 0, 0};

  for (long i = 0; i < maxSteps; i++) {
    
    int currentDelay;
    if (i < accelSteps) {
      currentDelay = map(i, 0, accelSteps, MIN_SPEED, SPEED);
    } else if (i < maxSteps - decelSteps) {
      currentDelay = SPEED;
    } else {
      currentDelay = map(i, maxSteps - decelSteps, maxSteps, SPEED, MIN_SPEED);
    }

    for (int j = 0; j < 3; j++) {
      if (absSteps[j] > 0) {
        counter[j] += absSteps[j];
        if (counter[j] >= maxSteps) {
          digitalWrite(stepPins[j], HIGH);
        }
      }
    }

    delayMicroseconds(currentDelay);

    for (int j = 0; j < 3; j++) {
      if (absSteps[j] > 0 && counter[j] >= maxSteps) {
        digitalWrite(stepPins[j], LOW);
        counter[j] -= maxSteps; 
      }
    }

    delayMicroseconds(currentDelay);
  }
  Serial.println("OK"); 
}

//processing python inputs:
void parseMultiCommand(String input) {
  input.trim();
  input.toLowerCase();
  input.replace("°", "");

  if (input.startsWith("home:")){
    String target = input.substring(5);
    target.trim();
 
    if (target == ("1")){
      homing1();
    }
    else if (target == ("2")){
      homing2();
    }
    else if (target == ("3")){
      homing3();
    }

    Serial.println("OK");
      return;
  }

  float deg1 = 0.0, deg2 = 0.0, deg3 = 0.0;

  int firstComma = input.indexOf(',');
  int secondComma = input.indexOf(',', firstComma + 1);

  if (firstComma != -1 && secondComma != -1) {
    String str1 = input.substring(0, firstComma);
    String str2 = input.substring(firstComma + 1, secondComma);
    String str3 = input.substring(secondComma + 1);

    
    if (str1.indexOf(':') != -1) str1 = str1.substring(str1.indexOf(':') + 1);
    if (str2.indexOf(':') != -1) str2 = str2.substring(str2.indexOf(':') + 1);
    if (str3.indexOf(':') != -1) str3 = str3.substring(str3.indexOf(':') + 1);

    deg1 = str1.toFloat();
    deg2 = str2.toFloat();
    deg3 = str3.toFloat();

    moveAllJointsSimultaneous(deg1, deg2, deg3);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    parseMultiCommand(input);
  }
}