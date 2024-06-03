"""
Las funciones generadoras en python se utilizan para recorrer objetos iterables y
no saturar la memoria de un dispositivo, a diferencia de un for no completa el bucle
sino que lo recorre en trozo pero guarda el ultimo punto en que se quedo
"""

import time
from console_clear import console_clear


prescripcion1 = {
    "medicamento": "ibuprofeno",
    "fechas": [
        "2024/07/15",
        "2024/08/15",
        "2024/09/15",
    ],
}

prescripcion2 = {
    "medicamento": "paracetamol",
    "fechas": [
        "2024/07/15",
        "2024/08/15",
        "2024/09/15",
    ],
}
prescripcion3 = {
    "medicamento": "corticoesteroides",
    "fechas": [
        "2024/07/15",
        "2024/08/15",
        "2024/09/15",
    ],
}
prescripcion4 = {
    "medicamento": "morfina",
    "fechas": [
        "2024/07/15",
        "2024/08/15",
        "2024/09/15",
    ],
}

data = []
for i in range(6):
    data.append(prescripcion1)
    data.append(prescripcion2)
    data.append(prescripcion3)
    data.append(prescripcion4)

# for prescription in data:
#     for i in prescription:
#         if i == "medicamento":
#             print(f"Medicamento: {prescription[i]}")
#         if i == "fechas":
#             print(f"fechas: ")
#             for j in prescription[i]:
#                 print(j)


# usando map
def setPrescription(prescription):
    """
    funcion para crear estilo de un prescripcion
    """
    medicamento = prescription["medicamento"]
    date_text = ""
    fechas = prescription["fechas"]
    for i in fechas:
        date_text += f"{i}\n"
    return {"medicamento": medicamento, "fechas": date_text}


# usando map
# processed_prescriptions = map(setPrescription, data)

# for prescription in processed_prescriptions:
#     print(f"{prescription['medicamento']}")
#     print(f"Fechas:\n{prescription['fechas']}")


# usando yield
def generador():
    for prescription in data:
        yield prescription["medicamento"], prescription["fechas"]


prescription = generador()


def lote_prescription(size=10):
    for i in range(size):
        try:
            print(next(prescription))
        except:
            return


console_clear()
print("Numero de datos: ", len(data))
lote_prescription()
time.sleep(1)
lote_prescription()
time.sleep(1)
lote_prescription()
time.sleep(1)
