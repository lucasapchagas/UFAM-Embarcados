// Variáveis

char DIGITO_1 = '4';
char DIGITO_2 = '9';
char DIGITO_3 = '1';

volatile char estado = 'A';
String situacao = "TRANCADO";
volatile char input = '!'; 

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop()
{
  delay(500);

  if (estado == 'D') {
    digitalWrite(13, HIGH);
  } else {
    digitalWrite(13, LOW);
  }

  Serial.print("Situacao: ");
  Serial.print(situacao);
  Serial.print(" ; Estado: ");
  Serial.println(estado);
  Serial.println();
  
  
  while(Serial.available() == 0) { } // Espera o input.
  input = Serial.read();
  	
  if (input != -1) { 
    if (estado == 'A' && input == DIGITO_1) {
      estado = 'B';
    } else if (estado == 'B') {
      if (input == DIGITO_2) {
      	estado = 'C';
      } else  {
        if (input != DIGITO_1) {
          estado = 'A';
        }
      }
    }
    else if (estado == 'C') {
      if (input == DIGITO_3) {
        estado = 'D';
        situacao = "DESTRANCADO";
      } else if (input == DIGITO_1) {
        estado = 'B';
      } else {
        estado = 'A';
      }
    } else {
      estado = 'A';
      situacao = "TRANCADO";
    }
  }
}