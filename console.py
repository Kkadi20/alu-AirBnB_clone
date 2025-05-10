#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Base command interpreter class for HBNB project"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
