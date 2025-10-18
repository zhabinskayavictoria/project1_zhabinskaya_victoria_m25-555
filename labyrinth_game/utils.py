from labyrinth_game.constants import ROOMS

def describe_current_room(game_state):
    current_room_key = game_state['current_room']
    room = ROOMS[current_room_key]

    print(f"== {current_room_key.upper()} ==")
    print(room['description'])

    if room['items']:
        print("Заметные предметы:")
        for item in room['items']:
            print(f" - {item}")

    exits_list = ', '.join(room['exits'].keys())
    print(f"Выходы: {exits_list}")

    if room['puzzle'] is not None:
        print("Кажется, здесь есть загадка (используйте команду solve).")


