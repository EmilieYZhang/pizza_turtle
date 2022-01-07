#Name: Emilie Yahui Zhang
#McGill ID: 261034013

#Welcome to Emilie's pizzaria

import turtle
    
def pizza_slices(turtle, num_slices, radius, slice_color):
    """ (Turtle, int, int, int, str) -> NoneType
    Makes slices of pizza by using turtle as Turtle,
    and colours it with slice_color, dividing it into a
    number of slices given by num_slices and the
    size of the slices given by radius."""
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    angle = (360/num_slices)
    turtle.color("black", slice_color)
    turtle.begin_fill()
    
    if num_slices == 1:
        turtle.penup()
        turtle.goto(0,-radius)
        turtle.pendown()
        turtle.circle(radius, angle)
    else:
        for i in range(num_slices):
            turtle.forward(radius)
            turtle.left(90)
            turtle.circle(radius, angle)
            turtle.left(90)
            turtle.forward(radius)
            turtle.left(180)
    turtle.end_fill()

def pizza_crust(turtle, c_thickness, radius_pizza,):
    """ (Turtle, int, int) -> NoneType
    Outlines the thickness of the pizza crust.
    Use turtle as Turtle. The thickness of crust determined by c_thickness
    and the diameter of crust circle will be determined given
    radius_pizza which is the radius of the pizza."""
    turtle.penup()
    turtle.goto(0, -radius_pizza)
    turtle.left(90)
    turtle.forward(c_thickness)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(radius_pizza - c_thickness)

def pepperoni_shape(turtle, radius, pepo_color):
    """ (Turtle, int, str) -> NoneType
    Draws a single pepperoni.
    turtle as Turtle draws pepperoni of a certain size determined by radius,
    and filled with color of pep_color."""
    turtle.color("black", pepo_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def pizza_pepperoni(turtle, location_x, location_y, num_pepo, diameter, pepo_radius, pepo_color):
    """ (Turtle, int, int, int, int, int, str) -> NoneType
    Adds the pepperoni topping on the pizza.
    turtle as Turtle start at position of (x, y) where x is
    at location_x and y is at location_y. The number of pepperonis is num_pepo,
    the diameter is how big of a circle the pepperonis should be placed,
    pepo_radius is radius of each pepperoni and pepo_color is the pepperoni color."""    
    turtle.penup()
    turtle.goto(location_x, location_y)
    angle_of_pepo = 360/num_pepo
    
    for i in range(num_pepo):
        turtle.pendown()
        pepperoni_shape(turtle, pepo_radius, pepo_color)
        turtle.penup()
        turtle.circle((diameter/2), angle_of_pepo)
        
def mushroom_corner(turtle, line_size):
    """ (Turtle, int) -> NoneType
    Draws the L-shaped corner of a mushroom.
    turtle as Turtle draws L pattern with each line the length of line_size."""
    turtle.forward(line_size)
    turtle.right(90)
    turtle.forward(line_size)
    turtle.left(90)

def mushroom_shape(turtle, size_diameter, mush_color):
    """ (Turtle, int, str) -> NoneType
    Draws a single mushroom with distinct shape.
    turtle as Turtle draws mushroom with its cross-sectional diameter as size_diameter,
    and fills it with color of mush_color."""
    #length of each straight side of mushroom
    line_size = size_diameter/3
    #radius of the half-circle part of mushroom
    size_radius = size_diameter/2
    turtle.color("black", mush_color)
    turtle.begin_fill()
    mushroom_corner(turtle, line_size)
    turtle.circle(size_radius, 180)
    turtle.left(90)
    mushroom_corner(turtle, line_size)
    turtle.forward(line_size)
    turtle.left(90)
    turtle.end_fill()

def pizza_mushroom(turtle, location_x, location_y, num_mush, diameter, mush_color):
    """ (Turtle, int, int, int, int, str) -> NoneType
    Adds mushroom topping to the pizza.
    Takes turtle as Turtle, location_x and location_y as the starting point of the mushroom,
    num_mush as the number of mushrooms,
    diameter as how big of a circle the mushrooms should make,
    the mush_color as the color of the mushrooms on pizza"""
    angle_of_mush = 360/num_mush
    turtle.goto(location_x, location_y)
    
    for i in range(num_mush):
        turtle.pendown()
        mushroom_shape(turtle, 90, mush_color)
        turtle.penup()
        turtle.circle((diameter/2), angle_of_mush)

def polygon_shape(turtle, num_sides, ing_color):
    """ (Turtle, int, str) -> NoneType
    Draws a single ingredient of a polygon shape.
    turtle as Turtle draws ingredient with number of sides num_sides,
    and fills it with color of ing_color."""
    turtle.color("black", ing_color)
    orientation_angle = 360/num_sides
    turtle.begin_fill()
    
    for i in range(num_sides):
        turtle.forward(60)
        turtle.right(orientation_angle)
    turtle.end_fill()

def pizza_pepper(turtle, location_x, location_y, num_pepper, diameter, pepper_color):
    """ (Turtle, int, int, int, int, str) -> NoneType
    Adds the pepper topping on the pizza.
    turtle as Turtle start at position of (x, y) where x is
    at location_x and y is at location_y. The number of peppers is num_pepper,
    the diameter is how big of a circle the peppers should be placed,
    pepper_color is the pepper color."""  
    angle_of_pepper = 360/num_pepper
    turtle.goto(location_x, location_y)
    
    for i in range(num_pepper):
        turtle.pendown()
        #decided that pepper should be cube-shaped, so a polygon with 4 sides
        polygon_shape(turtle, 4, pepper_color)
        turtle.penup()
        turtle.circle((diameter/2), angle_of_pepper)
        
def chef_signature(turtle, location_x, location_y, pen_thickness):
    """ (Turtle, int, int) -> NoneType
    Adds chef's signature by drawing letter 'E'.
    turtle as Turtle start at position of (x, y) where x is
    at location_x and y is at location_y then 'E' is drawn with
    pen size of pen_thickness."""
    #go to location on the page to start signing
    turtle.goto(location_x, location_y)
    #adjustable pen thickness
    turtle.pensize(pen_thickness)
    #use turtle to draw letter 'E'
    turtle.pendown()
    turtle.right(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.penup()
    turtle.goto((location_x-20), (location_y-20))
    turtle.pendown()
    turtle.forward(15)
            
def my_artwork():
    """ () -> NoneType
    Draws pizza artwork. """ 
    picasso = turtle.Turtle()
    picasso.speed("fastest")
    #draw the pizza outline
    picasso.pensize(15)
    pizza_slices(picasso, 7, 300, "dark salmon")    
    pizza_crust(picasso, 40, 300)
    pizza_slices(picasso, 7, 260, "khaki")
    pizza_pepperoni(picasso, 0, -200, 7, 400, 50, "crimson")
    pizza_mushroom(picasso, 0, -210, 9, 420, "sienna")
    pizza_pepper(picasso, 0, -55, 5, 110, "forest green")
    chef_signature(picasso, 380, -250, 5)
    picasso.hideturtle()