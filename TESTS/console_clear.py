import platform
import os


def console_clear():
    """funcion para integrar opcion de limpiar consola en python"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
