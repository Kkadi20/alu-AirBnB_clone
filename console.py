#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

classes = {
    "BaseModel": BaseModel
}

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        objects = storage.all()
        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objects.items() if key.startswith(arg)])
        else:
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')

                # Try casting to int or float
                if attr_value.isdigit():
                    attr_value = int(attr_value)
                else:
                    try:
                        attr_value = float(attr_value)
                    except ValueError:
                        pass

                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
