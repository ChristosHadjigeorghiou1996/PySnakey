from enum import Enum

class MenuStateEnum(Enum):
    MAIN_MENU: str = "main_menu"
    START_GAME: str = "start_game"
    KEY_BINDINGS: str="key_bindings"
    EXIT: str = "exit"