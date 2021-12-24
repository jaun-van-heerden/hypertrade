from cmd import Cmd


class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"

    # start
    def do_start(self):
        print('Starting')

    def help_start(self):
        print('Send <start> to get warm up those engines')

    # exit
    def do_exit(self, inp):
        print("Bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def default(self, inp):
        print('~')


if __name__ == '__main__':
    MyPrompt().cmdloop()
