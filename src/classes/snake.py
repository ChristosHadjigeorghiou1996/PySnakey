from pygame.draw import rect

from src import CELL_SIZE, GRID_HEIGHT,  GRID_WIDTH, SCREEN, WHITE
from src.classes.map_position import MapPosition
from src.classes.food import Food

class Snake:
    def __init__(self, position: MapPosition, food: Food):
        self.body = [position]
        self.direction = (1, 0)
        self.food = food
        self.food_consumed = 0

    def move(self) -> bool:
        """
        Check the new position of the snake
        :return boolean if game continues
        Returns:
            _type_: _description_
        """
        map_position = self.body[0]
        x,y = map_position.x_pos, map_position.y_pos
        dx, dy = self.direction
        new_head = MapPosition((x + dx) % GRID_WIDTH, (y + dy) % GRID_HEIGHT)
        # snake eats itself
        if new_head in self.body[1:]:
            return False
        self.body.insert(0, new_head)
        if new_head != self.food.position:
            self.body.pop()
        else:
            self.grow()
            self.food.respawn()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow(self):
        self.food_consumed += 1
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            rect(SCREEN, WHITE, (segment.x_pos * CELL_SIZE, segment.y_pos * CELL_SIZE, CELL_SIZE, CELL_SIZE))