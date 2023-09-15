

// Variáveis
volatile char estado = 'A';
String situacao = "BLOQUEADO";
volatile char input = '!'; 

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600); // Iniciar a comunicação serial
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  digitalWrite(13, HIGH);
  digitalWrite(12, LOW);
}

void loop()
{
  // ler o input
  input = Serial.read();
  if(input != -1){
    if(estado == 'A' && input == '4'){ // input == primeiro dígito da senha
      estado = 'B';
    }
    else if(estado == 'B' && input == '9'){ // input == segundo dígito da senha
      estado = 'C';
    }
    else if(estado == 'C' && input == '1'){// input == terceiro dígito da senha
      estado = 'A';
      situacao = "DESBLOQUEADO";
      digitalWrite(12, HIGH);
      digitalWrite(13, LOW);
      Serial.println("bloqueando trava...");
      delay(5000);
      digitalWrite(13, HIGH);
  	  digitalWrite(12, LOW);
      Serial.println("trava bloqueada...");
      Serial.println();
      situacao = "BLOQUEADO";
    }
    else{ // erro
      estado = 'A';
      situacao = "BLOQUEADO";
      digitalWrite(13, HIGH);
  	  digitalWrite(12, LOW);
    }
  }
  else{ // nao foi lido nada pelo input
    //Serial.println("nao foi lido nada!");
  }

  delay(1000);
  
  Serial.print("Situacao: ");
  Serial.print(situacao);
  Serial.print(" ; Estado: ");
  Serial.println(estado);
  Serial.println();
}
