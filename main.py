import os
import time
import flet as ft
from web3 import Web3
from flet import colors
from dotenv import load_dotenv
from controls.View import View
from controls.Tittle import Tittle
from controls.Button import CustomButton
from controls.Textfield import TextFieldCustom
from controls.Card import Card

# load_dotenv()
# infura_api = os.getenv('INFURA_API')
# my_address = os.getenv('WALLET_ADDRESS')
# privatekey = os.getenv('PRIVATE_KEY')
# w3 = Web3(Web3.HTTPProvider(infura_api))
# testing connection
# print(w3.is_connected())
user = "Test"
password = "hello"


def main(page: ft.Page):
    page.title = "Prescrytpo"
    page.padding = 18
    page.auto_scroll = True

    # VIEWS
    sign_up = View(
        controls=[
            Tittle("Sign up"),
            TextFieldCustom("Enter your token wallet"),
            TextFieldCustom("Paste your private key", True),
            TextFieldCustom("Set a pin", True),
            CustomButton("Save account"),
        ],
        aligment="center",
    )
    sign_in = View(
        controls=[
            Tittle("Sign In"),
            TextFieldCustom("Write your pin"),
            CustomButton("Enter"),
        ],
        height=700,
        aligment="center",
    )

    balance = View(controls=[Tittle("Balance"), CustomButton("Check balance")])
    explore = View(controls=[Tittle("Explore")])
    account = View(
        controls=[
            Tittle("Account"),
            Card(
                controls=[
                    ft.Text(value="Lorem ipsum dolor", size=14),
                ],
                bgcolor=colors.GREEN_900,
                data="Prescripcion1",
            ),
        ],
    )

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

    section = [
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
    page.navigation_bar = ft.NavigationBar(
        indicator_color=colors.GREEN_800,
        destinations=[
            section[0],
            section[1],
            section[2],
        ],
        on_change=change_route,
    )

    page.add(balance)


ft.app(target=main, view=ft.AppView.FLET_APP)
