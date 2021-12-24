from loguru import logger


class Bot:

    def __init__(self,
                 name: str,
                 asset: str,
                 spend_max: float):


        logger.info('initialising bot')

        self.name = name

        self.asset = asset


        self.spend_max = spend_max


    def run(self):

        logger.info('running bot')
