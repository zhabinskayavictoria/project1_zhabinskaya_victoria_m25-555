#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS
from labyrinth_game.player_actions import get_input, show_inventory
from labyrinth_game.utils import describe_current_room

game_state = {
    'player_inventory': [],
    'current_room': 'entrance',
    'game_over': False,
    'steps_taken': 0
}

def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    
    while not game_state['game_over']:
        command = get_input()
        if command in ("quit"):
            print("Выход из игры. Пока!")
            break
        
        
if __name__ == "__main__":
    main()
    