class Tile:
    def __init__(self, x, y, walkable):
        self.x_pos = x
        self.y_pos = y
        self.is_walkable = walkable
        self.is_occupied = False

    def get_is_walkable(self):
        return self.is_walkable

    def get_is_occupied(self):
        return self.is_occupied

    def set_is_occupied(self, new_flag):
        self.is_walkable = new_flag

    def get_tile_x_pos(self):
        return self.x_pos

    def get_tile_y_pos(self):
        return self.y_pos
