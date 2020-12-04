"""
Hospital Game
"""


class Room:
    """This is a class that represents the rooms"""
    def __init__(self, description,
                 north, northeast, northwest, southeast,
                 east, south, southwest, west, up, down):
        self.description = description
        self.north = north
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.east = east
        self.southwest = southwest
        self.south = south
        self.west = west
        self.up = up
        self.down = down


class Item:

    def __init__(self, room, name, description):
        self.room = room
        self.name = name
        self.description = description


def main():
    room_list = []
    item_list = []

    room = Room("You are in the waiting room.\n"
                "There are doors in every direction except north.",
                None, None, None, 4, 3, 5, 2, 1, None, None)
    room_list.append(room)

    room = Room("You are now in Patient Room 100.\nThere is a door to the east", None, None, None, None, 0, None, None, None, None, None)
    room_list.append(room)

    room = Room("You have entered Patient Room 101.\nThere is a door to the east", None, None, None, None, 0, None, None, None, None, None)
    room_list.append(room)

    room = Room("You are now in Patient Room 102.\nThere is a door to the west.", None, None, None, None, None, None, None, 0, None, None)
    room_list.append(room)

    room = Room("You are now in Patient Room 103.\nThere is a door to the west.", None, None, None, None, None, None, None, 0, None, None)
    room_list.append(room)

    room = Room("You have walked into the main hallway.\nThere is an elevator to the west and rooms to the north and south.", 0, None, None, None, None, 7, None, 9, None, None)
    room_list.append(room)

    room = Room("You have walked into the elevator.\n You can go up or the main hallway is to the east.", None, None, None, None, 5, None, None, None, 17, None)
    room_list.append(room)

    room = Room("You walked into the old emergency room.\nThere is one door to the north and west. There is a locked door to the east.", 5, None, None, None, None, None, None, 6, None, None)
    room_list.append(room)

    room = Room("You are in the janitor's closet.\nThere is a door to the east into the old Emergency Room.", None, None, None, None, 7, None, None, None, None, None)
    room_list.append(room)

    room = Room("You walked into the medical supplies closet.\nThere is one door to the west leading back to the Emergency Room.", None, None, None, None, 8, None, None, 7, None, None)
    room_list.append(room)

    # Represent the current room the user is in.
    current_room = 0

    # Medicine (Medical Supplies 8)
    medicine = Item(8, "medicine", "You spot life saving medicine on the counter.")
    item_list.append(medicine)

    # Scalpel (Patient room 100)
    scalpel = Item(1, "scalpel", "You see a scalpel on a tray next to the patient bed.")
    item_list.append(scalpel)

    # Blood (Main Hallway 5)
    blood = Item(5, "blood", "You see blood on the floor in the hallway.")
    item_list.append(blood)

    # Chemicals (Janitors Closet 6)
    chemicals = Item(6, "chemicals", "You see cleaning chemicals on the shelf that could be useful.")
    item_list.append(chemicals)

    # Phone (Emergency Room 7)
    phone = Item(7, "phone", "You see a phone that connects to the intercom on the desk in the old emergency room.")
    item_list.append(phone)

    #Key (Patient Room 4)
    key = Item(4, "key", "You see a key labeled janitor's closet.")
    item_list.append(key)

    print("Welcome to the apocalypse.\nYou decided to make a trip to the hospital to look for supplies.\nOn your way there you realize you've been infected from someone that was hiding their symptoms.")
    print("Your goal is to find the cure while you still can.")
    print("Use the command 'get' and then type the item and hit enter to pick it up.\nTo use the item type 'use' and then said item and hit enter.")
    print("Good luck!")

    done = False
    while not done:
        print()

        # Print room description
        print(room_list[current_room].description)
        # Printing items in the room
        for item in item_list:
            if item.room == current_room:
                print(item.description)

        # User action input
        userinput = input("What would you like to do? ")
        command_words = userinput.split(" ")

        if userinput.lower() == "north" or userinput.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "east" or userinput.lower() == "e":
            next_room = room_list[current_room].east
            if next_room == None:
                print ("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "south" or userinput.lower() == "s":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "west" or userinput.lower() == "w":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "northeast" or userinput.lower() == "ne":
            next_room = room_list[current_room].northeast
            if next_room == None:
                print ("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "southeast" or userinput.lower() == "se":
            next_room = room_list[current_room].southeast
            if next_room == None:
                print ("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "southwest" or userinput.lower() == "sw":
            next_room = room_list[current_room].southwest
            if next_room == None:
                print ("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "up" or userinput.lower() == "u":
            next_room = room_list[current_room].up
            if next_room == None:
                print ("You can't go that way.")
            else:
                current_room = next_room

        elif userinput.lower() == "down" or userinput.lower() == "d":
            next_room = room_list[current_room].down
            if next_room == None:
                print ("You can't go that way.")
            else:
                current_room = next_room

        # Stealing the medicine
        elif command_words[0] == "steal":
            if len(command_words) > 1:
                if command_words[1] == "medicine":
                    if item_list[0].room == current_room:
                        item_list[0].room = -1
                        print()
                        print("You took the medicine off the counter and pocketed it, which will be useful later.")
                    else:
                        print("You are not in the right room for that item.")
            else:
                print("What would you like to steal?")

        # Print out the inventory
        elif command_words[0] == "inventory":
            for item in item_list:
                if item.room == -1:
                    print(item.name)

        elif command_words[0] == "get":
            for item in item_list:
                if len(command_words) > 1:
                    if command_words[1] == item.name and item.room == current_room:
                        item.room = -1
                        print()
                        print ("You've picked it up.")

        elif command_words[0] == "drop":
            if len(command_words) > 1:
                for item in item_list:
                    if command_words[1] == item.name and item.room == -1:
                        item.room = current_room
                        print("You have dropped that item.")
            else:
                print("What would you like to drop?")

        elif command_words[0] == "use":
            if len(command_words) > 1:
                if command_words[1] == "medicine":
                    if item_list[0].room == -1:
                        print()
                        print("You have decided to use the medicine, it cured you and prevents you from catching the virus again.")
                        print()
                        print("Congratulations, you live to see another day.\n Game Over. ")
                        done = True
                    else:
                        print("You have to get the medicine before you can use it.")
                elif command_words[1] == "key":
                    if key.room == -1:
                        print()
                        print("You have used the key to unlock the janitor's closet.")
                        room_list[7].east = 8
                        room_list[7].description = "You walked into the old emergency room.\nThere is one door to the north and west. There is an unlocked door to the east."
                    else:
                        print("You have to get the medicine before you can use it.")
                else:
                    print("That can't be used.")
            else:
                print("What would you like to use?")

        elif userinput.lower() == "quit" or userinput.lower() == "q":
            done = True
            print("You quit.")


main()
