#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS, COMMANDS
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)

game_state = {
    'player_inventory': [],
    'current_room': 'entrance',
    'game_over': False,
    'steps_taken': 0
}
def process_command(game_state, command_line, commands):
    parts = command_line.strip().split(maxsplit=1)
    action = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else None
    directions = ['north', 'south', 'east', 'west']

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
        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case 'help':
            show_help(commands)
        case 'quit' | 'exit':
            print("Выход из игры. Пока!")
            game_state['game_over'] = True
        case _ if action in directions:
            move_player(game_state, action)
        case _:
            print(f"Неизвестная команда: {action}")

            
def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    
    while not game_state['game_over']:
        command_line = get_input()
        process_command(game_state, command_line, COMMANDS)
        
        
if __name__ == "__main__":
    main()
    
    
    