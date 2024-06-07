import pytest
from unittest.mock import Mock
import pygame
from src.classes.snake import Snake
from src.classes.map_position import MapPosition
from src.classes.food import Food

@pytest.fixture
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def snake() -> Snake:
    initial_position = MapPosition(5, 5)
    food = Mock(spec=Food)
    food.position = MapPosition(10, 10)
    return Snake(initial_position, food)

def test_initialization(snake) -> None:
    assert len(snake.body) == 1
    assert snake.body[0] == MapPosition(5, 5)
    assert snake.food_consumed == 0
    assert snake.direction == (1, 0)

def test_move(snake: Snake) -> None:
    snake.move()
    assert snake.body[0] == MapPosition(6, 5)
    assert len(snake.body) == 1

def test_change_direction(snake: Snake) -> None:
    snake.change_direction((1, 0))
    assert snake.direction == (1, 0)

def test_grow(snake: Snake) -> None:
    snake.grow()
    assert len(snake.body) == 2
    assert snake.body[1] == snake.body[0]

def test_food_consumption(snake: Snake) -> None:
    snake.food.position = MapPosition(snake.body[0].x_pos + 1, snake.body[0].y_pos)
    snake.move()
    assert snake.food_consumed == 1
    snake.food.respawn.assert_called_once()

def test_collision_with_self(snake: Snake) -> None:
    snake.body = [
        MapPosition(5, 5),
        MapPosition(5, 6),
        MapPosition(5, 7),
        MapPosition(6, 7),
        MapPosition(6, 6)
    ]
    snake.direction = (0, 1)
    result = snake.move()
    result = snake.move()
    assert not result
