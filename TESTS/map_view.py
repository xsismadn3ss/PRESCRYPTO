from ast import List
import flet as ft
import datetime
from controls.View import View
from controls.Button import CustomButton
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


# mapear tarjetas
def getPrescriptions(prescription):
    medicamento: str = prescription["medicamento"]
    fechas = prescription["fechas"]
    date_txt = ""
    for i in fechas:
        date_txt += f"{i}\n"

    titulo = ft.Text(value=medicamento.capitalize(), size=24)
    dates = ft.Text(value=f"Fechas:\n{date_txt}", size=16)

    return {"titulo": titulo, "contenido": dates}


def mapPrescriptions():
    mappedCards = map(getPrescriptions, data)
    cards = []

    for diccionario in mappedCards:
        card = Card(
            controls=[diccionario["titulo"], diccionario["contenido"]],
            bgcolor=ft.colors.GREEN_900,
        )
        cards.append(card)

    return cards


def main(page: ft.Page):
    page.title = "TEST"

    tarjetas = mapPrescriptions()
    contendedor_tarjetas = ft.Column(controls=tarjetas)
    inicio = View(
        controls=[  # controles para la vista
            Tittle("PRESCRIPTIONS"),
            ft.Container(
                # mapear lista para generar tarjetas
                content=contendedor_tarjetas
            ),
            ft.ElevatedButton(
                text="Cargar nuevos",
                color=ft.colors.WHITE,
            ),
        ]
    )

    page.add(inicio)


ft.app(target=main, view=ft.AppView.FLET_APP)
