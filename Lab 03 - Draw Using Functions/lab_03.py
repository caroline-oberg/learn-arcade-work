import arcade

# this is a comment the computer will ignore
# this is a comment
def draw_grass():
    """Draw the grass"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.AMAZON)
def draw_flower(x,y):
    """Draw a flower"""
    arcade.draw_rectangle_filled(100 + x - 100, 120 + y - 150, 20, 40, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(100 + x - 100, 150 + y - 150, 20, arcade.csscolor.LAVENDER)
    arcade.draw_circle_filled(100 + x - 100, 150 + y - 150, 10, arcade.csscolor.YELLOW)

def draw_cow(x, y):
    """Draw the cow"""
    # Cow body
    arcade.draw_lrtb_rectangle_filled(75 + x - 200, 300 + x - 200, 350 + y - 300, 250 + y - 300, arcade.csscolor.WHITE)
    # Cow legs
    arcade.draw_lrtb_rectangle_filled(75 + x - 200, 100 + x - 200, 300 + y - 300, 200 + y - 300, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(110 + x - 200, 135 + x - 200, 300 + y - 300, 200 + y - 300, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(235 + x - 200, 260 + x - 200, 300 + y - 300, 200 + y - 300, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(275 + x - 200, 300 + x - 200, 300 + y - 300, 200 + y - 300, arcade.csscolor.WHITE)
    #Cow hooves
    arcade.draw_lrtb_rectangle_filled(75 + x - 200, 100 + x - 200, 225 + y - 300, 200 + y - 300, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(110 + x - 200, 135 + x - 200, 225 + y - 300, 200 + y - 300, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(235 + x - 200, 260 + x - 200, 225 + y - 300, 200 + y - 300, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(275 + x - 200, 300 + x - 200, 225 + y - 300, 200 + y - 300, arcade.csscolor.BLACK)
    # Cow tail
    arcade.draw_lrtb_rectangle_filled(50 + x - 200, 75 + x - 200, 340 + y - 300, 330 + y - 300, arcade.csscolor.WHITE)
    # Cow Head
    arcade.draw_ellipse_filled(340 + x - 200, 350 + y - 300, 100, 80, arcade.csscolor.WHITE)
    # EYES
    arcade.draw_ellipse_filled(380 + x - 200, 370 + y - 300, 20, 20, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(360 + x - 200, 370 + y - 300, 20, 20, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(380 + x - 200, 370 + y - 300, 15, 15, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(360 + x - 200, 370 + y - 300, 15, 15, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(380 + x - 200, 370 + y - 300, 5, 5, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(360 + x - 200, 370 + y - 300, 5, 5, arcade.csscolor.BLACK)
    # Mouth
    arcade.draw_ellipse_filled(380 + x - 200, 330 + y - 300, 20, 20, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(380 + x - 200, 330 + y - 300, 18, 18, arcade.csscolor.PALE_VIOLET_RED)
    # Cow Spots
    arcade.draw_ellipse_filled(150 + x - 200, 300 + y - 300, 40, 30, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(250 + x - 200, 300 + y - 300, 40, 30, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(260 + x - 200, 330 + y - 300, 40, 30, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(200 + x - 200, 275 + y - 300, 40, 30, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(200 + x - 200, 330 + y - 300, 38, 40, arcade.csscolor.BLACK)
    arcade.draw_ellipse_filled(140 + x - 200, 335 + y - 300, 40, 30, arcade.csscolor.BLACK)

def draw_tree(x, y):
    """Draw a tree"""
    arcade.draw_rectangle_filled(790 + x - 770, 400 + y - 500, 70, 150, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(790 + x - 770, 500 + y - 500, 100, arcade.csscolor.DARK_GREEN)

def main():
    arcade.open_window(800, 600, "Drawing Example")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    arcade.start_render()

    draw_grass()

    # Draw the Pond
    arcade.draw_ellipse_filled(600, 150, 400, 100, arcade.csscolor.INDIGO)

    # Draw the flower
    draw_flower(100, 150)
    draw_flower(200, 150)

    # Draw the tree
    draw_tree(770,350)
    draw_tree(300, 350)

    # Draw the cow
    draw_cow(100, 300)
    draw_cow(500, 300)
    #Sun
    arcade.draw_circle_filled(20, 600, 150, arcade.csscolor.YELLOW)


    arcade.finish_render()
    # Keep the window up until someone closes it.
    arcade.run()

main()