# Artwork from http://kenney.nl

import random
import arcade
import os

# --- Constants ---

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Lab"


class GoodSprite(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class BadSprite(arcade.Sprite):

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.good_sprite_list = None
        self.bad_sprite_list = None
        self.player_sprite_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

        self.good_sound = arcade.load_sound("impactGlass_light_002.ogg")
        self.bad_sound = arcade.load_sound("impactGlass_heavy_002.ogg")


    def setup(self):
        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character_femaleAdventurer_talk.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)


        for i in range(100):

            # Good Sprite image from kenney.nl
            good_sprite = GoodSprite("explosion1.png", SPRITE_SCALING_COIN)

            good_sprite.center_x = random.randrange(SCREEN_WIDTH)
            good_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            good_sprite.change_x = random.randrange(-3, 4)
            good_sprite.change_y = random.randrange(-3, 4)

            self.good_sprite_list.append(good_sprite)

        for i in range(100):

            bad_sprite = BadSprite("explosion5.png", SPRITE_SCALING_COIN)

            bad_sprite.center_x = random.randrange(SCREEN_WIDTH)
            bad_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_sprite.change_x = random.randrange(-3, 4)
            bad_sprite.change_y = random.randrange(-3, 4)

            self.bad_sprite_list.append(bad_sprite)

    def on_draw(self):

        arcade.start_render()
        self.good_sprite_list.draw()
        self.bad_sprite_list.draw()
        self.player_sprite_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.good_sprite_list) == 0:
            output = "Game Over"
            arcade.draw_text(output, 300, 300, arcade.color.WHITE, 40)

    def on_mouse_motion(self, x, y, dx, dy):

        if len(self.good_sprite_list) != 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):

        if len(self.good_sprite_list) != 0:
            self.good_sprite_list.update()
            self.bad_sprite_list.update()


        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)

        for good_sprite in good_hit_list:
            good_sprite.remove_from_sprite_lists()
            self.score += 1
            self.good_sound.play()

        for bad_sprite in bad_hit_list:
            bad_sprite.remove_from_sprite_lists()
            self.score -= 1
            self.bad_sound.play()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()