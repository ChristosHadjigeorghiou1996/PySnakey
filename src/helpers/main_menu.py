from sys import exit
from pygame import quit, Surface, K_DOWN, K_UP, K_RETURN, KEYDOWN
from pygame.event import get
from pygame.time import wait

from src import BLACK, HEIGHT, RED, TEXT_FONTS, TITLE_FONTS, WHITE, WIDTH
from src.classes.map_position import MapPosition
from src.classes.menu_state_enum import MenuStateEnum
from src.helpers.high_score_helper import HighScoreHelper
from src.helpers.screen_helper import ScreenHelper

class MainMenu:
    def __init__(self, screen: Surface, high_score_helper: HighScoreHelper) -> None:
        self.screen = screen
        self.high_score_helper = high_score_helper
        self.menu_options = ["High Score Mode", "Story Mode", "View Key Bindings", "View High Scores", "Exit"]
        self.selected_option = 0
        self.option_color = BLACK
        self.selected_color = RED
        self.menu_state = MenuStateEnum.MAIN_MENU
    
    def display_menu(self) -> None:
        self.screen.fill(WHITE)
        game_title_position = HEIGHT // 2 - 110 
        # Display menu options
        ScreenHelper.display_text_on_screen(self.screen,
                                    TITLE_FONTS,
                                    "Welcome to PySnakey",
                                    self.option_color,
                                    MapPosition(WIDTH // 2, game_title_position))
        initial_menu_position = HEIGHT // 2 - 50 
        for idx, value in enumerate(self.menu_options):
            # if idx is 0 then skip
            initial_menu_position += 50
            text_color = self.selected_color if idx == self.selected_option \
                else  self.option_color
            ScreenHelper.display_text_on_screen(self.screen,
                                                TITLE_FONTS,
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
                            TITLE_FONTS,
                            "Key Bindings",
                            BLACK,
                            MapPosition(WIDTH // 2, initial_menu_position)) 

        for action, key in key_bindings.items():
            initial_menu_position += 50
            ScreenHelper.display_text_on_screen(self.screen,
                                                TITLE_FONTS,
                                                f"{action}: {key}",
                                                BLACK,
                                                MapPosition(WIDTH // 2, initial_menu_position))
        # note that any button will go back to main menu
        initial_menu_position += 75
        ScreenHelper.display_text_on_screen(self.screen,
                                            TITLE_FONTS,
                                            f"Press any button to go to main menu",
                                            BLACK,
                                            MapPosition(WIDTH // 2, initial_menu_position))

    def display_high_scores(self):
        self.screen.fill(BLACK)
        high_scores = self.high_score_helper.load_high_scores()
        # leaderboard title
        ScreenHelper.display_text_on_screen(self.screen,
                                            TITLE_FONTS,
                                            "HALL OF FAME LEADERBOARD!",
                                            color=WHITE,
                                            map_position=MapPosition(WIDTH // 2, 40))

        if not high_scores:
            ScreenHelper.display_text_on_screen(self.screen,
                                                TEXT_FONTS,
                                                "No high scores saved!",
                                                color=WHITE,
                                                map_position=MapPosition(WIDTH // 2, HEIGHT // 2))

        for i, score in enumerate(high_scores):
            text = f"{i + 1}. {score}"
            ScreenHelper.display_text_on_screen(self.screen, TEXT_FONTS, text, color=WHITE, map_position=MapPosition(WIDTH // 2, 50 + (i + 1) * 40))

        ScreenHelper.display_text_on_screen(self.screen,
                                            TEXT_FONTS,
                                            "Click any button to return",
                                            color=WHITE,
                                            map_position=MapPosition(WIDTH // 2, HEIGHT - 50))

    def handle_events(self) -> bool:
        for event in get():
            if event.type == KEYDOWN:
                if self.menu_state == MenuStateEnum.KEY_BINDINGS or self.menu_state == MenuStateEnum.VIEW_HIGH_SCORES:
                    self.menu_state = MenuStateEnum.MAIN_MENU
                if event.key == K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                elif event.key == K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                elif event.key == K_RETURN:
                    if self.selected_option == 0:
                        self.menu_state = MenuStateEnum.HIGH_SCORE_MODE
                    if self.selected_option == 1:
                        self.menu_state = MenuStateEnum.STORY_MODE
                    elif self.selected_option == 2:
                        self.menu_state = MenuStateEnum.KEY_BINDINGS
                    elif self.selected_option == 3:
                        self.menu_state = MenuStateEnum.VIEW_HIGH_SCORES
                    elif self.selected_option == 4:
                        self.menu_state = MenuStateEnum.EXIT
                        quit()
                        exit()
                return True
        return True
