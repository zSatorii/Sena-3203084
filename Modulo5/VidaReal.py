monto_transaccion = 5000
ubicacion_inusual = True
horario_inusual = False

if monto_transaccion > 3000 and (ubicacion_inusual or horario_inusual):
    print("Alerta: Posible fraude. Verificar transacción.")
    enviar_sms_verificacion()
else:
    print("Transacción procesada correctamente.")
