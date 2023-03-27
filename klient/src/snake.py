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
    NEXT_MOVE = random.choice(ALLOWED_DIRECTIONS)
    nearest_food_index = 0
    board = game['board']
    food = board['food']
    snakes = board['snakes']
    obstacles = board['obstacles']
    
    board_height = board['height']
    board_width = board['width']

    my_snake = game['you']
    snakes_head = my_snake['head']

    border_x_right = board_height - 1
    border_x_left = 0
    border_y_up = board_width - 1
    border_y_down = 0


    #Borders
    def move_is_border_x_right(): 
        return snakes_head['x'] == border_x_right
    
    def move_is_border_y_up():
        return snakes_head['y'] == border_y_up

    def move_is_border_x_left():
        return snakes_head['x'] == border_x_left

    def move_is_border_y_down():
        return snakes_head['y'] == border_y_down
    

    def nearest_food():
        nearest_food_index = 0

        for i in range(len(food)):
            first_number_x = 0
            second_number_x = 0
            first_number_y = 0
            second_number_y = 0

            current_food = food[i]

            # X cordination
            if current_food['x'] > snakes_head['x']:
                first_number_x = current_food['x']
                second_number_x = snakes_head['x']
            else:
                first_number_x = snakes_head['x']   
                second_number_x = current_food['x']   

            #Y cordination
            if current_food['y'] > snakes_head['y']:
                first_number_y = current_food['y']
                second_number_y = snakes_head['x']   
            else:
                first_number_y = snakes_head['y']   
                second_number_y = current_food['y'] 

            result_x = first_number_x - second_number_x
            result_y = first_number_y - second_number_y

            if result_x < food[nearest_food_index]['x'] and result_y < food[nearest_food_index]['y']:
                nearest_food_index = i

        print(f"Nearest food: {nearest_food_index}")
    
    #Borders 
    if move_is_border_x_right():
        ALLOWED_DIRECTIONS.remove('Right')

    if move_is_border_y_up():
        ALLOWED_DIRECTIONS.remove('Up')

    if move_is_border_x_left():
        ALLOWED_DIRECTIONS.remove('Left')

    if move_is_border_y_down():
        ALLOWED_DIRECTIONS.remove('Down')
    
    nearest_food()

    if len(food) != 0:
        nearest_food_var = food[nearest_food_index]
        #Go for nearest food on x
        difference_x = snakes_head['x'] - nearest_food_var['x']
        if difference_x != 0:
            if difference_x < 0:
                NEXT_MOVE = 'Right'
            else:
                NEXT_MOVE = 'Left'

        #Go for nearest food on y
        difference_y = snakes_head['y'] - nearest_food_var['y']
        if difference_y != 0:
            if difference_y < 0:
                NEXT_MOVE = 'Up'
            else:
                NEXT_MOVE = 'Down'
    
    if NEXT_MOVE in ALLOWED_DIRECTIONS:
        return {'direction': NEXT_MOVE}
    else:
        return {'direction': random.choice(ALLOWED_DIRECTIONS)}
    
