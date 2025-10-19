# Лабиринт сокровищ :boom:
 
Это текстовая приключенческая игра на Python. Игрок блуждает по комнатам, собирает артефакты в инвентарь, разгадывает ребусы и охотится за главным призом, но в лабиринте есть ловушки и случайные события!

# :one: Установка
### Установка зависимостей через Poetry
```
poetry install
```
### Или через Makefile
```
make install
```

# :two: Запуск
### Запуск через Poetry
```
poetry run project
```
### Или через Makefile
```
make project
```
### Другое
```
# Сборка пакета
make build

# Проверка кода (линтер)
make lint

# Публикация пакета 
make publish

# Установка собранного пакета
make package-install
```


# Игровые команды :speech_balloon:
| Команда | Описание | 
|----------------|---------|
| look | Осмотреть текущую комнату|
| go \<direction> |  Перейти в направлении (north/south/east/west)|
| north, south, east, west  | Быстрое перемещение|
| take \<item> | Поднять предмет|
| use \<item>  | Использовать предмет из инвентаря|
| inventory |  Показать инвентарь|
| solve  | Решить загадку в комнате|
| help  | Показать список команд|
| quit / exit |  Выйти из игры|

# Демонстрация игрового процесса :movie_camera:
Показаны два варианта выигрыша: 
- с помощью ключа treasure_key,
- с помощью решения головоломки. 

А также показаны все основные команды, ловушка и возможность выхода из игры.

[демонстрация](https://asciinema.org/a/pxrVwj9Oumkak76sIlVmCOuw5)

[![asciicast](https://asciinema.org/a/pxrVwj9Oumkak76sIlVmCOuw5.svg)](https://asciinema.org/a/pxrVwj9Oumkak76sIlVmCOuw5)
