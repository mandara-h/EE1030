void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  double sum=0;
  int count=10;
  while(count>0){
    Serial.println((analogRead(A0)*5)/1023.0,3);
    sum+=(analogRead(A0)*5)/1023.0;
    count--;
    delay(1000);
  }
    Serial.print("Average value: ");
    Serial.println(sum/10,3);
    delay(1000);
}
