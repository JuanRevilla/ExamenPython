import mysql.connector
from mysql.connector import Error
import numpy as np
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
#INSERCION
query_temp = "SELECT VALOR FROM GRUPO2.ValoresIKERJUAN ORDER BY ID DESC"     
respuesta = 0
valoractual = 0
try:
    cursor.execute(query_temp)
    respuesta = cursor.fetchall()
    cursor.execute(query_temp)
    valoractual = cursor.fetchone()
    connection.commit()
    print(f"Listo")
except Error as e:
    print(f"Fallo al Introducir Estacion: {e}")
valormedio = np.mean(respuesta)
print(f"Valor medio = {valormedio}, valor ultimo = {valoractual} ")


        