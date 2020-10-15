# Artwork from http://kenney.nl

import random
import arcade
import os
import typing

# --- Constants ---
import self as self

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Lab"


class Coin(arcade.Sprite):

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


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.all_sprites_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player_sprite = arcade.SpriteList()
        self.good_sprite = arcade.SpriteList()
        self.bad_sprite = arcade.SpriteList()

        # Score
        self.score = 0

        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character_femaleAdventurer_talk.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)


        for i in range(100):

            # Coin image from kenney.nl
            coin = Coin("explosion1.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)
        for i in range(100):

            coin = Coin("explosion5.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(4,-3)
            coin.change_y = random.randrange(4,-3)

    def on_draw(self):

        arcade.start_render()
        self.all_sprites_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):

        self.all_sprites_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
        for good_sprite in good_hit_list:
            self.good_sprite = arcade.Sprite("impactGlass_light_002.ogg")
            self.good_sprite = arcade.Sprite("explosion1.png", SPRITE_SCALING_COIN)
        for bad_sprite in bad_hit_list:
            self.bad_sprite = arcade.Sprite("impactGlass_heavy_002.ogg")
            self.bad_sprite = arcade.Sprite("explosion5.png", SPRITE_SCALING_COIN)

        coin.remove_from_sprite_lists()
        self.score += 1

    if self.good_sprite = 0
        print("Game Over.")


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()