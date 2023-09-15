
// Variáveis
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
  
  // 'p' significa pass (atravessar a catraca)
  // 'c' significa coin (inserir uma moeda)
  input = Serial.read();
  if( input != 'c' || input != 'p'){
    if(input == 'c' && situacao.compareTo("BLOQUEADO") == 0){ 
      situacao = "DESBLOQUEADO";
      digitalWrite(13, LOW);
      digitalWrite(12, HIGH);
    }
    else if(input == 'p' && situacao.compareTo("BLOQUEADO") == 0){
      Serial.println("Alarme!!! Voce precisa colocar uma moeda!!!");
    }
    else if(input == 'c' && situacao.compareTo("DESBLOQUEADO") == 0){ 
      Serial.println("Obrigado pela moeda");
    }
    else if(input == 'p' && situacao.compareTo("DESBLOQUEADO") == 0){
      situacao = "BLOQUEADO";
      Serial.println("Voce atravessou a catraca, mudando estado para BLOQUEADO...");
      digitalWrite(13, HIGH);
	  digitalWrite(12, LOW);
    }
    input = '!';
  }
  else{ // nao foi lido nada pelo input
    //Serial.println("nao foi lido nada!");
  }
 
  delay(2000); // Aguardar 1000 milissegundos
  Serial.println(situacao);
}
