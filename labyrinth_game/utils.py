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

def solve_puzzle(game_state):
    from labyrinth_game.player_actions import get_input
    current_room_key = game_state['current_room']
    room = ROOMS[current_room_key]
    puzzle = room.get('puzzle')

    if not puzzle:
        print("Загадок здесь нет.")
        return

    question, correct_answer = puzzle
    print(question)
    answer = get_input("Ваш ответ: ").strip().lower()

    if answer == correct_answer.lower():
        print("Правильно! Вы решили загадку.")
        room['puzzle'] = None  
        if 'treasure_key' not in game_state['player_inventory']:
            game_state['player_inventory'].append('treasure_key')
            print("Вы получили ключ от сокровищницы!")
    else:
        print("Неверно. Попробуйте снова.")


def attempt_open_treasure(game_state):
    from labyrinth_game.player_actions import get_input
    current_room_key = game_state['current_room']
    room = ROOMS[current_room_key]

    if current_room_key != 'treasure_room':
        print("Здесь нет сокровищ.")
        return

    inventory = game_state['player_inventory']

    if 'treasure_key' in inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        if 'treasure_chest' in room.get('items', []):
            room['items'].remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        answer = get_input(Сундук заперт. Ввести код? (да/нет):).strip().lower()
        if answer == 'да':
            puzzle = room.get('puzzle')
            if not puzzle:
                print("Код неизвестен, сундук не открыть.")
                return

            question, correct_code = puzzle
            code = get_input("Введите код: ").strip().lower()
            if code == correct_code.lower():
                print("Код верный! Сундук открыт!")
                if 'treasure_chest' in room.get('items', []):
                    room['items'].remove('treasure_chest')
                print("В сундуке сокровище! Вы победили!")
                game_state['game_over'] = True
            else:
                print("Неверный код.")
        else:
            print("Вы отступаете от сундука.")

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")