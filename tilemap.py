import tile


class TileMap:
    def __init__(self, screen_w, screen_h, tiles_w, tiles_h):
        self.map_width_in_pix = screen_w
        self.map_height_in_pix = screen_h
        self.number_of_columns = tiles_w
        self.number_of_rows = tiles_h
        self.tile_map = []

        self.build_tile_map()

    def build_tile_map(self):
        for column in range(self.number_of_columns):
            self.tile_map.append([])
            for row in range(self.number_of_rows):
                self.tile_map[column].append(tile.Tile(column, row, True))

    # 2D Array [Column #][Array of Rows as Tiles]
    def get_tile_map(self):
        # Example
        # [ [Tile(0,0), Tile(0,1), Tile(0,2)],
        #   [Tile(1,0), Tile(1,1), Tile(1,2)],
        #   [Tile(2,0), Tile(2,1), Tile(2,2)], ]
        return self.tile_map

    # Returns the Tile object for the given column and row
    def get_tile(self, column, row):
        return self.tile_map[column][row]

    # Dummy Check that tile list is correct
    def print_tile_map_to_console(self):
        for column in range(len(self.tile_map)):
            print("Column ", column, " has Row Tiles: ", end="")
            for row in range(len(self.tile_map[column])):
                print(
                    "(",
                    self.get_tile(column, row).get_tile_column_num(),
                    ", ",
                    self.get_tile(column, row).get_tile_row_num(),
                    ") ",
                    end="",
                )
            print()

    # Dummy Check that the Tile has correct info
    def print_tile_info(self, column, row):
        print("Tile info requested for: ", column, ", ", row)
        print("     Column: ", self.get_tile(column, row).get_tile_column_num())
        print("     Row: ", self.get_tile(column, row).get_tile_row_num())
        print("     Walkable: ", self.get_tile(column, row).get_is_walkable())
        print("     Occupied: ", self.get_tile(column, row).get_is_occupied())
        print()

    def get_num_of_columns(self):
        return self.number_of_columns

    def get_num_of_rows(self):
        return self.number_of_rows

    def get_map_width_pix(self):
        return self.map_width_in_pix

    def get_map_height_pix(self):
        return self.map_height_in_pix
