# Tiles are Column(x), Row(y) based
class Tile:
    def __init__(self, column, row, walkable):
        self.column_pos = column
        self.row_pos = row
        self.is_walkable = walkable
        self.is_occupied = False

    def get_is_walkable(self):
        return self.is_walkable

    def get_is_occupied(self):
        return self.is_occupied

    def set_is_occupied(self, new_flag):
        self.is_walkable = new_flag

    # X Position
    def get_tile_column_num(self):
        return self.column_pos

    # Y Position
    def get_tile_row_num(self):
        return self.row_pos
