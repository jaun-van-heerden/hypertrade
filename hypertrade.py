from bot import Bot
from manager import Manager
from swyftx_api import Swyftx


def main():
    # create manager
    manager = Manager(60)

    manager.find_top_accelerator(2)

    manager.add_bot()

    manager.run()


if __name__ == '__main__':
    main()



# todo Hotlist -- coins get hotter and have a cooldown percent