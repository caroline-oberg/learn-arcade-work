import arcade

# this is a comment the computer will ignore
# this is a comment
arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.BABY_BLUE)
arcade.start_render()
# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.AMAZON)
# Draw the Pond
arcade.draw_ellipse_filled(600, 150, 400, 100, arcade.csscolor.INDIGO)
# Cow body
arcade.draw_lrtb_rectangle_filled(75, 300, 350, 250, arcade.csscolor.WHITE)
# Cow legs
arcade.draw_lrtb_rectangle_filled(75, 100, 300, 200, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(110, 135, 300, 200, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(235, 260, 300, 200, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(275, 300, 300, 200, arcade.csscolor.WHITE)
#Cow hooves
arcade.draw_lrtb_rectangle_filled(75, 100, 225, 200, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(110, 135, 225, 200, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(235, 260, 225, 200, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(275, 300, 225, 200, arcade.csscolor.BLACK)
# Cow tail
arcade.draw_lrtb_rectangle_filled(50, 75, 340, 330, arcade.csscolor.WHITE)
# Cow Head
arcade.draw_ellipse_filled(340, 350, 100, 80, arcade.csscolor.WHITE)
# EYES
arcade.draw_ellipse_filled(380, 370, 20, 20, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(360, 370, 20, 20, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(380, 370, 15, 15, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(360, 370, 15, 15, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(380, 370, 5, 5, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(360, 370, 5, 5, arcade.csscolor.BLACK)
# Mouth
arcade.draw_ellipse_filled(380, 330, 20, 20, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(380, 330, 18, 18, arcade.csscolor.PALE_VIOLET_RED)
# Cow Spots
arcade.draw_ellipse_filled(150, 300, 40, 30, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(250, 300, 40, 30, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(260, 330, 40, 30, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(200, 275, 40, 30, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(200, 330, 38, 40, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(140, 335, 40, 30, arcade.csscolor.BLACK)
#Sun
arcade.draw_circle_filled(20, 600, 150, arcade.csscolor.YELLOW)


arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()

