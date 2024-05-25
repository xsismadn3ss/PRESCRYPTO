import json


# diccionario para agregar al archivo json
pk = {"pk": "mi contraseña"}

# si el archivo no existe crea uno en modo escritura(w = write)
with open(file="__.json", mode="w") as f:

    # truncar dicionario en el archivo con indentado de 4 espacios
    json.dump(pk, f, indent=4)

print("json guardado con exito")
