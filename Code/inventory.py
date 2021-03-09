

def print_menu():
    print("Type the numbers if you want to add, remove or check your list")
    print()
    print("MENU")
    print()
    print("1 - add")
    print("2 - remove")
    print("3 - show inventory")
    print("4 - save inventory")
    print("5 - load inventory")
    print()

def add_item():
    while (True):
        users_additions = input(
            "Enter something you'd like to add into your inventory: ")
        if users_additions == "done":
            break
        else:
            users_list.append(users_additions)

def remove_item():
    while (True):
        users_removals = input(
            "Enter somethign you'd like to remove from your list: ")
        if users_removals == "done":
            break
        else:
            if (users_removals in users_list):
                users_list.remove(users_removals)
            else:
                print(users_removals, "is not present in inventory")

def save_to_file():
    f = open("inventory_savings.txt", "w")
    for element in users_list:
        f.write(element + "\n")
    f.close()
    print("It's printed into the file :)")


def load_from_file():
    f = open("inventory_savings.txt", "r")
    data_from_file = f.readlines()

    # First approach
    for item in data_from_file:
        users_list.append(item.replace("\n", ""))

    # Second approach
    # users_list = []
    # for item in data_from_file:
    #     users_list.append(item.replace("\n",""))

    print("Data was loaded")

users_list = []

print("Type done in the section to exit from them")
print("And type exit twice if you want to leave")

while True:
    print_menu()

    users_input = input("Enter the number where you want to go: ")

    if (users_input == "done"):
        break

    elif (users_input == "1"):
        add_item()

    elif (users_input == "2"):
        remove_item()

    elif (users_input == "3"):
        print("Here is your list: ", users_list)

    elif (users_input == "4"):
        save_to_file()

    elif (users_input == "5"):
        load_from_file()
