import os
import json
import time
import flet as ft
from web3 import Web3
from flet import colors
from dotenv import load_dotenv
from controls.custom_controls import *

# load_dotenv()
# infura_api = os.getenv('INFURA_API')
# my_address = os.getenv('WALLET_ADDRESS')
# privatekey = os.getenv('PRIVATE_KEY')
# w3 = Web3(Web3.HTTPProvider(infura_api))
# testing connection
# print(w3.is_connected())

session = False

# nav_var
nav_sections = [
    ft.NavigationDestination(
        label="Balance",
        icon=ft.icons.ACCOUNT_BALANCE_WALLET_OUTLINED,
        selected_icon=ft.icons.ACCOUNT_BALANCE_WALLET,
        data="balance",
    ),
    ft.NavigationDestination(
        label="Explore",
        icon=ft.icons.EXPLORE_OUTLINED,
        selected_icon=ft.icons.EXPLORE_SHARP,
        data="explore",
    ),
    ft.NavigationDestination(
        icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED,
        selected_icon=ft.icons.ACCOUNT_CIRCLE,
        label="Account",
        data="account",
    ),
]

nav_bar = ft.NavigationBar(
    indicator_color=colors.GREEN_800,
    destinations=[
        nav_sections[0],
        nav_sections[1],
        nav_sections[2],
    ],
)


# vistas
save_account = CustomButton("Save account", data="sign_up")
sign_up = View_centered(
    controls=[
        Tittle("Sign up"),
        TextFieldCustom("Enter your token wallet"),
        TextFieldCustom("Paste your private key", True, reveal=True),
        TextFieldCustom(
            "Set a pin", True, reveal=True, input_filter=ft.NumbersOnlyInputFilter()
        ),
        Row(
            controls=[
                ft.Icon(name=ft.icons.WALLET, color=ft.colors.GREEN_900),
                ft.Icon(name=ft.icons.KEY, color=ft.colors.GREEN_900),
                ft.Icon(name=ft.icons.PIN, color=ft.colors.GREEN_900),
            ]
        ),
        save_account,
    ],
    height=700,
    alignment="center",
)

sign_account = CustomButton("Enter", data="sign_in")
sign_in = View_centered(
    controls=[
        Tittle("Sign In"),
        TextFieldCustom(
            text="Write your pin",
            psswrd=True,
            reveal=True,
            input_filter=ft.NumbersOnlyInputFilter(),
        ),
        sign_account,
    ],
    height=700,
    alignment="center",
)

balance = View_normal(
    controls=[
        Tittle("Balance"),
        TextFieldCustom(
            "", read_only=True, width=400, text_align="right", value="0.00 eth".upper()
        ),
        CustomButton("Check balance"),
    ],
    alignment="center",
)
explore = View_normal(controls=[Tittle("Explore")])

account_edit = CustomButton(text="Edit profile", data="edit_profile")
account = View_normal(
    controls=[
        Tittle("Account"),
        Card(
            controls=[
                ft.Text("Ramon Estrada", size=26, color=colors.WHITE),
                ft.Text("Age: 45", size=18, color=colors.WHITE),
            ],
            bgcolor=colors.GREEN_900,
            width=400,
        ),
        account_edit,
    ],
)

name = TextFieldCustom(
    text="writte your name".capitalize(),
    data="name",
)
lastname = TextFieldCustom(
    text="write your lastname".capitalize(),
    data="lastname",
)
age = TextFieldCustom(
    text="enter your age".capitalize(), input_filter=ft.NumbersOnlyInputFilter()
)
profile_submit = CustomButton(text="Save", data="save_profile")
profile_form = View_normal(
    controls=[Tittle("Edit profile"), name, lastname, age, profile_submit],
    alignment="center",
    height=600,
)

# funciones


def main(page: ft.Page):
    page.title = "Prescrytpo"
    # page.theme_mode = "light"

    # funciones
    def change_route(e):
        time.sleep(0.4)
        index = e.control.selected_index
        if index == 1:  # chance view to explore
            route = explore
            page.clean()
            page.add(route)

        elif index == 2:  # change view to account
            route = account
            page.clean()
            page.add(route)

        elif index == 0:  # change view to balance
            route = balance
            page.clean()
            page.add(route)
        page.update()

    def start_session(e):
        data = e.control.data

        if data == "sign_in":
            nav_bar.visible = True
            page.clean()
            page.add(balance)
            page.update()

        else:
            nav_bar.visible = True
            page.clean()
            page.add(balance)
            page.update()

    def open_edit(e):
        page.clean()
        nav_bar.visible = False
        page.add(profile_form)
        page.update()

    def save_profile(e):
        page.clean()
        nav_bar.visible = True
        page.add(account)
        page.update()

    page.navigation_bar = nav_bar

    # suscribir eventos
    nav_bar.visible = False
    nav_bar.on_change = change_route
    save_account.on_click = start_session
    sign_account.on_click = start_session
    account_edit.on_click = open_edit
    profile_submit.on_click = save_profile

    # añadir vista principal
    if session == False:
        page.add(sign_up)
    elif session == True:
        page.add(sign_in)


ft.app(target=main, view=ft.AppView.FLET_APP)
