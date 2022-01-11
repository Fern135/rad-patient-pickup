from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64  # for encryption

import os

import colorama
from colorama import Fore

# region global variables
colorama.init(autoreset=True)

# for the coloring the console for debugging
success = Fore.GREEN
warning = Fore.YELLOW
error = Fore.RED

format = "utf-8"  # into bytes

class cryptography:

    def get_encryption_key(self, msg):  # generate encryption key to encrypt lol
        try:
            # stripping any white spaces
            password_provided = str(msg).strip()

            # encoding into a byte
            password = password_provided.encode(format)

            # salt used to encrypt
            # salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"
            salt = os.urandom(32)

            # generating said key
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )

            return base64.urlsafe_b64encode(kdf.derive(password))

        except Exception as e:
            print(f"{error} * Error: {str(e)}")
            return (f"{error} * Error: {str(e)}")


    def encrypt(self, data):  # encrypt
        try:
            # encrypt data
            fernet = Fernet(
                self.get_encryption_key(
                    data.encode(format)
                )
            )
            return fernet.encrypt(
                data.encode(format)
            )
        except Exception as e:
            print(f"{error} * error: {str(e)}")
            return (f"{error} * error: {str(e)}")


    def decrypt(self, data):  # decrypt
        try:
            # decrypt data
            fernet = Fernet(
                self.get_encryption_key(
                    data.decode(format)
                )
            )
            return fernet.decrypt(
                data.decode(format)
            )
        except Exception as e:
            print(f"{error} * error: {str(e)}")
            return (f"{error} * error: {str(e)}")
