
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
    room = Room("Hidden Chamber", None, None, 1, None)
    room_list.append(room)
    room = Room("West Corridor", 0, 2, None, None)
    room_list.append(room)
    room = Room("North Hall", None, 5, 3, 1)
    room_list.append(room)
    room = Room("South Hall", 2, 5, 4, 1)
    room_list.append(room)
    room = Room("The Terrace", 3, 6, None, None)
    room_list.append(room)
    room = Room("East Quarters", None, None, 6, 3)
    room_list.append(room)
    room = Room("The Greenhouse", 5, None, None, 4)
    room_list.append(room)
    current_room = 0
    done = False
    while not done:
        print()

    print(room_list[0].description)

    if userinput.lower() = input("north")
        next_room = [room_list[current_room].north]
        if next_room == None
            print("You can't go that way.")
            else current_room = next_room

    elif userinput.lower() = "east"
        next_room = [room_list[current_room].east]
        if next_room == None
            print ("You can't go that way.")
            else current_room = next_room

    elif userinput.lower() = "south"
        next_room = [room_list[current_room].south]
        if next_room == None
            print("You can't go that way.")
            else current_room = next_room

    elif userinput.lower() = "west"
        next_room = [room_list[current_room].west]
        if next_room == None
            print("You can't go that way.")
            else current_room = next_room

    if userinput.lower() == "quit"
        done = True
main()