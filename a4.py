"""
A module to draw cool shapes with the introcs Turtle.

Renee Gowda (rsg276) and Muskan Gupta (mg2479)
October 31st, 2024
"""
from introcs.turtle import Window, Turtle, Pen
import introcs  # For the RGB and HSV objects
import math     # For the math computations


################# Helpers for Precondition Verification #################
def is_number(x):
    """
    Returns: True if value x is a number; False otherwise.

    Parameter x: the value to check
    Precondition: NONE (x can be any value)
    """
    return type(x) in [float, int]


def is_window(w):
    """
    Returns: True if w is a introcs Window; False otherwise.

    Parameter w: the value to check
    Precondition: NONE (w can be any value)
    """
    return type(w) == Window


def is_valid_color(c):
    """
    Returns: True c is a valid turtle color; False otherwise

    Parameter c: the value to check
    Precondition: NONE (c can be any value)
    """
    return (type(c) == introcs.RGB or type(c) == introcs.HSV or
            (type(c) == str
                and (introcs.is_tkcolor(c) or introcs.is_webcolor(c))))


def is_valid_speed(sp):
    """
    Returns: True if sp is an int in range 0..10; False otherwise.

    Parameter sp: the value to check
    Precondition: NONE (sp can be any value)
    """
    return (type(sp) == int and 0 <= sp and sp <= 10)


def is_valid_length(side):
    """
    Returns: True if side is a number >= 0; False otherwise.

    Parameter side: the value to check
    Precondition: NONE (side can be any value)
    """
    return (is_number(side) and 0 <= side)


def is_valid_iteration(n):
    """
    Returns: True if n is an int >= 1; False otherwise.

    Parameter n: the value to check
    Precondition: NONE (n can be any value)
    """
    return (type(n) == int and 1 <= n)


def is_valid_depth(d):
    """
    Returns: True if d is an int >= 0; False otherwise.

    Parameter d: the value to check
    Precondition: NONE (d can be any value)
    """
    return (type(d) == int and d >= 0)


def is_valid_turtlemode(t):
    """
    Returns: True t is a Turtle with drawmode True; False otherwise.

    Parameter t: the value to check
    Precondition: NONE (t can be any value)
    """
    return (type(t) == Turtle and t.drawmode)


def is_valid_penmode(p):
    """
    Returns: True t is a Pen with solid False; False otherwise.

    Parameter p: the value to check
    Precondition: NONE (p can be any value)
    """
    return (type(p) == Pen and not p.solid)


def report_error(message, value):
    """
    Returns: An error message about the given value.

    This is a function for constructing error messages to be used in assert
    statements. We find that students often introduce bugs into their assert
    statement messages, and do not find them because they are in the habit of
    not writing tests that violate preconditions.

    The purpose of this function is to give you an easy way of making error
    messages without having to worry about introducing such bugs. Look at
    the function draw_two_lines for the proper way to use it.

    Parameter message: The error message to display
    Precondition: message is a string

    Parameter value: The value that caused the error
    Precondition: NONE (value can be anything)
    """
    return message+': '+repr(value)


