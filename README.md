# Airbnb Clone

## General

This project is the first step of the AirBnB clone project. So it's a FullStack project.

With Mickael we create the command interpreter to manage the AirBnB objects.

In first, we implement the BaseModel object. This object define all others object of our project.

In second time, we create the command interpreter. We see how to use it and all exemple for used it under the General section.

And in last, we define all others objects(User, State, Place...), that inherits from BaseModel.

## The command interpreter

To start the command interpreter, you need python3 and you should use in a terminal:
> ./console.py

Example of first use:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  create  destroy  help  quit  show  update all

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $

### Command description

* help
    - Display the documented command.

            (hbnb) help

            Documented commands (type help <topic>):
            ========================================
            EOF  create  destroy  help  quit  show  update all
    - Used in association with a command that display how to use the command.

            (hbnb) help quit
            Quit command to exit the program

* create
    - Creates a new instance of object passes in parameter and save it to a JSON file.

            (hbnb) create User
            e0d60b67-1ba9-4d3f-a336-b239b96a85c5
            (hbnb) 
* show
    - Display the string represantation of an instance based on the class name and id.

            (hbnb) show User e0d60b67-1ba9-4d3f-a336-b239b96a85c5
            [User] (e0d60b67-1ba9-4d3f-a336-b239b96a85c5) {'id': 'e0d60b67-1ba9-4d3f-a336-b239b96a85c5', 'created_at': datetime.datetime(2022, 3, 2, 14, 59, 10, 44658), 'updated_at': datetime.datetime(2022, 3, 2, 14, 59, 10, 44719)}
            (hbnb) 
* all
    - Display all string representation of all instances based or not on the class name.

            (hbnb) all BaseModel
            []
            (hbnb) all Mymodel
            ** class doesn't exist **
            (hbnb) all User
            ["[User] (92cfa8a5-4664-4108-bce9-bb2e2e7f22a2) {'id': '92cfa8a5-4664-4108-bce9-bb2e2e7f22a2', 'created_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836486), 'updated_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836673)}"]
            (hbnb) 

* update
    - Updated an instance based on the class name and id by adding or updated attribute (save the change into the JSON file)

            (hbnb) update User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2 first_name "Jean"
            (hbnb) show User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2
            [User] (92cfa8a5-4664-4108-bce9-bb2e2e7f22a2) {'id': '92cfa8a5-4664-4108-bce9-bb2e2e7f22a2', 'created_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836486), 'updated_at': datetime.datetime(2022, 3, 2, 15, 5, 53, 836673), 'first_name': '"Jean"'}
            (hbnb) 

* destroy
    - Deletes an instance based on the class name and id (save the change into the JSON file).

            (hbnb) destroy User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2
            (hbnb) show User 92cfa8a5-4664-4108-bce9-bb2e2e7f22a2
            ** no instance found **
            (hbnb)
