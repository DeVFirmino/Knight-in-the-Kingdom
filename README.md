# Knight-in-the-Kingdom



A text-based adventure game in Python.

## Description

Knight in the Kingdom is a simple text adventure game where you explore rooms, collect items, and face challenges like a dragon. Your goal is to claim the throne by reaching the Throne Room with both the crown and the sword in your inventory. 

## How to Play

1. **Clone or download this repository.**
2. Make sure you have Python 3 or VSCode installed.
3. Run the game from your terminal:

   ```bash
   python3 script_timed_test_one_template.py
   ```

4. Follow the on-screen instructions to play.

## Available Commands

- `go [north|south|east|west]`  
  Move in the specified direction, if possible.

- `get [item]`  
  Pick up an item in the current room.

- `inspect room`  
  See the item in the current room.

- `inspect inventory`  
  See the items you have collected.

## Objective

- Win the game by reaching the **Throne Room** with both the **crown** and the **sword** in your inventory.
- If you encounter the dragon without the sword or spellbook, you lose.

## Example Gameplay

```
The 'Knight in the Kingdom', a textual "Adventure Game"
===================
Commands:
  go [north|south|east|west] - Move in the specified direction
  get [item] - Pick up an item
  inspect room - See the items in the current room
  inspect inventory - See the items in your inventory

You are in Tower
Direction allowed north or east or south
> inspect room
In this location I see map
> get map
map picked up!
> go north
You move north to the Throne Room.
...
```

## Code Structure

- **script_timed_test_one_template.py**: Contains all the game logic, including movement, item collection, inventory, and win/lose conditions.

## Author

Daniel Dias

---

Feel free to contribute or suggest improvements!
