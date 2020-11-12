import arcade

ROW_COUNT = 10
COLUMN_COUNT = 10

WIDTH = 20
HEIGHT = 20

MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid_shape_list = None
        self.create_shapes_from_grid()

    def create_shapes_from_grid(self):
        self.grid_shape_list = arcade.ShapeElementList()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                rectangle = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                self.grid_shape_list.append(rectangle)

    def on_draw(self):

        arcade.start_render()

        self.grid_shape_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):

        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        self.create_shapes_from_grid()

        running_total = 0

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 1:
                    running_total +=1

        print("Total of", running_total, "cells are selected.")

        for row in range(ROW_COUNT):
            continuous_count = 0
            running_total = 0
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 1:
                    running_total +=1
                    continuous_count +=1
                else:
                    if continuous_count >= 3:
                        print("There are", continuous_count, "blocks selected on", row)
                    continuous_count = 0

            print("Row", row, "has", running_total, "cells selected.")

            if continuous_count >= 3:
                print("There are", continuous_count, "blocks selected on", row)

        for column in range(COLUMN_COUNT):
            running_total = 0
            for row in range(ROW_COUNT):

                if self.grid[row][column] == 1:
                    running_total +=1

            print("Column", column, "has", running_total, "cells selected.")

def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()