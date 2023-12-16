from .constants import*

UNIT_STATS = {
    'Strength': 0,
    'Agility': 0,
    'HP': 0,
    'Field Position': '',
    'Name': ''
}

class Unit:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.direction = 1

    self.x = 0
    self.y = 0

    def calc_pos(self):