#################### DEMO: Two lines ####################
def draw_two_lines(w, sp):
    """
    Draws two lines on to window w.

    This function clears w of any previous drawings. Then, in the middle of
    the window w, this function draws a green line 100 pixels to the east,
    and then a blue line 200 pixels to the north. It uses a new turtle that
    moves at speed sp, 0 <= sp <= 10, with 1 being slowest and 10 fastest
    (and 0 being "instant").

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter w: The window to draw upon.
    Precondition: w is a introcs Window object.

    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions to ensure valid inputs
    assert is_window(w), report_error('w is not a valid window', w)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)

    # Clear the window to prepare for new drawings
    w.clear()

    # Create a turtle and set its speed, then draw the lines
    t = Turtle(w)
    t.speed = sp
    t.color = 'green'  # Set color for the first line
    t.forward(100)  # Draw a green line 100 pixels in the current direction
    t.left(90)  # Turn the turtle 90 degrees to the left
    t.color = 'blue'  # Set color for the second line
    t.forward(200)  # Draw a blue line 200 pixels to the north
    t.flush()  # Ensure drawing is visible, especially if speed is 0


#################### TASK 1: Triangle ####################
def draw_triangle(t, s, c):
    """
    Draws an equilateral triangle of side s and color c at current position.

    The direction of the triangle depends on the current facing of the turtle.
    If the turtle is facing west, the triangle points up and the turtle starts
    and ends at the east end of the base line.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)

    Parameter c: The triangle color
    Precondition: c is a valid turtle color (see the helper function above)
    """
    # Assert the preconditions to ensure the turtle, side length, and color are valid
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)
    assert is_valid_color(c), report_error('Invalid color', c)

    # Save the current color and speed for restoration later
    col = t.color
    t.color = c  # Set the turtle's color for the triangle
    spd = t.speed

    # Draw the equilateral triangle
    for i in range(3):
        t.forward(s)  # Move forward by the side length
        t.right(120)  # Turn the turtle 120 degrees to form the triangle

    # Restore the turtle's original color and speed
    t.color = col
    t.speed = spd
    t.flush()  # Ensure drawing is visible, especially if speed is 0


#################### TASK 2: Hexagon ####################
def draw_hex(t, s):
    """
    Draws six triangles using the color 'cyan' to make a hexagon.

    The triangles are equilateral triangles, using draw_triangle as a helper.
    The drawing starts at the turtle's current position and heading. The
    middle of the hexagon is the turtle's starting position.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    """
    # Assert the preconditions to ensure the turtle and side length are valid
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)

    # Save the current color and speed for restoration later
    col = t.color
    t.color = 'cyan'  # Set the color for the hexagon
    spd = t.speed

    # Draw six triangles to form a hexagon
    for j in range(6):
        draw_triangle(t, s, 'cyan')  # Draw each triangle
        t.left(60)  # Turn the turtle 60 degrees to make the next triangle

    # Restore the turtle's original color and speed
    t.color = col
    t.speed = spd
    t.flush()  # Ensure drawing is visible, especially if speed is 0


#################### TASK 3: Circle ####################
def draw_circle(t, r):
    """
    Draws a circle of radius r.

    The circle is drawn using the standard turtle method of approximating a
    circle by drawing many small steps. The turtle starts at the bottom of
    the circle and moves upwards (i.e. heading 90 degrees). After drawing
    the circle, the turtle's attributes (position, heading, color, and
    drawmode) are the same as when the function started.

    REMEMBER: You need to flush the turtle if the speed is 0.

    This procedure asserts all preconditions.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.

    Parameter r: The radius of the circle
    Precondition: r is a valid radius (number >= 0)
    """
    # Assert the preconditions to ensure the turtle and radius are valid
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(r), report_error('Invalid radius', r)

    # Save the current color and speed for restoration later
    col = t.color
    t.color = 'red'  # Set the color for the circle
    spd = t.speed

    # Draw the circle by approximating it with many small steps
    circumference = 2 * math.pi * r  # Calculate the circumference
    steps = int(circumference / 10)  # Decide how many small steps to take
    step_length = circumference / steps  # Length of each step
    angle = 360 / steps  # Angle to turn after each step

    for i in range(steps):
        t.forward(step_length)  # Move forward by one small step
        t.left(angle)  # Turn the turtle to form the next step of the circle

    # Restore the turtle's original color and speed
    t.color = col
    t.speed = spd
    t.flush()  # Ensure drawing is visible, especially if speed is 0


