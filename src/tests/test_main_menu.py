import pytest
import pygame
from unittest.mock import Mock, patch
from src.classes.menu_state_enum import MenuStateEnum
from src.helpers.main_menu import MainMenu

@pytest.fixture
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def screen():
    return Mock(spec=pygame.Surface)

@pytest.fixture
def main_menu(screen) -> MainMenu:
    return MainMenu(screen)

def test_initial_state(main_menu: MainMenu):
    assert main_menu.menu_state == MenuStateEnum.MAIN_MENU
    assert main_menu.selected_option == 0

def test_handle_events_up_key_2(main_menu: MainMenu):
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP})
    pygame.event.post(event)
    main_menu.handle_events()
    assert main_menu.selected_option == 3


def test_handle_events_down_key(main_menu: MainMenu):
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_DOWN})
    pygame.event.post(event)
    main_menu.handle_events()
    assert main_menu.selected_option == 1

def test_handle_events_enter_key_high_score(main_menu: MainMenu):
    main_menu.selected_option = 0
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
    pygame.event.post(event)
    main_menu.handle_events()
    assert main_menu.menu_state == MenuStateEnum.HIGH_SCORE_MODE

def test_handle_events_enter_key_view_key_story_mode(main_menu: MainMenu):
    main_menu.selected_option = 1
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
    pygame.event.post(event)
    main_menu.handle_events()
    assert main_menu.menu_state == MenuStateEnum.STORY_MODE

def test_handle_events_enter_key_bindings(main_menu: MainMenu):
    main_menu.selected_option = 2
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
    pygame.event.post(event)
    main_menu.handle_events()
    assert main_menu.menu_state == MenuStateEnum.KEY_BINDINGS

def test_handle_events_enter_exit(main_menu: MainMenu):
    main_menu.selected_option = 3
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RETURN})
    with patch('pygame.quit') as mock_quit:
        with pytest.raises(SystemExit):
            pygame.event.post(event)
            main_menu.handle_events()
            print(main_menu.menu_state)
            mock_quit.assert_called_once()
