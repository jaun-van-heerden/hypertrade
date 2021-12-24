from api.swyftx import Manager
from time import sleep
from bot import Bot
from loguru import logger
import json
from pathlib import Path


# todo Hot list -- coins get hotter and have a cooldown percent

class Hypertrade:

    def __init__(self):
        self.config = None
        self.db = None
        self.bots = None
        self.platform = None
        self.status = {'config': False,
                       'db': False,
                       'platform': False,
                       'bots': False}

    def setup(self):
        self.load_config()
        self.connect_db()
        self.connect_platform()

    def load_config(self, config_filepath=None):
        """load the configuration"""
        if config_filepath is None:  # default
            config_filepath = 'config.json'
        config_filepath = Path(config_filepath)
        try:
            with open(config_filepath, 'rb') as file:
                self.config = json.load(file)
            self.status['config'] = True
        except Exception as e:
            print(e)
            print('failed to load config file')
            exit(2)

    def connect_platform(self):
        # todo make generic
        logger.info('connecting to Swyftx')
        self.platform = Manager(self.config)
        self.status['platform'] = True
        logger.info('connected to Swyftx')

    def connect_db(self, db_name=None):
        """ Connect to SQLite DB """
        if db_name is None:
            db_name = 'data.db'
        self.db = db_name
        logger.info(f'connected to a fake database <{self.db}>')


def main():
    ht = Hypertrade()
    ht.setup()


if __name__ == '__main__':
    main()
