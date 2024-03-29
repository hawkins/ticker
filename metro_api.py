
from config import config

class MetroApiOnFireException(Exception):
    pass

class MetroApi:
    def __init__(self, network):
        self.network = network

    def fetch_train_predictions(self, station_code: str) -> [dict]:
        return self._fetch_train_predictions(station_code, retry_attempt=0)

    def _fetch_train_predictions(self, station_code: str, retry_attempt: int) -> [dict]:
        try:
            api_url = config['metro_api_url'] + station_code
            train_data = self.network.fetch(api_url, headers={
                'api_key': config['metro_api_key']
            }).json()

            print('Received response from WMATA api...')
            trains = train_data['Trains']
            print(trains)

            normalized_results = list(map(self._normalize_train_response, trains))

            return normalized_results
        except RuntimeError:
            if retry_attempt < config['metro_api_retries']:
                print('Failed to connect to WMATA API. Reattempting...')
                # Recursion for retry logic because I don't care about your stack
                return self._fetch_train_predictions(station_code, group, retry_attempt + 1)
            else:
                raise MetroApiOnFireException()

    def _normalize_train_response(self, train: dict) -> dict:
        line = train['Line']
        destination = train['Destination']
        arrival = train['Min']

        if destination == 'No Passenger' or destination == 'NoPssenger' or destination == 'ssenger':
            destination = 'No Psngr'

        return {
            'line_color': self._get_line_color(line),
            'destination': destination,
            'arrival': arrival
        }

    def _get_line_color(self, line: str) -> int:
        if line == 'RD':
            return 0xFF0000
        elif line == 'OR':
            return 0xFF5500
        elif line == 'YL':
            return 0xFFFF00
        elif line == 'GR':
            return 0x00FF00
        elif line == 'BL':
            return 0x0000FF
        else:
            return 0xAAAAAA
