from sense_hat import SenseHat
import time
import random
SnakeColor = (255, 255, 255)
FoodColor = (255, 0, 0)
Blank = (0, 0, 0)
snake = [(2,4), (3,4), (4,4)]
food = (random.randint(0,8), random.randint(0,8))
Direction = "right"
sense = SenseHat()

def draw_snake():
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], SnakeColor)
def move():
    firstSegment = snake[0]
    lastSegment = snake[-1]
    next = list(lastSegment)
    if (Direction == "right"):
        if (lastSegment[0] == 7):
            next[0] = 0
        else:
            next[0] = lastSegment[0] + 1
    if (Direction == "left"):
        if (lastSegment[0] == 0):
            next[0] = 7
        else:
            next[0] = lastSegment[0] - 1
    if (Direction == "up"):
        if (lastSegment[1] == 0):
            next[1] = 7
        else:
            next[1] = lastSegment[1] - 1
    if (Direction == "down"):
        if (lastSegment[1] == 7):
            next[1] = 0
        else:
            next[1] = lastSegment[1] + 1
    snake.append(next)
    sense.set_pixel(next[0], next[1], SnakeColor)
    sense.set_pixel(firstSegment[0], firstSegment[1], Blank)
    snake.remove(firstSegment)
def joystick_moved(event):
    global Direction
    if ((Direction == "left" and event.direction == "right") or (Direction == "right" and event.direction == "left") or (Direction == "up" and event.direction == "down") or (Direction == "down" and event.direction == "up")):
        return 0
    Direction = event.direction
def draw_food():
        if (food[0] >= 0 and food[1]  >= 0):
            sense.set_pixel(food[0], food[1], FoodColor)
def handle_food():
    if (snake[-1] == food):
        food[0] = random.randint(0,8)
        food[1] = random.randint(0,8)
        print("hit")

sense.stick.direction_any = joystick_moved
while (True):
    sense.clear()
    move()
    draw_snake()
    handle_food()
    draw_food()
    time.sleep(0.25)
        
