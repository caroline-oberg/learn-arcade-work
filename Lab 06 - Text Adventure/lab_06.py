
class Room:
    """This is a class that represents the rooms"""
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    room_list = []
    room = Room("You are in the hidden chamber.\nThere is a door to the south.", None, None, 1, None)
    room_list.append(room)
    room = Room("You are now in the west corridor.\nThere is a door to the north and the east", 0, 2, None, None)
    room_list.append(room)
    room = Room("You have entered the north hall.\nThere are doors to the east, south, and west.", None, 5, 3, 1)
    room_list.append(room)
    room = Room("You are now in the art gallery.\nThere are doors in every direction.", 2, 5, 4, 1)
    room_list.append(room)
    room = Room("You have walked onto the terrace.\nThere are doors to the north and the east.", 3, 6, None, None)
    room_list.append(room)
    room = Room("You are in the east quarters.\nThere are doors to the south and the west.", None, None, 6, 3)
    room_list.append(room)
    room = Room("You walked into the greenhouse.\nThere is one door to the north and one to the west.", 5, None, None, 4)
    room_list.append(room)
    current_room = 0
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

        elif userinput.lower() == "quit" or userinput.lower() == "q":
            done = True
            print("You quit.")
main()