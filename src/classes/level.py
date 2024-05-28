from dataclasses import dataclass
from typing import List, Optional

from src.classes.food import Food
from src.classes.obstacle import Obstacle
from src.classes.snake import Snake


@dataclass
class Level:
    snake: Snake
    food: Food
    obstacles: Optional[List[Obstacle]]
    food_objective: int
