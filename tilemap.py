import tile


class TileMap:
    def __init__(self, screen_w, screen_h, tiles_w, tiles_h):
        self.map_width_in_pix = screen_w
        self.map_height_in_pix = screen_h
        self.map_width_in_tiles = tiles_w
        self.map_height_in_tiles = tiles_h
        self.tile_map = []

        self.build_tile_map()

    def build_tile_map(self):
        for x in range(self.map_height_in_tiles):
            self.tile_map.append([])
            for y in range(self.map_width_in_tiles):
                self.tile_map[x].append(tile.Tile(x, y, True))

    def get_tile_map(self):
        return self.tile_map

    def get_tile(self, x, y):
        return self.tile_map[x][y]

    def print_tile_map_to_console(self):
        for i in range(len(self.tile_map)):
            print("Row ", i, " has tiles: ", end="")
            for j in range(len(self.tile_map[i])):
                print(
                    "(",
                    self.get_tile(i, j).get_tile_x_pos(),
                    ", ",
                    self.get_tile(i, j).get_tile_y_pos(),
                    ") ",
                    end="",
                )
            print()
