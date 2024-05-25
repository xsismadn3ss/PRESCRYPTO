from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from console_clear import console_clear
import json
import base64
import time
import os


def generate_key(pin: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(pin.encode()))
    return key


def encrypt(psswrd: str, pin: str) -> str:
    salt = os.urandom(16)  # Genera una salt aleatoria
    key = generate_key(pin, salt)
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(psswrd.encode())
    # Prepend the salt to the encrypted message
    return base64.urlsafe_b64encode(salt + encrypted_message).decode()


def decrypt(encrypted_psswrd: str, pin: str) -> str:
    data = base64.urlsafe_b64decode(encrypted_psswrd)
    salt, encrypted_psswrd = data[:16], data[16:]
    key = generate_key(pin, salt)
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_psswrd)
    return decrypted_message.decode()


# ENCRYPTAR TEXTO
def set_password():
    if not os.path.exists("__k__.json"):
        with open(file="__k__.json", mode="w") as file:
            print("archivo creado")

            pk = input("INGRESA LA CONTRASEÑA DE TU WALLET: ")
            pin = input("INGRESA UN PIN: ")

            console_clear()
            encrypted_psswrd = encrypt(psswrd=pk, pin=pin)

            print(encrypted_psswrd)
            print("CONTRASEÑA ENCRIPTADA Y GUARDADA, POR FAVOR NO OLVIDES TU PIN")

            # guardar clave encriptada en un archivo json
            json.dump({"pk": encrypted_psswrd}, file, indent=4)
    else:
        check_password()


def check_password():
    with open(file="__k__.json", mode="r") as file:
        k = json.load(file)
        encrypted_psswrd = k["pk"]

        console_clear()
        pin = input("ENTER YOUR PIN: ")
        try:
            decrypted_psswrd = decrypt(encrypted_psswrd=encrypted_psswrd, pin=pin)
            print(f"CONTRASEÑA CORRECTA\n{decrypted_psswrd}")
        except:
            print("CONTRASEÑA INCORRECTA")


console_clear()
set_password()