#################### TASK 2: Hexagon ####################
def draw_hex(t, s):
    """
    Draws six equilateral triangles using the color 'cyan' to create a hexagon.

    The function uses a helper function, draw_triangle, to draw each of the six
    triangles that make up the hexagon. Each triangle is equilateral, and the
    turtle starts at the center of the hexagon. The turtle rotates 60 degrees after
    each triangle to form the hexagonal shape.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES REMAIN UNCHANGED:
    position (x and y, within rounding errors), heading, color, and drawmode.
    If any of these attributes are modified during execution, they are restored to their
    original values.

    REMINDER: The turtle must be flushed if the speed is set to 0.

    Preconditions:
    - t: The turtle must be in drawmode (True).
    - s: The side length must be a valid number (non-negative).

    Parameters:
    t (Turtle): The drawing Turtle.
    s (float or int): The side length of each triangle forming the hexagon.
    """
    # Assert the preconditions to ensure proper function behavior
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)

    # Store the turtle's current color and speed to restore later
    col = t.color
    t.color = 'cyan'  # Set color to cyan for the hexagon drawing
    spd = t.speed  # Store the current speed of the turtle

    # Draw six equilateral triangles to form the hexagon
    for j in range(6):
        draw_triangle(t, s, 'cyan')  # Draw one triangle
        t.left(60)  # Rotate the turtle by 60 degrees for the next triangle

    # Restore the turtle's original attributes
    t.color = col
    t.speed = spd
    t.flush()  # Ensure the drawing is rendered if speed is 0

#################### TASK 3A: Spirals ####################
def draw_spiral(w, side, ang, n, sp):
    """
    Draws a spiral by creating a new turtle and invoking the helper function to draw the spiral.

    This function starts by clearing the window and creating a new turtle. The turtle is positioned
    at the center of the canvas and faces south. It then calls the helper function, draw_spiral_helper,
    to draw the spiral. After the drawing is complete, the turtle is hidden.

    REMINDER: The turtle must be flushed if the speed is set to 0.

    Preconditions:
    - w: A valid introcs Window object where the drawing will occur.
    - side: A valid side length for the spiral.
    - ang: A valid angle to turn after each side of the spiral.
    - n: The number of edges of the spiral (must be a positive integer).
    - sp: A valid turtle speed.

    Parameters:
    w (Window): The window object where the spiral will be drawn.
    side (float or int): The length of each side of the spiral.
    ang (float or int): The angle to rotate after each side.
    n (int): The number of sides (iterations) in the spiral.
    sp (int): The speed of the turtle.
    """
    # Assert the preconditions to ensure proper function behavior
    assert is_window(w), report_error('w is not a valid window', w)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    assert is_number(ang), report_error('ang is not a valid angle', ang)

    # Clear the window and create a new turtle
    w.clear()
    t = Turtle(w)
    t.heading = 270  # Position the turtle to face south
    draw_spiral_helper(t, side, ang, n, sp)  # Draw the spiral using the helper function
    t.visible = False  # Hide the turtle after drawing is complete

    # Flush the turtle if the speed is set to 0
    if sp == 0:
        t.flush()

def draw_spiral_helper(t, side, ang, n, sp):
    """
    Draws a spiral consisting of n lines, each with increasing length.

    Each line is drawn with the specified side length, and after each line,
    the turtle turns by the given angle. The length of each line increases
    incrementally (Line 0 is `side`, Line 1 is `2*side`, and so on). The colors
    of the lines alternate between blue, magenta, and red, in that order, starting
    with blue for the first line.

    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and heading
    of the turtle may differ.

    Preconditions:
    - t: The drawing Turtle must be in drawmode (True).
    - side: The side length of the spiral, must be a valid number (non-negative).
    - ang: The angle to turn after each line, must be a valid number.
    - n: The number of sides (iterations), must be a positive integer.
    - sp: The speed of the turtle.

    Parameters:
    t (Turtle): The drawing Turtle.
    side (float or int): The length of the first spiral side.
    ang (float or int): The angle to turn after each side.
    n (int): The number of sides (iterations) in the spiral.
    sp (int): The turtle speed.
    """
    # Assert the preconditions to ensure proper function behavior
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    assert is_number(ang), report_error('ang is not a valid angle', ang)

    # Store the turtle's initial color and speed to restore after drawing
    savedColor = t.color
    savedSpeed = t.speed
    col = ['blue', 'magenta', 'red']  # Color sequence for the lines
    myIndex = 0  # Index to track the current color

    # Draw each line of the spiral
    for i in range(n):
        t.color = col[myIndex]  # Set the color for the current line
        myIndex = (myIndex + 1) % 3  # Move to the next color in the sequence

        # Draw the line with increasing length
        t.forward((i + 1) * side)
        t.left(ang)  # Turn by the specified angle after each line

    # Restore the turtle's original color and speed
    t.color = savedColor
    t.speed = savedSpeed


