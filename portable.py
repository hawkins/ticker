# DC Metro Board
import time
from config import config
from train_board import TrainBoard
from metro_api import MetroApi, MetroApiOnFireException

STATION_CODE = config["metro_station_code"]
REFRESH_INTERVAL = config["refresh_interval"]


def main(network):
    def refresh_trains(network) -> [dict]:
        try:
            api = MetroApi(network)
            return api.fetch_train_predictions(STATION_CODE)
        except MetroApiOnFireException:
            print("WMATA Api is currently on fire. Trying again later ...")
            return None

    train_board = TrainBoard(refresh_trains)
    while True:
        train_board.refresh()
        time.sleep(REFRESH_INTERVAL)
