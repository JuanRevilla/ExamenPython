import paho.mqtt.client as mqtt
import time
#INSERCION
import mysql.connector
from mysql.connector import Error
from datetime import datetime

topic1= "ANALOG/GRUPO[[2]]"
broker_address = "10.172.118.177"

try:
    # Establecer la conexión con la base de datos
    connection = mysql.connector.connect(
        host='10.172.118.177',  # Reemplaza con la IP de tu ordenador
        database='GRUPO2',
        user='GRUPO2',
        port = '3317',
        password='letmein'
    )
    # Verificar si la conexión fue exitosa
    if connection.is_connected():
        print("Conexión de exito a la base de datos")
    else:
        print("No se pudo conectar a la base de datos")
except Error as e:
    print(f"Fallo en la conexion: {e}")

cursor = connection.cursor()


def on_message(client, userdata, message):
    #INSERCION
    query_temp = "INSERT INTO ValoresIKERJUAN (VALOR) VALUES ('"+str(message.payload.decode("utf-8"))+"')"        
    try:
        cursor.execute(query_temp)
        connection.commit()
        print(f"Estación Introducida")
    except Error as e:
        print(f"Fallo al Introducir Estacion: {e}")
        
    print("message received " ,str(message.payload.decode("utf-8")))

client = mqtt.Client()
client.on_message = on_message
client.connect(broker_address)
client.loop_start()
client.subscribe(topic1)
while True:
    time.sleep(1)