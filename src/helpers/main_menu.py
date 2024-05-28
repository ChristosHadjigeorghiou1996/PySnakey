from sys import exit
from pygame import display, quit, Surface, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_RETURN, KEYDOWN
from pygame.event import get
from pygame.font import Font

from src import BLACK, HEIGHT, MENU_OPTIONS, RED, TEXT_FONT_SIZE, TITLE_FONT_SIZE, WHITE, WIDTH
from src.classes.map_position import MapPosition
from src.classes.menu_state_enum import MenuStateEnum
from src.helpers.screen_helper import ScreenHelper


class MainMenu:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.menu_options_state = {
            'main_menu' : 'Main menu',
            'start_game': 'Start Game',
            'view_key_bindings': 'View Key Bindings',
            'exit': 'Exit'
        }
        self.menu_options = MENU_OPTIONS
        self.selected_option = 0
        self.title_font = Font(None, TITLE_FONT_SIZE)
        self.text_font = Font(None, TEXT_FONT_SIZE)
        self.option_color = BLACK
        self.selected_color = RED
        self.menu_state = MenuStateEnum.MAIN_MENU
    
    def display_menu(self) -> None:
        self.screen.fill(WHITE)
        initial_menu_position = HEIGHT // 2 - 50 
        # Display menu options
        ScreenHelper.display_text_on_screen(self.screen,
                                    self.title_font,
                                    "Welcome to PySnakey",
                                    self.option_color,
                                    MapPosition(WIDTH // 2, initial_menu_position))
        for idx, value in enumerate(self.menu_options):
            # if idx is 0 then skip
            initial_menu_position += 50
            text_color = self.selected_color if idx == self.selected_option \
                else  self.option_color
            ScreenHelper.display_text_on_screen(self.screen,
                                                self.text_font,
                                                value,
                                                text_color,
                                                MapPosition(WIDTH // 2, initial_menu_position))

    def view_key_bindings(self) -> None:
        key_bindings = {
            "Move Up": "Arrow Up",
            "Move Down": "Arrow Down",
            "Move Left": "Arrow Left",
            "Move Right": "Arrow Right",
            "Pause": "P",
            "Quit": "Q"
        }

        self.screen.fill(WHITE)
        initial_menu_position = HEIGHT // 4 - 50 
        ScreenHelper.display_text_on_screen(self.screen,
                            self.title_font,
                            "Key Bindings",
                            BLACK,
                            MapPosition(WIDTH // 2, initial_menu_position)) 

        for action, key in key_bindings.items():
            initial_menu_position += 50
            ScreenHelper.display_text_on_screen(self.screen,
                                                self.text_font,
                                                f"{action}: {key}",
                                                BLACK,
                                                MapPosition(WIDTH // 2, initial_menu_position))
        # note that any button will go back to main menu
        initial_menu_position += 75
        ScreenHelper.display_text_on_screen(self.screen,
                                            self.text_font,
                                            f"Press any button to go to main menu",
                                            BLACK,
                                            MapPosition(WIDTH // 2, initial_menu_position))

    def handle_events(self) -> bool:
        for event in get():
            if event.type == KEYDOWN:
                if self.menu_state == MenuStateEnum.KEY_BINDINGS:
                    self.menu_state = MenuStateEnum.MAIN_MENU
                if event.key == K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                elif event.key == K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                elif event.key == K_RETURN:
                    if self.selected_option == 0:
                        self.menu_state = MenuStateEnum.START_GAME
                    elif self.selected_option == 1:
                        self.menu_state = MenuStateEnum.KEY_BINDINGS
                    elif self.selected_option == 2:
                        self.menu_state = MenuStateEnum.EXIT
                        quit()
                        exit()
                return True
        return True
