from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


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
        next_room = exits[direction]
        if next_room == 'treasure_room':
            if 'rusty_key' in game_state['player_inventory']:
                print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")
                game_state['current_room'] = 'treasure_room'
            else:
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
                return
        else:
            game_state['current_room'] = next_room

        game_state['steps_taken'] += 1
        describe_current_room(game_state)
        random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")
        
def take_item(game_state, item_name):
    current_room = game_state['current_room']
    room_items = ROOMS[current_room].get('items', [])
    if item_name == 'treasure_chest':
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return
    if item_name in room_items:
        game_state['player_inventory'].append(item_name)
        room_items.remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")
        
def use_item(game_state, item_name):
    inventory = game_state.get('player_inventory', [])
    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return
    if item_name == 'torch':
        print("Светло становится вокруг вас.")
    elif item_name == 'sword':
        print("Вы чувствуете уверенность в своих силах.")
    elif item_name == 'bronze_box':
        if 'rusty_key' not in inventory:
            inventory.append('rusty_key')
            print("Вы открыли бронзовую шкатулку и нашли в ней ржавый ключ.")
        else:
            print("Шкатулка пуста.")
    else:
        print("Вы не знаете, как использовать этот предмет.")

