import arcade

# this is a comment the computer will ignore
# this is a comment
arcade.open_window(800, 600, "My sample window")
arcade.set_background_color(arcade.color.LAVENDER_PURPLE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.GREEN)
arcade.finish_render()
arcade.run()

