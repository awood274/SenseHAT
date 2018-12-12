from sense_hat import SenseHat
import time
import random
SnakeColor = (255, 255, 255)
FoodColor = (255, 0, 0)
Blank = (0, 0, 0)
snake = [(0,4), (1,4), (2,4)]
food = [random.randint(0,7), random.randint(0,7)]
Direction = "right"
sense = SenseHat()
LastEaten = time.time()
Wait = 0.35
Cooldown = 5.0
Score = 0

def draw_snake():
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], SnakeColor)
def GameOver():
    sense.show_message("Game Over!! Score: %s" % Score)
    snake = []
def move():
    global LastEaten
    global Wait
    global snake
    global Cooldown
    global Score
    
    remove = True
    firstSegment = snake[0]
    lastSegment = snake[-1]
    next = list(lastSegment)
    if (Direction == "right"):
        if (lastSegment[0] == 7):
            GameOver()
            return False
        else:
            next[0] = lastSegment[0] + 1
    if (Direction == "left"):
        if (lastSegment[0] == 0):
            GameOver()
            return False
        else:
            next[0] = lastSegment[0] - 1
    if (Direction == "up"):
        if (lastSegment[1] == 0):
            GameOver()
            return False
        else:
            next[1] = lastSegment[1] - 1
    if (Direction == "down"):
        if (lastSegment[1] == 7):
            GameOver()
            return False
        else:
            next[1] = lastSegment[1] + 1

    if (next == food):
        first = True
        while (first or food in snake):
            food[0] = random.randint(0,7)
            food[1] = random.randint(0,7)
            first = False
        remove = False
        LastEaten = time.time()
        Wait -= 0.01
        Cooldown -= 0.05
        Score += 1
    elif (next in snake or (len(snake) == 1 and time.time() - LastEaten >= Cooldown)):
        GameOver()
        return False
            
    snake.append(next)
    sense.set_pixel(next[0], next[1], SnakeColor)
    if (remove):
        sense.set_pixel(firstSegment[0], firstSegment[1], Blank)
        snake.remove(firstSegment)

    return True
def joystick_moved(event):
    global Direction
    if (Direction == "middle" or (Direction == "left" and event.direction == "right") or (Direction == "right" and event.direction == "left") or (Direction == "up" and event.direction == "down") or (Direction == "down" and event.direction == "up")):
        return 0
    Direction = event.direction
def draw_food():
        if (food[0] >= 0 and food[1]  >= 0):
            sense.set_pixel(food[0], food[1], FoodColor)

sense.stick.direction_any = joystick_moved
while (True):
    sense.clear()
    if (move() == False):
        break;
    if (time.time() - LastEaten >= Cooldown):
        LastEaten = time.time()
        snake.remove(snake[-1])
    draw_snake()
    draw_food()
    time.sleep(Wait)