#################### TASK 3B: Polygons ####################

def multi_polygons(w, side, k, n, sp):
    """
    Draws k n-sided polygons of a given side length using a helper function.

    This function performs the following:
    1. Clears the window to prepare for drawing.
    2. Initializes a turtle at the center of the window facing north (heading = 90).
    3. Calls multi_polygons_helper to draw the polygons.
    4. Sets the turtle to invisible after the drawing is complete.

    Additionally, if the turtle speed is set to 0, it forces the turtle to flush the drawing for display.

    Preconditions:
    - w is a valid introcs Window object.
    - side is a valid positive number (>= 0).
    - k is an integer >= 1 (the number of polygons to draw).
    - n is an integer >= 3 (the number of sides of each polygon).
    - sp is a valid turtle speed.

    Parameters:
    - w: The window on which the polygons will be drawn.
    - side: The length of each side of the polygon.
    - k: The number of polygons to draw.
    - n: The number of sides for each polygon.
    - sp: The speed at which the turtle moves.

    Returns:
    - None
    """
    # Ensure all preconditions are met before proceeding
    assert is_window(w), report_error('w is not a valid window', w)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    assert is_valid_iteration(k), report_error('k is not a valid number of polygons', k)
    assert type(n) == int, report_error('n is not an int', n)
    assert n >= 3, report_error('n is not a valid number of sides', n)

    # Clear the window to prepare for the new drawing
    w.clear()

    # Initialize the turtle object at the center, facing north
    t = Turtle(w)
    t.heading = 90

    # Call the helper function to draw the polygons
    multi_polygons_helper(t, side, k, n, sp)

    # Hide the turtle once drawing is complete
    t.visible = False

    # If the turtle speed is 0, flush the drawing to ensure it's displayed
    if sp == 0:
        t.flush()


def multi_polygons_helper(t, side, k, n, sp):
    """
    Helper function to draw k n-sided polygons, alternating between blue and orange.

    The turtles alternate colors (blue, then orange) for each polygon and rotate by
    360/k degrees after each polygon. The drawing starts from the same position for each polygon.

    The function ensures that after drawing, all turtle attributes (color, speed, etc.)
    are restored to their original state.

    Preconditions:
    - t is a valid Turtle object in drawmode.
    - side is a valid length for the polygon sides.
    - k is an integer >= 1.
    - n is an integer >= 3 (number of sides for each polygon).
    - sp is a valid turtle speed.

    Parameters:
    - t: The turtle used to draw the polygons.
    - side: The length of each side of the polygon.
    - k: The number of polygons to draw.
    - n: The number of sides for each polygon.
    - sp: The speed at which the turtle moves.

    Returns:
    - None
    """
    # Ensure all preconditions are met before proceeding
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    assert is_valid_iteration(k), report_error('k is not a valid number of polygons', k)
    assert type(n) == int, report_error('n is not an int', n)
    assert n >= 3, report_error('n is not a valid number of sides', n)

    # Save the turtle's original color and speed settings to restore them later
    savedColor = t.color
    savedSpeed = t.speed

    # Define alternating colors for the polygons
    col = ['blue', 'orange']

    # Set the initial color to blue
    t.color = col[0]

    # Calculate the angle for rotation after each polygon
    ang = 360.0 / k

    # Draw the k polygons
    for i in range(k):
        # Alternate the colors between blue and orange
        t.color = col[(i - 1) % 2]

        # Draw a polygon using the helper function
        draw_polygon(t, side, n)

        # Turn the turtle left by the calculated angle
        t.left(ang)

    # Restore the turtle's original speed and color settings
    t.speed = savedSpeed
    t.color = savedColor


