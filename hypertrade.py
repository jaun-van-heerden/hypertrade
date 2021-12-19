from manager import Manager


def main():

    # create manager
    manager = Manager(60)

    # manager.find_top_accelerator(2)

    manager.add_bot()

    manager.run()


if __name__ == '__main__':

    main()



# todo Hotlist -- coins get hotter and have a cooldown percent