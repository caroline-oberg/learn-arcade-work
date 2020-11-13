
class Room:
    """This is a class that represents the rooms"""
    def __init__(self, description, north, northeast, northwest, southeast, east, south, southwest, west, up, down):
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

    room = Room("You are in the Waiting Room.\nThere are doors in every direction except north.", None, None, None, 4, 3, 5, 2, 1, None, None)
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

    room = Room("You have walked into the elevator.\n You can go up or the main hallway is to the east.", None, None, None, 5, None, None, None, None, 17, None)
    room_list.append(room)

    room = Room("You walked into the old Emergency Room.\nThere is one door to the north, east and west.", 5, None, None, None, 8, None, None, 6, None, None)
    room_list.append(room)

    room = Room("You are in the Janitors Closet.\nThere is a door to the east into the old Emergency Room.", None, None, None, None, 7, None, None, None, None, None)
    room_list.append(room)

    room = Room("You walked into the medical supplies closet.\nThere is one door to the west leading back to the Emergency Room.", None, None, None, None, 8, None, None, 7, None, None)
    room_list.append(room)

    current_room = 0

    # Medicine (Medical Supplies 8)
    medicine = Item(8, "medicine", "You spot life saving medicine on the counter.")
    item_list.append(medicine)

    # Scalpel (Patient room 100)
    scalpel = Item(1, "scalpel", "You see a scalpel on a tray next to the patient bed.")
    item_list.append(scalpel)

    # Blood (Main Hallway 5)
    blood = Item(5, "blood", "You see blood on the floor in the hallway")
    item_list.append(blood)

    # Chemicals (Janitors Closet 6)
    chemicals = Item(6, "chemicals", "You see cleaning chemicals on the shelf that could be useful")
    item_list.append(chemicals)

    # Phone (Emergency Room 7)
    phone = Item(7, "phone", "You see a phone that connects to the intercom on the desk in the old emergency room")
    item_list.append(phone)

    done = False
    while not done:
        print()

        print(room_list[current_room].description)
        userinput = input("What do you want to do? ")

        if userinput.lower() == "north" or userinput.lower() == "n":
            next_room = room_list[current_room].north
            if next_room == None:
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

        elif userinput.lower() == "quit" or userinput.lower() == "q":
            done = True
            print("You quit.")
main()