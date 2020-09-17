import arcade

# this is a comment the computer will ignore
# this is a comment
def draw_grass():
    """Draw the grass"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.AMAZON)
def draw_flower(x,y):
    """Draw a flower"""
    arcade.draw_rectangle_filled(100 + x, 120 + x, 20 + y, 40 + y, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(100 + x, 150 + y, 20, arcade.csscolor.LAVENDER)
    arcade.draw_circle_filled(100 + x, 150 + y, 10, arcade.csscolor.YELLOW)

def draw_cow(x, y):
    """Draw the cow"""
    # Cow body
    arcade.draw_lrtb_rectangle_filled(75 + x, 300 + x, 350 + y, 250 + y, arcade.csscolor.WHITE)
    # Cow legs
    arcade.draw_lrtb_rectangle_filled(75 + x, 100 + x, 300 + y, 200 + y, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(110 + x, 135 + x, 300 + y, 200 + y, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(235 + x, 260 + x, 300 + y, 200 + y, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(275 + x, 300 + x, 300 + y, 200 + y, arcade.csscolor.WHITE)
    #Cow hooves
    arcade.draw_lrtb_rectangle_filled(75 + x, 100 + x, 225 + y, 200 + y, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(110 + x, 135 + x, 225 + y, 200 + y, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(235 + x, 260 + x, 225 + y, 200 + y, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(275 + x, 300 + x, 225 + y, 200 + y, arcade.csscolor.BLACK)
    # Cow tail
    arcade.draw_lrtb_rectangle_filled(50 + x, 75 + x, 340 + y, 330 + y, arcade.csscolor.WHITE)
    # Cow Head
    arcade.draw_ellipse_filled(340 + x, 350 + x, 100 + y, 80 + y, arcade.csscolor.WHITE)
    # EYES
    arcade.draw_ellipse_filled(380 + x, 370 + x, 20 + y, 20 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(360 + x, 370 + x, 20 + y, 20 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(380 + x, 370 + x, 15 + y, 15 + y, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(360 + x, 370 + x, 15 + y, 15 + y, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(380 + x, 370 + x, 5 + y, 5 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(360 + x, 370 + x, 5 + y, 5 + y, arcade.csscolor.BLACK)
    # Mouth
    arcade.draw_ellipse_filled(380 + x, 330 + x, 20 + y, 20 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(380 + x, 330 + x, 18 + y, 18 + y, arcade.csscolor.PALE_VIOLET_RED)
    # Cow Spots
    arcade.draw_ellipse_filled(150 + x, 300 + x, 40 + y, 30 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(250 + x, 300 + x, 40 + y, 30 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(260 + x, 330 + x, 40 + y, 30 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(200 + x, 275 + x, 40 + y, 30 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(200 + x, 330 + x, 38 + y, 40 + y, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(140 + x, 335 + x, 40 + y, 30 + y, arcade.csscolor.BLACK)

def draw_tree(x, y):
    """Draw a tree"""
    arcade.draw_rectangle_filled(790 + x, 300 + x, 100 + y, 260 + y, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(770 + x, 500 + y, 100, arcade.csscolor.DARK_GREEN)

def main():
    arcade.open_window(800, 600, "Drawing Example")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    arcade.start_render()

    draw_grass()

    # Draw the Pond
    arcade.draw_ellipse_filled(600, 150, 400, 100, arcade.csscolor.INDIGO)

    # Draw the flower
    draw_flower(0,0)
    draw_flower(100,0)

    # Draw the cow
    draw_cow(0,0)
    draw_cow(400, 0)
    # Draw the tree
    draw_tree(0,0)
    draw_tree(400, 0)
    #Sun
    arcade.draw_circle_filled(20, 600, 150, arcade.csscolor.YELLOW)


    arcade.finish_render()
    # Keep the window up until someone closes it.
    arcade.run()

main()