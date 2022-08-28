import turtle

def make_outer(player):
	player.setheading(90)
	player.forward(100)
	player.setheading(0)
	player.forward(450)
	player.setheading(270)
	player.forward(100)
	player.setheading(180)
	player.forward(450)
	player.end_fill()


def make_circle(player):
	player.up()
	player.setpos(0,49)
	player.down()
	player.circle(49)

def make_spokes(player):
	for i in range(1,25):
		player.up()
		player.setpos(0,0)
		player.right(15)
		player.down()
		player.forward(49)

def make_stand(player):
	player.begin_fill()
	player.up()
	player.setpos(-225,150)
	player.setheading(180)
	player.down()
	player.forward(20)
	player.setheading(270)
	player.forward(450)
	player.setheading(0)
	player.forward(20)
	player.setheading(90)
	player.forward(450)
	player.end_fill()


def make_shape():
	window = turtle.Screen()
	window.bgcolor("white")
	window.setup(width=1.0, height=1.0, startx=None, starty=None)
	player = turtle.Turtle()
	player.shape("turtle")
	player.color("black")
	player.speed(1)

	player.up()
	player.setpos(-225,-150)
	player.down()
	player.color("green")
	player.begin_fill()
	make_outer(player)

	player.up()
	player.setpos(-225,-50)
	player.down()
	player.color("black")
	make_outer(player)

	player.up()
	player.setpos(-225,50)
	player.down()
	player.color("#ff9933")
	player.begin_fill()
	make_outer(player)

	player.color("black")
	make_circle(player)
	make_spokes(player)
	make_stand(player)
	player.up()
	player.setpos(250,200)

	window.exitonclick()

make_shape()