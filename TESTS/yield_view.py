import flet as ft
from controls.View import View
from controls.Card import Card
from controls.Tittle import Tittle

"""
prueba para crear dinamicamente tarjetas para cada prescripcion en una interfaz
"""


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

data = [
    prescripcion1,
    prescripcion2,
    prescripcion3,
    prescripcion4,
]


def hellowordl(e):
    contenido = e.control.data
    print(contenido)


# paginar tarjetas
def generatePrescriptions():
    datos = data[::-1]

    for prescription in datos:
        # PLANTILLA DE TARJETA
        titulo = ft.Text(size=16, color=ft.colors.WHITE)
        fechas = ft.Text(size=14, color=ft.colors.WHITE70)
        contenido = {
            "medicamento": prescription["medicamento"],
            "fechas": prescription["fechas"],
        }

        for i in prescription:
            if i == "medicamento":
                valor: str = prescription[i]
                titulo.value = valor.upper()
            if i == "fechas":
                fechas_txt = "Fechas:\n"
                for j in prescription[i]:
                    fechas_txt += f"{j}\n"
                fechas.value = fechas_txt

        # añadir controles a la tarjeta
        tarjeta = Card(
            controls=[titulo, fechas],
            bgcolor=ft.colors.GREEN_900,
            on_click=hellowordl,
            data=contenido,
        )
        yield tarjeta


card = generatePrescriptions()


def lote_tarjetas(size=5):
    cards = []
    try:
        for i in range(size):
            cards.append(next(card))
    except Exception as e:
        pass
    return cards


def main(page: ft.Page):
    page.title = "TEST"

    def add(e):
        contendedor_tarjetas.controls += lote_tarjetas()
        page.update()

    tarjetas = lote_tarjetas()
    contendedor_tarjetas = ft.Column(controls=tarjetas)
    inicio = View(
        controls=[  # controles para la vista
            Tittle("PRESCRIPTIONS"),
            ft.Container(
                # añadir contenedor para tarjetas
                content=contendedor_tarjetas
            ),
            ft.ElevatedButton(
                text="Cargar nuevos",
                color=ft.colors.WHITE,
                on_click=add,
            ),
        ]
    )

    page.add(inicio)


ft.app(target=main, view=ft.AppView.FLET_APP)
