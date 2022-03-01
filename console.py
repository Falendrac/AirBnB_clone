#!/usr/bin/python3
"""
Creation of the console of the web application
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Manage the EOF
        """
        return True

    def do_quit(self, line):
        """
        Quit the program
        """
        return True

    def emptyline(self):
        print(end="")

    def help_EOF(self):
        """
        Help section of EOF
        """
        print('\n'.join(['Manage the EOF, exit the console']))

    def help_quit(self):
        """
        Help section of quit
        """
        print('\n'.join(['quit function\nUsage quit\nExit the console']))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
