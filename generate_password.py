import time
import random
import os

from PyInquirer import prompt
import pyperclip

char_dict = {
    "small_alphabets": "abcdefghijklmnopqrstuvwxyz",
    "capital_alphabets": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers": "0123456789",
    "special_characters": r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
}

selectParameters = [
    {
        "type": "checkbox",
        "message": "Select parameters",
        "name": "parameters",
        "choices": [
            {
                "name": "Small Alphabets",
                "checked": True,
            },
            {
                "name": "Capital Alphabets",
            },
            {
                "name": "Numbers"
            },
            {
                "name": "Special Characters"
            }
        ]
    }
]

passwordLength = [
    {
        "type": "input",
        "message": "Enter password length",
        "name": "length",
        "default": "25"
    }
]


def generate_password():
    while True:
        os.system("clear")
        params = prompt(selectParameters)
        if len(params["parameters"]) != 0:
            break
        print("\nYou must choose at least one parameter.")
        time.sleep(2)
    length = prompt(passwordLength)

    characters = "".join(
        char_dict[param.lower().replace(" ", "_")]
        for param in params["parameters"]
    )

    password = "".join(random.choices(characters, k=int(length["length"])))
    pyperclip.copy(password)
    print(f"\nPassword: {password}")


if __name__ == "__main__":
    generate_password()
