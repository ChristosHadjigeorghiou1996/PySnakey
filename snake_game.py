import pygame

from src import BLACK, CELL_SIZE, GRID_HEIGHT, GRID_WIDTH, HEIGHT, LOGGER, SCREEN, TEXT_FONTS, TITLE_FONTS, WHITE, WIDTH
from src.classes.map_position import MapPosition
from src.classes.levels import Levels
from src.helpers.main_menu import MainMenu
from src.classes.menu_state_enum import MenuStateEnum
from src.helpers.screen_helper import ScreenHelper
from src.helpers.high_score_helper import HighScoreHelper


class SnakeGame:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.main_menu = MainMenu(self.screen)
        self.celebration_group = pygame.sprite.Group()
        self.levels = Levels().get_levels()
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self) -> None:
        """
        Reset the game and enable to start again from main menu
        """
        self.current_level = 0
        self.high_score_helper = HighScoreHelper()
        self.snake, self.food, self.score = self.high_score_helper\
            .initialize_snake_food_positions_and_score()
        self.current_level = 0
        self.start = True
        self.pause = False
        self.waiting_for_click = False
        self.is_done = False
        self.grid_dimensions = (GRID_WIDTH, GRID_HEIGHT)

    def get_is_done(self) -> bool:
        return self.is_done

    def set_is_done(self, is_done: bool) -> None:
        self.is_done= is_done

    def get_clock(self) -> pygame.time.Clock:
        return self.clock

    def get_waiting_for_click(self) -> bool:
        return self.waiting_for_click

    def set_waiting_for_click(self, waiting: bool) -> None:
        self.waiting_for_click = waiting

    def is_paused(self) -> bool:
        """
        Check if the game is paused
        :return True if game is paused else False
        """
        return self.pause

    def get_current_level(self) -> int:
        """
        Get the current level of the game
        :return the number of the level
        """
        return self.current_level

    def set_current_level(self, level: int) -> None:
        """
        Set the current level of the game
        :param level: integer level of game
        """
        self.current_level = level

    def game_finished(self) -> None:
        """
        Finish the game by toggling done flag and wait for input
        """
        self.is_done = True

        # iterate through options and show them on screen
        for index, text in enumerate(["Mouse click to go to main menu", "Click q to exit"]):
            ScreenHelper.display_text_on_screen(self.screen,
                                                TITLE_FONTS,
                                                text,
                                                map_position=MapPosition(WIDTH // 2, HEIGHT // 2 + (index + 1) * 50 ))
        while self.is_done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.reset_game()
                    self.main_menu.menu_state = MenuStateEnum.MAIN_MENU
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                
            pygame.display.flip()
            self.clock.tick(10)  

    def display_screen_after_level(self) -> None:
        """
        Display screen after finishing level
        """
        self.current_level += 1
        ScreenHelper.display_text_on_screen(self.screen, TITLE_FONTS, "Congrats on finishing the game!")
        self.game_finished() if self.current_level == len(self.levels) else self.start_level()

    def start_level(self) -> None:
        """
        Start the new level and wait for click to play it
        """
        self.waiting_for_click = True
        self.level = self.levels[self.current_level]

    def pause_screen(self) -> None:
        """
        Pause screen and wait for 'p' to be pressed
        """
        ScreenHelper.display_text_on_screen(self.screen, TITLE_FONTS, "Press p to continue")
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pygame.display.flip()
            self.clock.tick(10)   

    def handle_events(self) -> bool:
        """
        Handle events in pygame and checking its type
        :return True if the game continues
        """
        snake = self.snake if self.main_menu.menu_state == MenuStateEnum.HIGH_SCORE_MODE \
            else self.level.snake
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
                # check if P is pressed for pause
                elif event.key == pygame.K_p:
                    self.pause = True
                    self.pause_screen()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.waiting_for_click and not self.is_done:
                    self.waiting_for_click = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                return False
        return True
    
    def update(self) -> bool:
        """
        Update the sprites and the logic for playing game
        :return True if playing game else False
        """
        if not self.get_waiting_for_click():
            if self.is_done:
                self.is_done = not self.is_done
                self.main_menu.menu_state = MenuStateEnum.MAIN_MENU
            else:
                if self.main_menu.menu_state == MenuStateEnum.HIGH_SCORE_MODE:
                    snake = self.snake
                    food = self.food
                    obstacles = None
                    food_objective = None
                    level_text = "   High score mode"
                    consumed_text = f"Score: {snake.food_consumed * 10}"
                else:
                    snake = self.level.snake
                    food = self.level.food
                    obstacles = self.level.obstacles
                    food_objective = self.level.food_objective
                    level_text = f"  Level: {self.get_current_level() + 1}"
                    consumed_text = f"Consumed: {self.level.snake.food_consumed}/{self.level.food_objective}"
                # draw the level information on the bottom part of the screen
                ScreenHelper.display_text_on_screen(self.screen, TEXT_FONTS, level_text, top_left=True)
                ScreenHelper.display_text_on_screen(self.screen, TEXT_FONTS, consumed_text, top_right=True)
                snake.draw()
                food.draw()
                if obstacles:
                    for obstacle in obstacles:
                        pygame.draw.rect(self.screen, WHITE,  
                                        (obstacle.position.x_pos * CELL_SIZE,
                                        obstacle.position.y_pos * CELL_SIZE,
                                        CELL_SIZE,
                                        CELL_SIZE))
                if snake.move():
                    if snake.body[0] == food.position:
                        snake.grow()
                        food.respawn()
                else:
                    return False

                if food_objective and snake.food_consumed == food_objective:
                    self.display_screen_after_level()
        else:
            if self.is_done:
                message = "Mouse click to navigate to main menu"
            if self.current_level == 0:
                message = "Welcome to PySnakey!"
                # add the text below the first one
                ScreenHelper.display_text_on_screen(self.screen,
                                                    TITLE_FONTS,
                                                    "Right click to start!",
                                                    map_position=MapPosition(WIDTH // 2, HEIGHT // 2 + 50))

            elif self.current_level == len(self.levels):
                message = "Congrats you have finished the game!"
                self.is_done = True
            else:
                message = "Right click to start the next level!"
            ScreenHelper.display_text_on_screen(self.screen, TITLE_FONTS, message)
        return True

def main():
    # Create a new SnakeGame instance for the main menu
    snake_game = SnakeGame(SCREEN)
    snake_game.start_level()
    running = True

    while running:
        SCREEN.fill(BLACK)
        # Handle events based on the current menu state
        if snake_game.main_menu.menu_state == MenuStateEnum.MAIN_MENU or \
                snake_game.main_menu.menu_state == MenuStateEnum.KEY_BINDINGS:
            running = snake_game.main_menu.handle_events()
            # Check if the game should start
            if snake_game.main_menu.menu_state == MenuStateEnum.KEY_BINDINGS:
                snake_game.main_menu.view_key_bindings()
            elif snake_game.main_menu.menu_state == MenuStateEnum.MAIN_MENU:
                snake_game.main_menu.display_menu()
        else:
            running = snake_game.update() and snake_game.handle_events()

        if not running:
            ScreenHelper.take_screenshot()
            ScreenHelper.display_text_on_screen(snake_game.screen, TITLE_FONTS, "You have lost.")
            snake_game.game_finished()
            if not snake_game.is_done:
                running = True
        try:
            # update display if the game is not over
            pygame.display.flip()
        except pygame.error as e:
            LOGGER.error(f"Error when updating the display: {str(e)}")
        # frame rate
        snake_game.get_clock().tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()