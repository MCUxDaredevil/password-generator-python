import time
import random
import os

from PyInquirer import prompt

# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~
char_dict = {
    "small_alphabets": "abcdefghijklmnopqrstuvwxyz",
    "capital_alphabets": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers": "0123456789",
    "special_characters": r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
}

questions = [
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
    },
    {
        "type": "input",
        "message": "Enter password length",
        "name": "length",
        "default": "16"
    }
]


def create_password(length=16):
    character_string = char_dict["small_alphabets"] + char_dict["capital_alphabets"] + char_dict["numbers"] + char_dict["special_characters"]

    print("".join(random.sample(character_string, k=length)))


def main():
    while True:
        os.system("clear")
        answers = prompt(questions)
        if len(answers["parameters"]) != 0:
            break
        print("\nYou must choose at least one parameter.")
        time.sleep(2)
    print(answers)


if __name__ == "__main__":
    main()
