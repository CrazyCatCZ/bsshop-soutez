# jmeno hada z konfiguracniho souboru config.py
from config import NAME

import random

# povolene smery pohybu hada
DIRECTIONS = ('Right', 'Left', 'Up', 'Down')

# nedostane data hry, vraci jmeno hada
def index():
    return NAME

# dostane data hry, vraci prazdnou odpoved
def init(game):
    return ''

# dostane data hry, vraci smer pohybu hada
def move(game):
    #
    # SEM UMISTUJTE SVUJ KOD
    #

    ALLOWED_DIRECTIONS = ['Right', 'Left', 'Up', 'Down']
    board = game['board']
    food = board['food']
    snakes = board['snakes']
    obstacles = board['obstacles']
    
    board_height = board['height']
    board_width = board['width']

    my_snake = snakes[0]
    snakes_head = my_snake['head']

    border_x_right = board_height - 1
    border_x_left = 0
    border_y_up = board_width - 1
    border_y_down = 0

    #def find_nearest_food():

    def move_is_border_x_right(): 
        return snakes_head['x'] == border_x_right
    
    def move_is_border_y_up():
        return snakes_head['y'] == border_y_up

    def move_is_border_x_left():
        return snakes_head['x'] == border_x_left

    def move_is_border_y_down():
        return snakes_head['y'] == border_y_down
    
    
    if move_is_border_x_right():
        ALLOWED_DIRECTIONS.remove('Right')

    elif move_is_border_y_up():
        ALLOWED_DIRECTIONS.remove('Up')

    elif move_is_border_x_left():
        ALLOWED_DIRECTIONS.remove('Left')

    elif move_is_border_y_down():
        ALLOWED_DIRECTIONS.remove('Down')
    
    print(board_height, board_width)
    print(snakes_head)

    # pro ukazku se vraci nahodny smer
    return {'direction': random.choice(ALLOWED_DIRECTIONS)}
