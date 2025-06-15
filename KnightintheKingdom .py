
import random

g_locations = {
    'Tower': {'north': 'Throne Room', 'east': 'Armory', 'south': 'Dungeon', 'item': 'map'},
    'Throne Room': {'south': 'Tower', 'item': 'crown'},
    'Armory': {'west': 'Tower', 'north': 'Library', 'item': 'sword'},
    'Library': {'south': 'Armory', 'item': 'spellbook'},
    'Dungeon': {'north': 'Tower', 'item': 'dragon'}
}

#  Here I can distribute the game 
# items on random locations, ensuring that each room has at most one item
# and all are used.
def distribuite_items_randomly(locations):
    items = ['map', 'crown', 'sword', 'spellbook', 'dragon']
    rooms = list(locations.keys())
    random.shuffle(items)  # "here i am shuffling all the items with the method shuffle"

    # here i can remove all items frmo the rooms
    for room in rooms:
        if 'item' in locations[room]:
            del locations[room]['item']
    # Assign one item to each room
    for room, item in zip(rooms, items):
        locations[room]['item'] = item
    
def show_game_options() -> None:
    # "Instructions for the game"
    print(
        "The 'Knight in the Kingdom', a textual \"Adventure Game\"\n"
        "===================\n"
        "Commands:\n"
        "  go [north|south|east|west] - Move in the specified direction\n"
        "  get [item] - Pick up an item\n"
        "  inspect room - See the items in the current room\n"
        "  inspect inventory - See the items in your inventory\n"
    )
     
def show_status(current_location: str, locations: dict) -> None:
    # the current room of the player
    print(f"You are in {current_location}")

    # I created an list empty to store directions and considered only the 4 possile directions
    directions = []
    for d in ['north', 'south', 'east', 'west']:
        if d in locations[current_location]:
            directions.append(d)

    # if there is a valid direction, we can join them for display
    if directions:
        print("Direction allowed " + " or ".join(directions))
    # here I tell if there are no directions I inform the player
    else:  
        print("There are no exits from this room") 

def inspect_inventory(inventory: list) -> None:
    # I can check if there are items on the player inventory using the if and the join method
    if inventory:
        print("Your inventory contains: " + ", ".join(inventory))
    else:
        # Inventory is empty
        print("Your inventory is empty.")

def inspect_location(current_location: str, locations: dict) -> None:
    # Prints the item found in the current room, if any
    # on the if block I check if the item key existes on the room, if exists prints on the console.
    if 'item' in locations[current_location]:
        print(f"In this location I see {locations[current_location]['item']}")
    else:
        # If there are no item found 
        print("There is nothing to see here.")

def get_command() -> tuple:
    """
    reads input from the player and splits it into (action, target).
    The input is made case-insensitive and trimmed for extra spaces.
    Returns a tuple: (action, target). If the input is empty, returns ('', '').
    """
    command = input("> ").strip().lower()  # read input, remove extra spaces, make lowercase

    # spliting the input into up to 2 parts ('go north' -> ['go', 'north'])
    parts = command.split(maxsplit=1)

    # if the user entered two words ("go north'), 
    # return the first as action and the second as target
    if len(parts) == 2:
        return parts[0], parts[1]
    # If the user entered only one word (e.g., 'get'), 
    # return it as action and an empty string as target
    elif len(parts) == 1:
        return parts[0], ''
    # If the input was empty, return two empty strings
    else:
        return '', ''
    
def move_to_next_location(current_location: str, target: str, locations: dict) -> str:
    """
    Checks if the move in the requested direction is allowed from the current location.
    If yes, returns the name of the next location. Otherwise, returns the current location.
    """
    # check if the requested direction (target) exists in the current location
    if target in locations[current_location]:
        # get the name of the next location from the dictionary
        next_location = locations[current_location][target]
        print(f"You move {target} to the {next_location}.")
        return next_location
    else:
        # direction not allowed from this room
        print("You can't go that way.")
        return current_location

def pickup_item(target: str, inventory: list, current_location: str, locations: dict) -> None:
    """
    Handles picking up an item from the current location.
    If the requested item exists in the current room, it is added to the player's inventory and removed from the room.
    Otherwise, a message is shown saying the item is not here.
    """
    # check if the 'item' key exists in the current room and matches the requested item
    if 'item' in locations[current_location] and locations[current_location]['item'] == target:
        # adding the item to the inventory
        inventory.append(target)
        # show a confirmation message to the player
        print(f"{target} picked up!")
        # remove the item from the room
        del locations[current_location]['item']
    else:
        # If the item is not found in the current room
        print(f"Sorry, I do not see {target} here")

def game_mainloop(first_location: str, locations: dict) -> bool:
    """
    Main game loop that keeps running until the player wins or loses.
    Handles all the major game events and player actions.
    """
    current_location = first_location  # start in the initial room (usually 'Tower')
    inventory = []  # player's inventory starts empty
    show_game_options()  # Show the instructions at the start

    while True:
        show_status(current_location, locations)  # Show where the player is

        # Get the player's command (action and target)
        move = get_command()

        if move:
            action, target = move

            if action == "go":
                current_location = move_to_next_location(current_location, target, locations)

            elif action == "get":
                pickup_item(target, inventory, current_location, locations)

            elif action == "inspect":
                if target == "inventory":
                    inspect_inventory(inventory)
                elif target == "room":
                    inspect_location(current_location, locations)
                else:
                    print("Cannot inspect that")

        else:
            print("Invalid command. Try 'go [direction]', 'get [item]', or 'inspect [room/inventory]'.")

        # WINNING CONDITION: If player is in Throne Room with both crown and sword, they win
        if current_location == 'Throne Room' and 'crown' in inventory and 'sword' in inventory:
            print("Congratulations! You have claimed the throne with the crown and the sword!")
            break

        # DRAGON LOGIC:
        # If the player finds the dragon...
        if 'item' in locations[current_location] and locations[current_location]['item'] == 'dragon':
            # If the player has the sword or the spellbook, they defeat the dragon and keep playing
            if 'sword' in inventory or 'spellbook' in inventory:
                print("You encountered the dragon, but you defeated it with your mighty weapon!")
                # Remove the dragon from the room (so it can't be found again)
                del locations[current_location]['item']
            else:
                # Player loses if they don't have the required items
                print("The dragon has defeated you... Game Over!")
                break

# starts game
if __name__ == "__main__":
    distribuite_items_randomly(g_locations)
    game_mainloop('Tower', g_locations)

