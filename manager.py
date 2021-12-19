from swyftx_api import Swyftx
from time import sleep
from bot import Bot
import time
from pprint import pprint


class Manager:

    def __init__(self, interval):
        """
        timimg
        """
        self.interval = interval

        print('initialising manager')

        print('connecting to Swyftx')
        self.swyftx = Swyftx()

        self.bots = []

    def add_bot(self):
        print('adding bot')
        bot = Bot()
        self.bots.append(bot)

    """
    Gets data for all assets



    """

    def find_top_accelerator(self, interval, num_top=10):
        print('finding top accelerator')

        milli_end = round(time.time() * 1000)

        milli_start = milli_end - interval * 1000 * 60 * 60

        # get all assest data
        for asset in self.swyftx.market_assets:

            pprint(asset)

            self.swyftx.get_asset_data('1',
                                       asset,
                                       '1h',
                                       'ask',
                                       str(milli_start),
                                       str(milli_end),
                                       str(20))

    def run(self):
        while True:
            sleep(self.interval)

            for bot in self.bots:
                bot.run()