# DO NOT MODIFY
def draw_polygon(t, side, n):
    """
    Draws an n-sided polygon with the given side length.

    This function ensures that the turtle's position, heading, and other attributes
    remain unchanged after drawing the polygon.

    Preconditions:
    - t is a valid Turtle object in drawmode.
    - side is a valid length for the polygon sides.
    - n is an integer >= 1 (number of sides for the polygon).

    Parameters:
    - t: The turtle used to draw the polygon.
    - side: The length of each side of the polygon.
    - n: The number of sides for the polygon.

    Returns:
    - None
    """
    # Ensure all preconditions are met before proceeding
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert type(n) == int and n >= 1, report_error('n is an invalid # of poly sides', n)

    # Calculate the exterior angle between adjacent sides
    ang = 360.0 / n

    # Loop to draw the polygon
    for _ in range(n):
        # Move the turtle forward by the side length
        t.forward(side)

        # Turn the turtle left by the calculated angle to form the polygon
        t.left(ang)


def draw_diamond(t, length, width):
    """
    Draws a diamond shape with a given major axis length (length) and minor axis width.

    The major axis is drawn along the current heading of the turtle, and the minor axis
    is perpendicular to the heading.

    Preconditions:
    - t is a valid Turtle object in drawmode.
    - length is a valid positive number for the major axis (>= 0).
    - width is a valid positive number for the minor axis (>= 0).

    Parameters:
    - t: The turtle used to draw the diamond.
    - length: The size of the major axis.
    - width: The size of the minor axis.

    Returns:
    - None
    """
    # Ensure all preconditions are met before proceeding
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(length), report_error('length is not a valid length', length)
    assert is_valid_length(width), report_error('width is not a valid length', width)

    # Calculate the next position to go to, based on the major axis and minor axis
    angle1 = t.heading * math.pi / 180.0
    x2 = t.x + math.cos(angle1) * length / 2
    y2 = t.y + math.sin(angle1) * length / 2
    x2 -= math.sin(angle1) * width / 2
    y2 += math.cos(angle1) * width / 2

    # Calculate the angle and edge length for the diamond
    angle2 = math.atan2(y2 - t.y, x2 - t.x) * 180.0 / math.pi
    angle3 = angle2 - t.heading
    edgesz = math.sqrt((x2 - t.x) ** 2 + (y2 - t.y) ** 2)

    # Draw the diamond by moving the turtle forward and turning as necessary
    t.right(angle3)
    t.forward(edgesz)
    t.left(2 * angle3)
    t.forward(edgesz)
    t.right(2 * angle3)
    t.backward(edgesz)
    t.left(2 * angle3)
    t.backward(edgesz)
    t.right(angle3)


#################### TASK 4A: Sierpinski Triangle ####################
def triangle(w, side, d, sp):
    """
    Draws a Sierpinski triangle with the given side length and depth d.

    This function initializes the graphics window, creates a new pen to draw,
    and calls the recursive function triangle_helper(p, 0, 0, side, d) to
    generate the Sierpinski triangle. The drawing process is performed
    by calling the helper function for recursion. After the drawing is
    complete, the pen is hidden.

    REMEMBER: The pen must be flushed if the speed is set to 0.

    Parameters:
    w (Window): The window to draw upon.
        - Precondition: w is a Window object.
    side (float): The side length of the triangle.
        - Precondition: side is a valid side length (number >= 0).
    d (int): The recursive depth of the triangle.
        - Precondition: d is a valid depth (int >= 0).
    sp (int): The drawing speed (0 is the slowest, 10 is the fastest).
        - Precondition: sp is a valid turtle/pen speed.
    """
    # Ensure all preconditions are met before starting the drawing
    assert is_window(w), report_error('w is not a valid window', w)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    assert is_valid_depth(d), report_error('d is not a valid depth', d)

    # Clear the window and set up the drawing pen
    w.clear()
    p = Pen(w, (0, 0), 'black', 'magenta', 10)  # Create a Pen object with specified attributes
    p.visible = True  # Make the pen visible
    p.solid = False  # Set the pen to not draw solid shapes
    triangle_helper(p, 0, 0, side, d)  # Call the helper function to draw the triangle

    # If speed is 0, flush the drawing buffer to ensure visibility
    if sp == 0:
        p.flush()

    p.visible = False  # Hide the pen after the drawing is complete


