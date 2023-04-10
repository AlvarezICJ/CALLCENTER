import pandas as pd
from datetime import datetime
from twilio.rest import Client

# Configuración de Twilio
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
client = Client(account_sid, auth_token)
my_twilio_number = 'your_twilio_number_here'
my_cell_number = 'your_cell_number_here'

# Obtener fecha y hora actual
now = datetime.now()
fecha = now.strftime("%d/%m/%Y")
hora = now.strftime("%H:%M:%S")

# Solicitar información de la venta
nombre = input("Ingresa el nmbre del paquete: ")
paquete = input("Ingrese el tipo de paquete vendido: ")
venta = int(input("Ingrese la cantidad vendida: "))

# Guardar la venta en el archivo de Excel
nueva_venta = {"Fecha": fecha, "Hora": hora, "Paquete": paquete, "Venta": venta}
df = pd.DataFrame([nueva_venta])
df.to_excel(r'ventas.xlsx', index=None, header=True)

# Enviar mensaje de texto con información de la venta
mensaje = f"Se ha vendido {venta} paquete(s) {paquete} de {nombre} el día de hoy."
message = client.messages.create(body=mensaje, from_=my_twilio_number, to=my_cell_number)
print("Mensaje enviado correctamente:", message.sid)

