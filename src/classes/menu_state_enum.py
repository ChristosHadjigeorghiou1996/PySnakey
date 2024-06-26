from enum import StrEnum

class MenuStateEnum(StrEnum):
    MAIN_MENU = "main_menu"
    STORY_MODE = "story_mode"
    HIGH_SCORE_MODE = "high_score_mode"
    KEY_BINDINGS = "key_bindings"
    VIEW_HIGH_SCORES = "view_high_scores"
    EXIT = "exit"
