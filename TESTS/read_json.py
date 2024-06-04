import json


def read_json():
    with open(file="user.json", mode="r+") as file:
        user = json.load(file)

        return user


def modify_json():
    with open(file="user.json", mode="w") as file:
        name = input("write your name: ")
        lastname = input("write your last name: ")
        age = input("enter your age: ")

        json.dump(
            {"name": name.capitalize(), "lastname": lastname.capitalize(), "age": age},
            file,
            indent=4,
        )


modify_json()
print(read_json())
