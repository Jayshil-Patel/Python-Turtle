import turtle
import random, time

player1 = turtle.Turtle()  # creating player 1
player1.shape("turtle")
player1.penup()
player1.goto(10, 20)  # setting up player 1's postiton
player1.pendown()
player1.color('blue')  # setting up player 1's color
player1.write('Player1')

player2 = turtle.Turtle()  # creating player 1
player2.shape("turtle")
player2.penup()
player2.goto(10, 80)  # setting up player 1's postiton
player2.pendown()
player2.color('red')  # setting up player 1's color
player2.write('Player 2')

start1 = 0
start2 = 0
end = 180
# creating end circle for player 1
endTurtle1 = turtle.Turtle()
endTurtle1.penup()

# creating end circle for player1's position
endTurtle1.goto(200, 20)
endTurtle1.pendown()

# creating a circle
endTurtle1.shape('circle')

# colouring the circle
endTurtle1.fillcolor('white')

# creating end circle for player 2
endTurtle2 = turtle.Turtle()
endTurtle2.penup()

# creating end circle for player2's position
endTurtle2.goto(200, 80)
endTurtle2.pendown()

# creating a circle
endTurtle2.shape('circle')

# colouring the circle
endTurtle2.fillcolor('white')

wn = turtle.Screen()
wn.bgcolor("light green")
# running while loop until the start
# position for any player is less than end position
while start1 <= end or start2 <= end:
    if start1 >= end:
        # printing the player name in the title
        wn.title(f"Player1 position is {start1},Player2 position is {start2}, Player1 wins")
        time.sleep(5)
        break
    elif start2 >= end:
        # printing the player name in the title
        wn.title(f"Player1 position is {start1},Player2 position is {start2}, Player2 wins")
        time.sleep(5)
        break

    # dice for player1
    dicel = random.randrange(1, 6)
    # dice for player2
    dice2 = random.randrange(1, 6)
    # forwarding player1
    player1.forward(dicel * 2)
    time.sleep(1)

    # forwarding player2
    player2.forward(dice2 * 2)
    time.sleep(1)
    # increasing position values for player1
    start1 + dicel * 2
    # increasing position values for player2
    start2 += dice2 * 2
    wn.title(f"Player1 position is {start1},Player2 position is {start2}, no one wins")
time.sleep(3)
turtle.bye()
