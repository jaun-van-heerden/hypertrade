import requests
import json
from pprint import pprint
from loguru import logger


class Swyftx:

    def __init__(self, demo_mode=False):
        self.base_url = "https://api.swyftx.com.au/"

        with open("resources/key.json") as key_file:
            data = json.load(key_file)
            self.key = data["key"]
            self.token = data["token"]

        self.status = "disconnected"

        """
        requests
        """
        self.headers = {"Content - Type": "application / json",
                        "Authorization": f"Bearer {self.token}"}

        """
        demo mode
        """

        self.demo_mode = demo_mode

        if self.demo_mode:
            self.base_url = "https://api.demo.swyftx.com.au"

        """
        balance
        """

        self.balance = None

        """
        market assets
        """
        self.market_assets = None

        """
        profile
        """
        self.profile = None

        """
        market assets
        """
        self.get_market_assets()

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


if __name__ == "__main__":
    swyftx = Swyftx()

    # test check connection
    swyftx.test_connection()

    # test get balance
    # swyftx.get_balance()

    # test get market assets
    # swyftx.get_market_assets()

    # test get profile
    # swyftx.get_profile()
