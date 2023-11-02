"""
Trabalho 3 - Embarcados: Medicao de Temperatura de Bebidas 

Link do github: https://github.com/lucasapchagas/UFAM-Embarcados/tree/main

ALUNOS:
Lucas Afonso Pereira Chagas [22050316]
Mayane Rebeca Maia Carmona [22250335]
Rômulo José Pereira Da Costa Júnior [22152250]
"""

import utime
import time
from machine import Pin
import network
from umqtt.simple import MQTTClient

WIFI_SSID = "" # Nome da rede Wifi
WIFI_PASSWORD = "" # Senha da rede Wifi

MQTT_SERVER = ""
MQTT_USERNAME = ""
MQTT_PASSWORD = ""
MQTT_PORT = 8883

MQTT_TOPIC = "esp32/temperature" # Escolha o tópico MQTT

INTERVALO_COLETAS = 1 # Escolha o intervalo entre as coletas

class MAX6675():
    def __init__(self, so_pin=21, cs_pin=22, sck_pin=23):
        self.cs = Pin(cs_pin, Pin.OUT)
        self.so = Pin(so_pin, Pin.IN)
        self.sck = Pin(sck_pin, Pin.OUT)

        self.cs.on()
        self.so.off()
        self.sck.off()

        self.last_read_time = utime.ticks_ms()

    def readFahrenheit(self):
        return self.readCelsius() * 9.0 / 5.0 + 32

    def readCelsius(self):
        data = self.__read_data()
        volts = sum([b * (1 << i) for i, b in enumerate(reversed(data))])

        return volts * 0.25

    def __read_data(self):
        self.cs.off()
        utime.sleep_us(10)
        data = self.__read_word() 
        self.cs.on()

        if data[-3] == 1:
            raise NoThermocoupleAttached()

        return data[1:-3]

    def __read_word(self):
        return [self.__read_bit() for _ in range(16)]


    def __read_bit(self):
        self.sck.off()
        utime.sleep_us(10)
        bit = self.so.value()
        self.sck.on()
        utime.sleep_us(10)
        return bit


class NoThermocoupleAttached(Exception):
    """Raised when there is no thermocouple attached to MAX6675"""
    pass


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print('Rede conectada: ', wlan.ifconfig())
    return wlan

def do_collect():
    read = 0
    try:
        read = sensor.readCelsius()
        print("Dado coletado: " + str(read) + "ºC")
    except:
      print("NENHUM SENSOR ENCONTRADO")
    return read

def connectMQTT():
    client = MQTTClient(client_id=b"sensor_esp32",
    server=b"{0}".format(MQTT_SERVER),
    port=MQTT_PORT,
    user=b"{0}".format(MQTT_USERNAME),
    password=b"{0}".format(MQTT_PASSWORD),
    keepalive=7200,
    ssl=True,
    ssl_params={'server_hostname': MQTT_SERVER}
    )

    client.connect()
    return client

def publish(topic, value, client):
    valueStr = str(value).encode()
    client.publish(topic, valueStr)

    print("Dado Publicado no tópico {0}: {1}Cº".format(topic, value))

if __name__ == "__main__":
    print("Tentando conectar ao wi-fi...")
    connection = do_connect()

    sensor = MAX6675()
    
    print("Tentando concetar ao cliente MQTT... ")
    client = connectMQTT()    

    print("Iniciando coleta... ")

    while True:
        publish(MQTT_TOPIC, do_collect(), client)
        time.sleep(INTERVALO_COLETAS)