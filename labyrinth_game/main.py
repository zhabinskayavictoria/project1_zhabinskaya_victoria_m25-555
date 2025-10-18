#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS
from labyrinth_game.player_actions import *
from labyrinth_game.utils import describe_current_room

game_state = {
    'player_inventory': [],
    'current_room': 'entrance',
    'game_over': False,
    'steps_taken': 0
}
def process_command(game_state, command):
    parts = command.strip().split(maxsplit=1)
    action = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else None

    match action:
        case 'look':
            describe_current_room(game_state)
        case 'inventory':
            show_inventory(game_state)
        case 'go':
            if arg:
                move_player(game_state, arg.lower())
            else:
                print("Вы не указали направление.")
        case 'take':
            if arg:
                take_item(game_state, arg.lower())
            else:
                print("Вы не указали предмет.")
        case 'use':
            if arg:
                use_item(game_state, arg.lower())
            else:
                print("Вы не указали предмет.")
        case 'quit' | 'exit':
            print("Выход из игры. Пока!")
            game_state['game_over'] = True
        case _:
            print(f"Неизвестная команда: {action}")
            
def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    
    while not game_state['game_over']:
        command = get_input()
        process_command(game_state, command)
        
        
if __name__ == "__main__":
    main()
    
    
    