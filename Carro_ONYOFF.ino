int estado=0;
int izqA = 5; 
int izqB = 6; 
int derA = 9; 
int derB = 10; 
int vel = 255;
int pecho=2;
int ptrig=3;
long duracion, distancia;
void setup(){
  Serial.begin(9600);
  pinMode(pecho, INPUT);
  pinMode(ptrig, OUTPUT);
  pinMode(derA, OUTPUT);
  pinMode(derB, OUTPUT);
  pinMode(izqA, OUTPUT);
  pinMode(izqB, OUTPUT);
}

void loop(){
 if(Serial.available()>0){
 estado = Serial.read();
 }
 if (estado =='1'){
   analogWrite(derB,0);
   analogWrite(izqB,0);
   analogWrite(derA,vel);
   analogWrite(izqA,vel);
  }
if(estado=='2'){
   analogWrite(derB,0);
   analogWrite(izqB,0);
   analogWrite(derA,0);
   analogWrite(izqA,vel);
  }
 if(estado=='3'){
 analogWrite(derA,0);
 analogWrite(izqA,0);
 analogWrite(derB,0);
 analogWrite(izqB,0);
 }
 if(estado=='4'){
 analogWrite(derB,0);
 analogWrite(izqB,0);
 analogWrite(derA,vel);
 analogWrite(izqA,0);
 }
 if(estado=='5'){
 analogWrite(derA,0);
 analogWrite(izqA,0);
 analogWrite(derB,vel);
 analogWrite(izqB,vel);
 }
 if (estado=='6'){
    digitalWrite(ptrig,LOW);
   delayMicroseconds(2);
   digitalWrite(ptrig,HIGH);
   delay(0.01);
   digitalWrite(ptrig,LOW);
   duracion=pulseIn(pecho,HIGH);
   distancia=(duracion/2)/29;
   delay(10);
   if (distancia <=15 && distancia >=2){
     digitalWrite(13,HIGH);
     analogWrite(derB, 0);                  // Parar los motores por 200 mili segundos
     analogWrite(izqB, 0); 
     analogWrite(derA, 0);    
     analogWrite(izqA, 0); 
     delay (200);
     analogWrite(derB, vel);               // Reversa durante 500 mili segundos
     analogWrite(izqB, vel);
     delay(500);           
        
     analogWrite(derB, 0);                // Girar durante 1100 milisegundos   
     analogWrite(izqB, 0); 
     analogWrite(derA, 0);  
     analogWrite(izqA, vel);  
     delay(1100);
     
     digitalWrite(13,LOW);
   }
   else{
     analogWrite(derB,0);
     analogWrite(izqB,0);
     analogWrite(derA,vel);
     analogWrite(izqA,vel);
   }
 }
 if (estado=='7'){
   analogWrite(derB,0);
   analogWrite(izqB,0);
   analogWrite(derA,0);
   analogWrite(izqA,0);
 }
}  
