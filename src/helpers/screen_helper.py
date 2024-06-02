from typing import Tuple
import datetime
import os

from pygame import display, image, Surface, error
from pygame.font import Font

from src import LOGGER, HEIGHT, SCREENSHOTS_PATH, SCREEN, STATUS_BAR_HEIGHT, WHITE, WIDTH
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
        try:
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
        except error as e:
            LOGGER.error(f"Error when displaying text {display_text} on screen: {str(e)}")

    @staticmethod
    def take_screenshot() -> None:
        """
        Take screenshot of the entire screen and save it
            with current datetime name at provided folder
        """
        # use datetime as filename
        filename = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S.png")
        filename_path = os.path.join(SCREENSHOTS_PATH, filename)
        os.makedirs(SCREENSHOTS_PATH, exist_ok=True)
        try:
            image.save(SCREEN, filename_path)
        except error as e:
            LOGGER.error(f"Error when taking screenshot: {str(e)}")
        finally:
            LOGGER.debug(f"Is file saved: {os.path.isfile(filename_path)}")
