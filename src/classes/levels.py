from typing import List
import random

from src import GRID_HEIGHT, GRID_WIDTH
from src.classes.food import Food
from src.classes.level import Level
from src.classes.map_position import MapPosition
from src.classes.obstacle import Obstacle
from src.classes.snake import Snake


class Levels:
    def __init__(self) -> None:
        self.levels = None
        self._set_levels()

    def _set_levels(self) -> None:
        """
        Initialize the levels to use
        """
        self.levels = [self.level_1(), self.level_2()]

    def get_levels(self) -> List[Level]:
        """
        Get the initialized levels for the game
        :return list of levels
        """
        return self.levels

    def level_1(self) -> Level:
        """
        Level one has no restrictions,
        :return the level
        """
        food_position = MapPosition(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food = Food(food_position, (0, 0, GRID_WIDTH, GRID_HEIGHT))
        snake_position = MapPosition(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        snake = Snake(snake_position, food)
        food_to_consume_objective = 5
        return Level(snake, food, None, food_to_consume_objective)

    def level_2(self) -> Level:
        """
        Second level restricts moving across borders
        :return the level
        """
        min_x = 1
        min_y = 1
        max_x = GRID_WIDTH - 2
        max_y = GRID_HEIGHT - 2
        food_position = MapPosition(random.randint(min_x, max_x), random.randint(min_y, max_y))
        food = Food(food_position, (1, 1, max_x, max_y))
        snake_position = MapPosition(random.randint(min_x, max_x), random.randint(min_y, max_y))
        snake = Snake(snake_position, food)
        food_to_consume_objective = 10
        # Create obstacles surrounding the screen borders
        obstacles: List[Obstacle] = []
        for x in range(GRID_WIDTH):
            obstacles.append(Obstacle(MapPosition(x, 0)))
            obstacles.append(Obstacle(MapPosition(x, GRID_HEIGHT - 1)))
        for y in range(GRID_HEIGHT):
            obstacles.append(Obstacle(MapPosition(0, y)))
            obstacles.append(Obstacle(MapPosition(GRID_WIDTH - 1, y)))

        return Level(snake, food, obstacles, food_to_consume_objective)
