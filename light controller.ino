int led1=3;
int led2=4;
int led3=5;
int led4=6;

char var;

void setup() {
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if(Serial.available())
  {
    var=Serial.read();

    if(var=='A')
    {
      digitalWrite(led1,HIGH);
    }
    if(var=='a')
    {
      digitalWrite(led1,LOW);
    }

    if(var=='B')
    {
      digitalWrite(led2,HIGH);
    }
    if(var=='b')
    {
      digitalWrite(led2,LOW);
    }

    if(var=='C')
    {
      digitalWrite(led3,HIGH);
    }
    if(var=='c')
    {
      digitalWrite(led3,LOW);
    }

    if(var=='D')
    {
      digitalWrite(led4,HIGH);
    }
    if(var=='d')
    {
      digitalWrite(led4,LOW);
    }
  }  
}
