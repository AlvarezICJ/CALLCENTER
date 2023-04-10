import pandas as pd
from twilio.rest import Client
from datetime import datetime

# Configuración de Twilio
account_sid = 'TU_ACCOUNT_SID'
auth_token = 'TU_AUTH_TOKEN'
client = Client(account_sid, auth_token)
twilio_number = 'TU_NUMERO_DE_TWILIO'
my_number = 'TU_NUMERO_DE_TELEFONO'

# Ruta y nombre del archivo de Excel
file_name = 'ventas_diarias.xlsx'

# Carga los datos del archivo de Excel en un DataFrame de pandas
try:
    df = pd.read_excel(file_name)
except:
    df = pd.DataFrame(columns=['Fecha', 'Paquete', 'Ventas', 'Total'])

# Obtiene la fecha, el nombre del paquete y las ventas del día
fecha = datetime.now().strftime('%Y-%m-%d')
paquete = input('Ingrese el nombre del paquete vendido hoy: ')
ventas = int(input('Ingrese la cantidad de paquetes premium vendidos hoy: '))

# Pregunta si se vendió en oferta
oferta = input('¿Se vendió en oferta a 19900 COP? (s/n) ')

if oferta.lower() == 's':
    precio_unitario = 19900
else:
    precio_unitario = 25000

# Calcula el total de las ventas
total = ventas * precio_unitario

# Agrega los datos de ventas al DataFrame
row = {'Fecha': fecha, 'Paquete': paquete, 'Ventas': ventas, 'Total': total}
df = df.append(row, ignore_index=True)

# Guarda el DataFrame en el archivo de Excel
df.to_excel(file_name, index=False)

# Envía un mensaje de texto con los datos de ventas
message = f'Hoy ({fecha}) se vendieron {ventas} paquetes {paquete}, con un total de ${total}.'
client.messages.create(to=my_number, from_=twilio_number, body=message)
