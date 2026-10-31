print("======= RESTAURANTE 'M & CH' ======")
print("\n---- NOTA DE REMISION ELECTRONICA ----")

def cuenta_total(subtotal, propina, comensales):
    cant_propina = subtotal * (propina / 100)
    total = subtotal + cant_propina
    propor = total / comensales
    return cant_propina, total, propor

while True:
    try:
        subtotal = float(input("\nSUBTOTAL DE LA CUENTA: $ "))
        if subtotal <= 0:
            print("INGRESA UN MONTO MAYOR A 0")
            continue
        break
    except ValueError:
        print("INGRESA UN MONTO VALIDO")

while True:
    try:
        propina = int(input("\nPORCENTAJE DE PROPINA (%): "))
        if propina <= 0:
            print("INGRESA UN MONTO MAYOR A 0")
            continue
        break
    except ValueError:
        print("INGRESA UN MONTO VALIDO")

while True:
    try:
        comensales = int(input("\nNUMERO DE PERSONAS A DIVIDIR CUENTA: "))
        if comensales <= 0:
            print("INGRESE UNA CANTIDAD MAYOR A 0")
            continue
        break
    except ValueError:
        print("INGRESE UN MONTO VALIDO")

prop, totl, pro_comen = cuenta_total(subtotal, propina, comensales)

print("\n--------------------------------------------------------------")
print(f"\nPROPINA {propina} (%): $ {prop:.2f} MXN")
print(f"\nEL TOTAL A PAGAR ES DE $ {totl:.2f} MXN")
print(f"\nPAGO POR PERSONA $ {pro_comen:.2f} MXN")

print("\n**** GRACIAS POR SU PREFERENCIA ****\n\nSI REQUIERE FACTURA PUEDE HACERLO EN LINEA\nEN LAS PROXIMAS 24 HRS 'www.restm&ch.com.mx'")