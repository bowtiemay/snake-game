import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0
lives = 3                                  # I created lives. You start with three lives, and every time
                                           # you run into the border or the snake body you lose a life.
# Set up the screen                        # Once you get to zero lives, the screen will print "GAME OVER"
wn = turtle.Screen()                       # and you click the screen to exit the game.
wn.title("Snake Game")
wn.bgcolor("blue")
wn.bgpic("Grass.gif")
wn.setup(width = 600, height = 600)
wn.tracer(0) #turns off the screen updates

wn.register_shape("snakehead.gif")         # I wrote this code to register all of the images
wn.register_shape("snakeheaddown.gif")     # that I would be using throughout the game.
wn.register_shape("snakeheadleft.gif")
wn.register_shape("snakeheadright.gif")
wn.register_shape("body.gif")
wn.register_shape("mouse.gif")


# Snake head
head = turtle.Turtle()                     # This section is code I followed along with Christian
head.speed(0)                              # Thompson's youtube video. This code creates the snake
head.shape("snakehead.gif")                # head, snake food and pen.
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("mouse.gif")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.pendown()
font = ("Courtier", 24, "normal")
pen.write("Score : 0  High Score : 0  Lives : 3", align="center", font=font)


# Functions
def go_up():                                # This code is a combination of Christian Thomson's tutorial
    if head.direction != "down":            # code and mine. I made it so that the snake head image changes
        head.direction = "up"               # direction according to direction of the snake head itself.
        head.shape("snakehead.gif")

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("snakeheaddown.gif")

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("snakeheadleft.gif")

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("snakeheadright.gif")

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()                              # Christian Thompson said to use the a, s, d, w keys but
wn.onkeypress(go_up, "Up")               # I prefer the arrow keys, so changed it
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the boarder
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        lives -= 1

        # Hide the segments:
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        # Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}  Lives: {}".format(score, high_score, lives), align="center", font=font)

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("body.gif")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay                  # Bug- the screen started to lag as the snake got longer
        delay -= 0.001                       # so I had to update and shorten the delay using the
                                             # time module. This was Thompson's idea.
        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}  Lives: {}".format(score, high_score, lives), align = "center", font = font)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            lives -= 0

            # Hide the segments:
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

    time.sleep(delay)

    if lives == 0:                                 # my code - if the number of lives is 0, print "GAME
        pen.goto(0,0)                              # OVER" and exit the game by clicking the screen.
        font = ("Courtier", 48, "normal")
        pen.write("GAME OVER", align="center", font=font)
        wn.exitonclick()


wn.mainloop()
