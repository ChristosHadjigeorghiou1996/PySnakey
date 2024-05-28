from typing import Tuple

from pygame import Surface
from pygame.font import Font

from src import HEIGHT, WHITE, WIDTH, STATUS_BAR_HEIGHT
from src.classes.map_position import MapPosition


class ScreenHelper:
    @staticmethod
    def display_text_on_screen(screen: Surface,
                               font: Font,
                               display_text: str,
                               color: Tuple[int, int ,int] = None,
                               map_position: MapPosition = None,
                               top_left:bool = False,
                               top_right: bool = False) -> None:
        text = font.render(display_text, True, color) if color else \
            font.render(display_text, True, WHITE)
        text_rect = text.get_rect()
        if map_position:
            text_rect.center = (map_position.x_pos, map_position.y_pos)
        else:
            vertical = HEIGHT - STATUS_BAR_HEIGHT + 5
            if top_left:
                text_rect.top = vertical
            elif top_right:
                text_rect.topright = (WIDTH - 10, vertical)
            else:
                text_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(text, text_rect)
