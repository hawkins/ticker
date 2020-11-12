from adafruit_matrixportal.network import Network

from config import config
from secrets import secrets


def clone_code_file(network):
    print("Fetching code updates")
    try:
        req = network.fetch("code.py")
    except RuntimeError as e:
        print(e)
        req = None

    if req:
        with open("code.py", "w") as code_file:
            code_file.write(req.text)
        print("Success")
    else:
        print("Failure")

