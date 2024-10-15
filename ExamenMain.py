#Aqui empieza el codigo
from pynq.overlays.base import BaseOverlay
from pynq.lib.pmod import PMOD_GROVE_G4
from pynq.lib.pmod import Grove_ADC
import paho.mqtt.client as mqtt
import time
import json

base = BaseOverlay("base.bit")
base.download()
print("El Bitstream ha sido programado a las " +str(base.timestamp))
ADC = Grove_ADC(base.PMODA, PMOD_GROVE_G4)


# Definir tópicos y dirección del broker
topic1= "ANALOG/GRUPO[[2]]"
broker_address = "10.172.118.177"

# Definir callbacks de MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT con código de resultado: " + str(rc))

def on_publish(client, userdata, mid):
    print("Mensaje publicado con ID: " + str(mid))

def on_disconnect(client, userdata, rc):
    print("Desconectado del broker MQTT con código de resultado: " + str(rc))
# Inicializar MQTT cliente
client = mqtt.Client(client_id="Publicador2_Grupo2")
client.on_connect = on_connect
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Conectar al broker
client.connect(broker_address, 1883)
client.loop_start()

#crear una lectura en ADC
valorA = 0
valmax = 0
valmin = 55
while(1):
    valor = ADC.read()
    if((valor > valorA + (valorA * 0.2) or valor < valorA - (valorA * 0.2)) and (valor != 0)):
        valorA = valor
        client.publish(topic1, float(valorA), qos=1, retain=True)
        print(f"Publicando en valor de rotary: {valorA}")
        #Añadir los valores
        if(valorA > valmax):
            valmax = valorA
        if(valorA < valmin):
            valmin = valorA
        with open("/tmp/valoresAPI.tmp","w") as data_file:
            data = {
                "val_max" : valmax,
                "val_min" : valmin,
                "val"     : valorA
            }
            json.dump(data,data_file)   
    time.sleep(0.5)