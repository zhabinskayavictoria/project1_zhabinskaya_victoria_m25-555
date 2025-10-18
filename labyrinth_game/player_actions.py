from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, show_inventory

def show_inventory(game_state):
    inventory = game_state['player_inventory']

    if inventory:
        print("Ваш инвентарь:")
        for item in inventory:
            print(f" - {item}")
    else:
        print("Ваш инвентарь пуст.")

def get_input(prompt="> "):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    exits = room_data.get('exits', {})
    if direction in exits:
        game_state['current_room'] = exits[direction]
        game_state['steps_taken'] += 1
        describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")
        
def take_item(game_state, item_name):
    current_room = game_state['current_room']
    room_items = ROOMS[current_room].get('items', [])
    if item_name in room_items:
        game_state['player_inventory'].append(item_name)
        room_items.remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")
        
