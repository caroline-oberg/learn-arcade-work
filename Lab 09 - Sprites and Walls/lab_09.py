#Artwork from http://kenney.nl

import random
import arcade
import os

SPRITE_SCALING = 1.8
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

VIEWPORT_MARGIN = 40

NUMBER_OF_COINS = 50

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        self.coin_list = None
        self.wall_list = None
        self.score = 0

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.good_sound = arcade.load_sound("impactGlass_light_002.ogg")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("character_femalePerson_interact.png", 0.4)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        wall = arcade.Sprite("barricadeWood.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # -- Set up several columns of walls
        for x in range(173, 650, 64):
            wall = arcade.Sprite("sandbagBrown_open.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("crateMetal.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(200, 1650, 210):
            for y in range(0, 1000, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("crateWood.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for i in range (NUMBER_OF_COINS):

            #coin image from kenney.nl
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.coin_list) == 0:
            output = "Game Over"
            arcade.draw_text(output, 300, 300, arcade.color.WHITE, 40)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.good_sound.play()



def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()