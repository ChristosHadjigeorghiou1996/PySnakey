from dataclasses import dataclass

from .map_position import MapPosition

@dataclass
class Obstacle:
    position: MapPosition

    def get_position(self) -> MapPosition:
        return self.position