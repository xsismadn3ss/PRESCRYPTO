import flet as ft
from flet import colors
from web3 import Web3
from dotenv import load_dotenv
from controls.Tittle import Tittle
from controls.Textfield import TextFieldCustom
from controls.View import View
from controls.Button import CustomButton
import os
import time

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

    # def check_balance(e):
    #     try:
    #         wallet = wallet_token.value
    #         # balance=w3.eth.get_balance(wallet)
    #         dlg = ft.AlertDialog(
    #             title=ft.Text(f"\nAvailable balance:\n{balance}ETH\n"),
    #             on_dismiss=lambda e: print("Dialog dissmissed"),
    #         )
    #     except Exception as e:
    #         dlg = ft.AlertDialog(
    #             title=ft.Text(
    #                 f"\nIncorrrect token\n\n{e}\n",
    #             ),
    #             on_dismiss=lambda e: print("Dialog dissmissed"),
    #         )
    #     wallet_token.value = ""
    #     page.dialog = dlg
    #     dlg.open = True
    #     page.update()

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
    lv = ft.ListView(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        Tittle("Hello world"),
                        TextFieldCustom("Write your name"),
                        CustomButton("Enter"),
                        Tittle("Hello world"),
                        TextFieldCustom("Write your name"),
                        CustomButton("Enter"),
                        Tittle("Hello world"),
                        TextFieldCustom("Write your name"),
                        CustomButton("Enter"),
                        Tittle("Hello world"),
                        TextFieldCustom("Write your name"),
                        CustomButton("Enter"),
                    ],
                ),
                padding=8,
                border_radius=10,
            ),
        ],
        expand=1,
        spacing=10,
        padding=8,
        auto_scroll=True,
    )

    balance = View(controls=[Tittle("Balance"), CustomButton("Check balance")])
    explore = View(controls=[Tittle("Explore")])
    account = View(
        controls=[
            Tittle("Account"),
            ft.Container(
                content=ft.Column(
                    controls=[ft.Text("Lore ipsum dolor", size=14)],
                ),
                bgcolor=colors.GREEN_900,
                opacity=90,
                border_radius=10,
                padding=20,
                height=200,
                width=500,
            ),
        ]
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

    page.add(
        # pagina de inicio
        balance
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
