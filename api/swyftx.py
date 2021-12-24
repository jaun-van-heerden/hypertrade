import requests
import json
from pprint import pprint
from loguru import logger


class Manager:

    def __init__(self, config=None):
        # """ demo mode """
        # self.demo_mode = demo_mode
        # self.base_url = "https://api.swyftx.com.au/"
        # if self.demo_mode:
        #     self.base_url = "https://api.demo.swyftx.com.au"

        self.config = config
        self.base_url = "https://api.swyftx.com.au/"
        self.key = None
        self.token = None

        """ requests """
        self.headers = {"Content - Type": "application / json",
                        "Authorization": f"Bearer {self.token}"}

        """ balance """
        self.balance = None

        """ market assets """
        self.market_assets = None

        """ profile """
        self.profile = None


    def test_connection(self):
        response = requests.get(self.base_url)
        logger.info(f'testing connection {response.status_code}')

    def get_balance(self):
        webaddr = self.base_url + "user/balance/"
        self.balance = self.get_request("Balance", webaddr)

    def get_profile(self):
        webaddr = self.base_url + "user/"
        self.profile = self.get_request("Profile", webaddr)

    def get_market_assets(self):
        webaddr = self.base_url + "markets/assets/"
        self.market_assets = self.get_request("Market Assets", webaddr)

    def get_request(self, loc, req_str):
        logger.info(f"Retrieving {loc} <{req_str}>")
        response = requests.get(req_str, headers=self.headers)
        pprint(response.json())
        return response.json()

    def get_asset_data(self,
                       baseAsset,
                       secondaryAsset,
                       resolution,
                       side,
                       timeStart,
                       timeEnd,
                       limit):
        """parameters"""
        webaddr = "https://api.swyftx.com.au/charts/getBars/" + \
                  baseAsset + "/" + \
                  str(secondaryAsset['id']) + "/" + \
                  side + "/" + \
                  "?" + resolution + "=" + \
                  "&timeStart=" + timeStart + \
                  "&timeEnd=" + timeEnd + \
                  "&limit=" + limit

        data = self.get_request(f"asset {secondaryAsset['name']}", webaddr)

        print(data)
        input()

    def set_auth(self):
        """SET """
        with open(self.config['key']['swyftx']) as file:
            data = json.load(file)
            self.key, self.token = data["key"], data["token"]


if __name__ == "__main__":
    swyftx = Manager()

    # test check connection
    swyftx.test_connection()

    # test get balance
    # swyftx.get_balance()

    # test get market assets
    # swyftx.get_market_assets()

    # test get profile
    # swyftx.get_profile()
