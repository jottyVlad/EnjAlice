from enum import Enum

DEFAULT_START_TEXT = "There is no start text defined"


class Sounds(str, Enum):
    Chainsaw = '<speaker audio="alice-sounds-things-chainsaw-1.opus">'
    Explosion = '<speaker audio="alice-sounds-things-explosion-1.opus">'
    WaterPouredIntoGlass = '<speaker audio="alice-sounds-things-water-3.opus">'
    Water1Pouring = '<speaker audio="alice-sounds-things-water-1.opus">'
    Water2Seethes = '<speaker audio="alice-sounds-things-water-2.opus">'
    Switch1 = '<speaker audio="alice-sounds-things-switch-1.opus">'
    Switch2 = '<speaker audio="alice-sounds-things-switch-2.opus">'
    ShotShothun = '<speaker audio="alice-sounds-things-gun-1.opus">'
    ShipHorn1 = '<speaker audio="alice-sounds-transport-ship-horn-1.opus">'
    ShipHorn2 = '<speaker audio="alice-sounds-transport-ship-horn-2.opus">'
    Door1 = '<speaker audio="alice-sounds-things-door-1.opus">'
    Door2 = '<speaker audio="alice-sounds-things-door-2.opus">'
    ClinkingGlasses = '<speaker audio="alice-sounds-things-glass-2.opus">'
    Bell1 = '<speaker audio="alice-sounds-things-bell-1.opus">'
    Bell2 = '<speaker audio="alice-sounds-things-bell-2.opus">'
    CarStarts = '<speaker audio="alice-sounds-things-car-1.opus">'
    CarDontStarts = '<speaker audio="alice-sounds-things-car-2.opus">'
