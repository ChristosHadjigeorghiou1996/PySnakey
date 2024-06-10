from typing import Tuple
import random

from pygame.draw import rect

from src.classes.map_position import MapPosition
from src import CELL_SIZE, RED, SCREEN

class Food:
    def __init__(self, position: MapPosition, grid_dimensions: Tuple[int, int, int, int]):
        self.position = position
        self.grid_dimensions = grid_dimensions

    def respawn(self):
        self.position = (MapPosition(random.randint(self.grid_dimensions[0], self.grid_dimensions[2] - 1),
                                     random.randint(self.grid_dimensions[1], self.grid_dimensions[3] - 1)))

    def draw(self):
        rect(SCREEN, RED, (self.position.x_pos * CELL_SIZE, self.position.y_pos * CELL_SIZE, CELL_SIZE, CELL_SIZE))
