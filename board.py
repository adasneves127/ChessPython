import arcade
import pieces


class ChessWin(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "Chess")

        # Make a blank board
        self.board = [[None for _ in range(8)] for _ in range(8)]

        self.isLightMove = True

        self.fromPiece = None
        self.populatePieces()

        arcade.set_background_color(arcade.color.WHITE)

    def populatePieces(self):
        self.board = [
            [pieces.Rook(0, 0, True), pieces.Knight(1, 0, True), pieces.Bishop(2, 0, True), pieces.Queen(3, 0, True),
             pieces.King(4, 0, True), pieces.Bishop(5, 0, True), pieces.Knight(6, 0, True), pieces.Rook(7, 0, True)],
            [pieces.Pawn(i, 1, True) for i in range(8)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [pieces.Pawn(i, 6, False) for i in range(8)],
            [pieces.Rook(0, 7, False), pieces.Knight(1, 7, False), pieces.Bishop(2, 7, False), pieces.Queen(3, 7, False),
             pieces.King(4, 7, False),pieces.Bishop(5, 7, False), pieces.Knight(6, 7, False), pieces.Rook(7, 7, False)],

        ]

    def on_draw(self):
        arcade.start_render()
        for i in range(8):
            for j in range(8):
                color = arcade.color_from_hex_string("#fbcb9b") if (i%2 ^ j%2) else arcade.color_from_hex_string("#d38b43")
                arcade.draw_xywh_rectangle_filled(100 * i, 100 * j, 100, 100, color)
        for row in self.board:
            for piece in row:
                if piece is not None:
                    piece.draw()

        arcade.finish_render()


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        index_x = x // 100
        index_y = y // 100
        print(index_x, index_y)
        if self.fromPiece is None:
            print("getting new location")
            if self.board[index_y][index_x] is not None and self.board[index_y][index_x].isLight == self.isLightMove:

                self.fromPiece = self.board[index_y][index_x]
                self.fromPiece.is_sel = True
                print(self.fromPiece)

        else:
            # Get old indexes
            oldX, oldY = self.fromPiece.x, self.fromPiece.y
            if(index_x == oldX and index_y == oldY):
                self.fromPiece = None
                return

            if not self.fromPiece.check_move(self.board, [index_x, index_y]):
                return


            # Move piece
            self.fromPiece.x = index_x
            self.fromPiece.y = index_y
            self.fromPiece.center_x = index_x * 100 + 50
            self.fromPiece.center_y = index_y * 100 + 50
            print(oldX, oldY)
            # Update indexes in board
            self.board[oldY][oldX] = None
            self.board[index_y][index_x] = self.fromPiece
            self.fromPiece.is_sel = False
            self.fromPiece.is_moved = True
            self.fromPiece = None

            # Flip the board turn
            self.isLightMove = not self.isLightMove
