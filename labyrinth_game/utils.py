from labyrinth_game.constants import ROOMS
from labyrinth_game.constants import CONST_RANDOM_1, CONST_RANDOM_2
import math

def pseudo_random(seed, modulo):
    x = math.sin(seed * CONST_RANDOM_1) * CONST_RANDOM_2
    frac = x - math.floor(x)
    return int(frac * modulo)

def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state.get('player_inventory', [])
    if inventory:
        index = pseudo_random(game_state.get('steps_taken', 0), len(inventory))
        lost_item = inventory.pop(index)
        print(f"Вы потеряли предмет: {lost_item}")
    else:
        damage = pseudo_random(game_state.get('steps_taken', 0), 10)
        if damage < 3:
            print("Вы получили смертельное ранение от ловушки. Игра окончена.")
            game_state['game_over'] = True
        else:
            print("Вы уцелели, но было опасно!")

def random_event(game_state):
    if pseudo_random(game_state.get('steps_taken', 0), 10) != 0:
        return  

    event_type = pseudo_random(game_state.get('steps_taken', 0) + 1, 3)

    current_room = game_state['current_room']
    inventory = game_state.get('player_inventory', [])

    if event_type == 0:
        print("Вы нашли на полу монетку.")
        ROOMS[current_room].setdefault('items', []).append('coin')

    elif event_type == 1:
        print("Вы слышите странный шорох.")
        if 'sword' in inventory:
            print("Благодаря мечу, вы отпугнули существо.")

    else:  
        if current_room == 'trap_room' and 'torch' not in inventory:
            print("Внимание! Ловушка сработала!")
            trigger_trap(game_state)


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
    alt_answers = {
        '10': ['десять'],
        'шаг шаг шаг': ['три шага'],
        'буква м': ['м']
    }
    print(question)
    answer = get_input("Ваш ответ: ").strip().lower()
    valid_answers = [correct_answer.lower()] + alt_answers.get(correct_answer.lower(), [])

    if answer in valid_answers:
        print("Правильно! Вы решили загадку.")
        room['puzzle'] = None  
        if current_room_key == 'trap_room':
            print("Вы обезвредили ловушку!")
        if 'treasure_key' not in game_state['player_inventory'] and current_room_key != 'trap_room':
            game_state['player_inventory'].append('treasure_key')
            print("Вы получили ключ от сокровищницы!")
    else:
        print("Неверно. Попробуйте снова.")
        if current_room_key == 'trap_room':
            from labyrinth_game.utils import trigger_trap
            trigger_trap(game_state)


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
        answer = get_input("Сундук заперт. Ввести код? (да/нет):").strip().lower()
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

def show_help(commands):
    print("\nДоступные команды:")
    for cmd, desc in commands.items():
        print(f"  {cmd:<16} - {desc}")