import serial
import time
import struct
import sqlite3
import datetime

conn = sqlite3.connect('temperaturas.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE if not exists temperaturas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        temp DECIMAL(5,2) NOT NULL,
        data DATE NOT NULL
);
""")

ser = serial.Serial('COM8', 115200, timeout=0)

while 1:
    try:
        bytesToRead = ser.inWaiting() #Conta os bytes que estão na fila para leitura
        if (bytesToRead >= 7):
            #Qnd tivermos 7 ou mais bytes, a info é printada

            byteValue = ser.readline()
            if (byteValue):
                print (byteValue.decode('utf-8'))

                input_temp = byteValue
                input_date = datetime.datetime.now().isoformat(sep=' ', timespec='minutes')

                cursor.executemany("""
                    INSERT INTO temperaturas (temp, data)
                    VALUES (?,?)
                """, input_temp, input_date)

                if (float(byteValue.decode('utf-8')) > 23):
                    ser.write(struct.pack('!B', 1))
                    print("Enviado")
                else:
                    ser.write(struct.pack('!B', 0))

        #Tempo de amostragem?
        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)

#CONFIGS
#Setar BaundRate
#Setar porta de comunicação
#Setar tempo de amostragem

#Salvar em banco as CONFIGS, o valor da temperatura e o horário
