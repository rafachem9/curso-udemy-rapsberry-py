void setup(){
  Serial.begin(9600);
  pinMode(8,OUTPUT);
}

void loop(){
  if(Serial.available()>0){
    char c = Serial.read();
    if (c == 'a'){
      digitalWrite(8,HIGH);
    }else if (c=='b') {
      digitalWrite(8,LOW);
      
    }
  }

}
