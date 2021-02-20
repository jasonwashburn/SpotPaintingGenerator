from turtle import Turtle, Screen
from random import choice
import colorgram


def get_image_colors(image_path, num_colors):
    # returns a list of colors extracted from the requested image
    # ARGS:
    #   image: path to image file
    #   num_colors: number of colors to extract
    colors = colorgram.extract(image_path, num_colors)
    return [(colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b) for i in range(len(colors))]


# Set painting specifics
gap = 50
radius = 20
number_of_rows = 10
spots_per_row = 10
margin = 2 * radius
image_sample_path = "./image.jpg"


# Create our Screen and Turtle
width = (gap * (spots_per_row - 1)) + ((2 * radius) * spots_per_row)
height = (gap * (number_of_rows - 1)) + ((2 * radius) * spots_per_row)
screen = Screen()
screen.colormode(255)
screen.screensize(width + (2 * margin), height + (2 * margin))
screen.setworldcoordinates(0, 0, width + (2 * margin), height + (2 * margin))
tim = Turtle()
tim.speed(0)

# Get colors from sample image
color_list = get_image_colors(image_sample_path, 30)

starting_location = ((margin + radius), margin)
for i in range(number_of_rows):
    tim.penup()
    tim.setpos(starting_location[0], starting_location[1] + (i * ((2 * radius) + gap)))
    for _ in range(spots_per_row):
        color = choice(color_list)
        tim.color(color)
        tim.fillcolor(color)
        tim.pendown()
        tim.begin_fill()
        tim.circle(radius)
        tim.end_fill()
        tim.penup()
        tim.forward(gap + (radius * 2))

screen.exitonclick()
