from dataclasses import dataclass

from .map_position import MapPosition

@dataclass
class Obstacle:
    char: str
    position: MapPosition