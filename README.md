Este código utiliza la librería pandas para cargar los datos del archivo de Excel en un DataFrame. Luego, solicita el nombre del paquete vendido, la cantidad de paquetes vendidos y si se vendió en oferta a 19900 COP. Según la respuesta a la pregunta de oferta, se establece el precio unitario.

Después, se calcula el total de las ventas y se agrega una nueva fila al DataFrame con los datos de ventas del día. Finalmente, se guarda el DataFrame en el archivo de Excel y se envía un mensaje de texto con los datos de ventas utilizando la API de Twilio.

Ten en cuenta que necesitarás reemplazar los valores TU_ACCOUNT_SID, TU_AUTH_TOKEN, TU_NUMERO_DE_TWILIO y TU_NUMERO_DE_TELEFONO con tus propias credenciales y números de teléfono.
