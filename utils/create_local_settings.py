#!/usr/bin/env python3

import os
import random


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = "myproject"


def generate_local_settings():
    content = "from .settings import *\n\n"

    characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"

    secret_key = "".join(
        [random.SystemRandom().choice(characters) for i in range(50)]
    )

    content += "SECRET_KEY = \"{}\"\n".format(secret_key)

    return content


def get_file_path():
    return os.path.join(BASE_DIR, PROJECT_NAME, "local_settings.py")


def write_local_settings(file_path, content):
    f = open(file_path, "w")
    f.write(content)


if __name__ == "__main__":
    print("Generating local settings")
    content = generate_local_settings()
    file_path = get_file_path()
    print("Saving local settings to file {}".format(file_path))
    write_local_settings(file_path, content)
