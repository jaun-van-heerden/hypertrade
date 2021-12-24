from swyftx_api import Swyftx
from time import sleep
from bot import Bot
from loguru import logger


class Manager:
    """ manager """

    def __init__(self, interval):
        """ init """

        self.interval = interval

        logger.info('initialising manager')

        logger.info('connecting to Swyftx')

        self.swyftx = Swyftx()

        logger.info('connected to Swyftx')

        self.bots = []

    def add_bot(self):
        """ add bot """

        logger.info('Adding Bot')

        bot = Bot()

        self.bots.append(bot)

    def run(self):
        """ run """

        while True:

            sleep(self.interval)

            for bot in self.bots:

                bot.run()
