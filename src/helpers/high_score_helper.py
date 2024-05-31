from typing import Tuple
import random

from src import GRID_HEIGHT, GRID_WIDTH
from src.classes.food import Food
from src.classes.map_position import MapPosition
from src.classes.snake import Snake


class HighScoreHelper:
    """
    Class responsible for high score mode
    * initializing snake and position
    * keep tract of score
    """
    def __init__(self) -> None:
        self.high_score = 0

    def get_high_score(self) -> int:
        """
        Get the high score
        :return the score
        """
        return self.high_score
    
    def set_high_score(self, high_score: int) -> None:
        """
        Set the high score
        :param high_score: int to assign
        """
        self.high_score = high_score
    
    def initialize_snake_food_positions_and_score(self) -> Tuple[Snake, Food, int]:
        food_position = MapPosition(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food = Food(food_position, (GRID_WIDTH, GRID_HEIGHT))
        snake_position = MapPosition(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        snake = Snake(snake_position, food)
        return snake, food, 0
