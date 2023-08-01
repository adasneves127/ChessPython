import arcade
from typing import List

class basePiece(arcade.Sprite):
    def __init__(self, path):
        super().__init__(path, scale=0.05)
        self.is_sel = False
        self.is_moved = False

    def draw(self, *, filter=None, pixelated=None, blend_function=None):

        if self.is_sel:
            arcade.draw_xywh_rectangle_filled(self.center_x - 50, self.center_y - 50, 100, 100, arcade.color.GRAY)
        super().draw()


class Knight(basePiece):
    def __init__(self, x, y, isLight):
        self.isLight = isLight
        self.x, self.y = x, y
        super().__init__(f"./assets/n{'l' if isLight else 'd'}t.png")
        self.center_x = (100 * x) + 50
        self.center_y = (100 * y) + 50

    def check_move(self, board, target_loc: List[int]) -> bool:
        return False

class King(basePiece):
    def __init__(self, x, y, isLight):
        self.isLight = isLight
        self.x, self.y = x, y
        super().__init__(f"./assets/k{'l' if isLight else 'd'}t.png")
        self.center_x = (100 * x) + 50
        self.center_y = (100 * y) + 50

    def check_move(self, board, target_loc: List[int]) -> bool:
        return False

class Pawn(basePiece):
    def __init__(self, x, y, isLight):
        self.isLight = isLight
        self.x, self.y = x, y
        super().__init__(f"./assets/p{'l' if isLight else 'd'}t.png")
        self.center_x = (100 * x) + 50
        self.center_y = (100 * y) + 50

    def check_move(self, board, target_loc: List[int]) -> bool:
        # If the piece is not moving straight, and is not capturing
        if self.isLight:
            # Check that we are moving up in ranks:
            if target_loc[1] <= self.y and board[target_loc[1]][target_loc[0]] is not None:
                return False
            if self.x != target_loc[0] and board[target_loc[1]][target_loc[0]] is None:
                # If we are moving diagonally, but not capturing
                return False
            if self.is_moved and target_loc[1] - self.y > 1:
                return False
        else:
            # Check that we are moving down in ranks:
            if target_loc[1] >= self.y:
                return False



        return True

class Queen(basePiece):
    def __init__(self, x, y, isLight):
        self.isLight = isLight
        self.x, self.y = x, y
        super().__init__(f"./assets/q{'l' if isLight else 'd'}t.png")
        self.center_x = (100 * x) + 50
        self.center_y = (100 * y) + 50

    def check_move(self, board, target_loc: List[int]) -> bool:
        return False

class Rook(basePiece):
    def __init__(self, x, y, isLight):
        self.isLight = isLight
        self.x, self.y = x, y
        super().__init__(f"./assets/r{'l' if isLight else 'd'}t.png")
        self.center_x = (100 * x) + 50
        self.center_y = (100 * y) + 50

    def check_move(self, board, target_loc: List[int]) -> bool:
        return False

class Bishop(basePiece):
    def __init__(self, x, y, isLight):
        self.isLight = isLight
        self.x, self.y = x, y
        super().__init__(f"./assets/b{'l' if isLight else 'd'}t.png")
        self.center_x = (100 * x) + 50
        self.center_y = (100 * y) + 50

    def check_move(self, board, target_loc: List[int]) -> bool:
        return False