def triangle_helper(p, x, y, side, d):
    """
    Recursively draws a Sierpinski triangle with the given side length and depth d,
    centered at (x, y).

    The triangle is drawn recursively by calling triangle_helper for smaller triangles.
    Once the recursion reaches depth 0, the triangle is filled using the fill_triangle function.

    Parameters:
    p (Pen): The graphics pen used for drawing.
        - Precondition: p is a Pen with fill attribute False.
    x (float): The x-coordinate of the triangle center.
        - Precondition: x is a number.
    y (float): The y-coordinate of the triangle center.
        - Precondition: y is a number.
    side (float): The side length of the triangle.
        - Precondition: side is a valid side length (number >= 0).
    d (int): The recursive depth of the triangle.
        - Precondition: d is a valid depth (int >= 0).
    """
    # Ensure that all input parameters are valid
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid number', x)
    assert is_number(y), report_error('y is not a valid number', y)
    assert is_valid_depth(d), report_error('d is not a valid depth', d)
    assert is_valid_length(side), report_error('side is not a valid length', side)

    # If recursion depth is 0, draw and fill the triangle
    p.visible = True
    if d == 0:
        fill_triangle(p, x, y, side)  # Call the function to fill the triangle
    else:
        # Calculate side length for smaller triangles and positions
        s = side / 2
        s2 = side / 4
        d_new = d - 1
        h = (math.sqrt(3) / 2) * side  # Height of the triangle
        height = 0.5 * h  # Half the height for positioning

        # Recursively draw three smaller triangles to form the Sierpinski pattern
        triangle_helper(p, x, y, s, d_new)
        triangle_helper(p, x + s, y, s, d_new)
        triangle_helper(p, x + s2, y + height, s, d_new)


def fill_triangle(p, x, y, side):
    """
    Fills an equilateral triangle of side length with the center at (x, y).

    The triangle is drawn with the top pointing up, and the drawing pen
    will fill it solidly.

    Parameters:
    p (Pen): The graphics pen used for drawing.
        - Precondition: p is a Pen with fill attribute False.
    x (float): The x-coordinate of the triangle center.
        - Precondition: x is a number.
    y (float): The y-coordinate of the triangle center.
        - Precondition: y is a number.
    side (float): The side length of the triangle.
        - Precondition: side is a valid side length (number >= 0).
    """
    # Validate inputs before drawing the filled triangle
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position', x)
    assert is_number(y), report_error('y is not a valid position', y)
    assert is_valid_length(side), report_error('side is not a valid length', side)

    # Calculate the height of the triangle
    h = side * math.sqrt(0.75)

    # Move the pen to the starting position and draw the filled triangle
    p.move(x - side / 2, y - h / 2)
    p.solid = True  # Set the pen to fill solid shapes
    p.drawLine(side, 0)  # Draw the base of the triangle
    p.drawLine(-side / 2.0, h)  # Draw the left side
    p.drawLine(-side / 2.0, -h)  # Draw the right side
    p.solid = False  # Reset the pen to non-solid mode


