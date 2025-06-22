import board;

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    keyboard.col_pins = (board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP15, board.GP14, board.GP13, board.GP12, board.GP11)
    keyboard.row_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP0)

    keyboard.diode_orientation = DiodeOrientation.COL2ROW