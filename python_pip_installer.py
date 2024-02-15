"""
Testing with a python pip installer
"""

import os

with open("required packages.txt", "r") as file:
    install = file.readlines()
    for item in install:
        os.system(f"pip install {item}")