def fill_rect(p, x, y, side, hght):
    """
    Fills a rectangle of width 'side' and height 'hght' with center at (x, y).

    Parameters:
    p (Pen): The graphics pen used for drawing.
        - Precondition: p is a Pen with solid attribute False.
    x (float): The x-coordinate of the rectangle center.
        - Precondition: x is a number.
    y (float): The y-coordinate of the rectangle center.
        - Precondition: y is a number.
    side (float): The width of the rectangle.
        - Precondition: side is a valid side length (number >= 0).
    hght (float): The height of the rectangle.
        - Precondition: hght is a valid side length (number >= 0).
    """
    # Validate inputs before drawing the filled rectangle
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position', x)
    assert is_number(y), report_error('y is not a valid position', y)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_length(hght), report_error('hght is not a valid length', hght)

    # Move the pen to the starting position and draw the filled rectangle
    p.move(x - side / 2.0, y - hght / 2.0)
    p.solid = True
    p.drawLine(0, hght)  # Draw the left vertical side
    p.drawLine(side, 0)  # Draw the top horizontal side
    p.drawLine(0, -hght)  # Draw the right vertical side
    p.drawLine(-side, 0)  # Draw the bottom horizontal side
    p.solid = False  # Reset the pen to non-solid mode
    p.move(x - side / 2.0, y - hght / 2.0)  # Return the pen to the starting position


#################### TASK 5: Minkowski Island ####################
def island(w, side, d, sp):
    """
    Draws a Minkowski island with the given side length and depth d.

    This function clears the window and makes a new Turtle t. The turtle starts
    at the lower right corner of the square centered at (0, 0) with side length
    'side'. It draws the island recursively by calling the function island_edge(t, side, d)
    four times, rotating the turtle left after each call to form a square.

    REMEMBER: You need to flush the turtle if the speed is 0.

    Parameters:
    w (Window): The window to draw upon.
        - Precondition: w is a Window object.
    side (float): The side length of the island.
        - Precondition: side is a valid side length (number >= 0).
    d (int): The recursive depth of the island.
        - Precondition: d is a valid depth (int >= 0).
    sp (int): The drawing speed (0 is the slowest, 10 is the fastest).
        - Precondition: sp is a valid turtle/pen speed.
    """
    # Ensure all preconditions are met before starting the drawing
    assert is_window(w), report_error('w is not a valid window', w)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed', sp)
    assert is_valid_depth(d), report_error('d is not a valid depth', d)

    # Clear the window and create a turtle for drawing
    w.clear()
    t = Pen(w, (0, 0), 'black', 'green', 5)
    t.visible = True  # Set the pen to visible

    # Draw the island by recursively drawing the square shape at different depths
    island_edge(t, side, d)  # Start drawing the island

    # Flush the drawing buffer if speed is set to 0
    if sp == 0:
        t.flush()

    t.visible = False  # Hide the pen after drawing the island
    

def island_edge(t, side, d):
    """
    Recursively draws a single Minkowski edge with depth d at the current position and angle.

    The edge is drawn using the current turtle's color. The turtle's heading and angle
    are changed as needed during the recursive process. The turtle's color, speed,
    and visibility are preserved throughout.

    Parameters:
    t (Turtle): The drawing turtle.
    side (float): The length of each Minkowski side.
    d (int): The recursive depth of the edge.

    Preconditions:
    - t is a Turtle object.
    - side is a valid side length (number >= 0).
    - d is a valid depth (integer >= 0).
    """
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_number(side), report_error('side is not a valid number', side)
    assert is_valid_depth(d), report_error('d is not a valid depth', d)

    if d == 0:
        t.forward(side)
    else:
        side = side / 4
        island_edge(t, side, d - 1)  # Recursively draw the first part
        t.right(90)  # Turn right by 90 degrees
        island_edge(t, side, d - 1)  # Recursively draw the second part
        t.left(90)  # Turn left by 90 degrees
        island_edge(t, side, d - 1)  # Recursively draw the third part
        t.left(90)  # Turn left by 90 degrees
        island_edge(t, side, d - 1)  # Recursively draw the fourth part
        island_edge(t, side, d - 1)  # Recursively draw another part
        t.right(90)  # Turn right by 90 degrees
        island_edge(t, side, d - 1)  # Recursively draw the sixth part
        t.right(90)  # Turn right by 90 degrees
        island_edge(t, side, d - 1)  # Recursively draw the seventh part
        t.left(90)  # Turn left by 90 degrees
        island_edge(t, side, d - 1)  # Recursively draw the eighth part
