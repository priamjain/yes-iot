void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(12,OUTPUT);
}
void loop() {
 if(Serial.available()){
  int x =Serial.read();
  Serial.println(x);
  if(x==49)digitalWrite(12,HIGH);
  else digitalWrite(12,LOW); 
 }
 }
