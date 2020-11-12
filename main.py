import time
import board
from adafruit_matrixportal.network import Network

from secrets import secrets
from config import config

network = Network(status_neopixel=board.NEOPIXEL)

def clone_code_file(network, user, repo, branch):
    print("Fetching code updates")
    url = "https://raw.githubusercontent.com/" + user + "/" + repo + "/" + branch + "/portable.py"
    try:
        req = network.fetch(url)
    except RuntimeError as e:
        print(e)
        req = None

    if req:
        with open("portable.py", "w") as code_file:
            code_file.write(req.text)
        print("Success")
    else:
        print("Failure")


portable = None
while not portable:
    clone_code_file(network)
    try:
        import portable as p
    except Exception as e:
        print(e)
        time.sleep(10)

p.main()