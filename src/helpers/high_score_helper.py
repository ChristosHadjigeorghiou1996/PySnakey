from typing import List, Tuple
import json
import os
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
    def __init__(self, high_score_file_path: str) -> None:
        self.high_score_file_path = high_score_file_path
        self.high_scores = self.load_high_scores()

    def load_high_scores(self) -> List[int]:
        if os.path.isfile(self.high_score_file_path):
            with open(self.high_score_file_path, "r") as f:
                return json.load(f)
        return []
    
    def save_high_scores(self) -> None:
        with open(self.high_score_file_path, "w") as f:
            json.dump(self.high_scores, f)

    def add_high_score(self, high_score: int) -> None:
        self.high_scores.append(high_score)
        self.high_scores.sort(reverse=True)
        self.save_high_scores()

    def initialize_snake_food_positions_and_score(self) -> Tuple[Snake, Food]:
        food_position = MapPosition(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food = Food(food_position, (0, 0, GRID_WIDTH, GRID_HEIGHT))
        snake_position = MapPosition(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        snake = Snake(snake_position, food)
        return snake, food
