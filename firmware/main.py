print("STARTING")

import board;

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.modules.macros import Macros

print(dir(board))

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)
keyboard.modules.append(Macros())

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29, board.GP10)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

QWERTY_LAYER = KC.TO(0)
NUM_LAYER = KC.TO(1)
FUNC_LAYER = KC.TO(2)
MOUSE_LAYER = KC.TO(3)

COPY_PASTE = KC.MACRO(KC.LGUI(KC.C), KC.LGUI(KC.V))
SELECT_ALL = KC.LGUI(KC.A)
UNDO = KC.LGUI(KC.Z)
REDO = KC.LGUI(KC.LSFT(KC.Z))
CUT = KC.LGUI(KC.X)
PASTE = KC.LGUI(KC.V)
COPY = KC.LGUI(KC.C)
SAVE = KC.LGUI(KC.S)
NEW_TAB = KC.LGUI(KC.T)
CLOSE_TAB = KC.LGUI(KC.W)
QUIT_APP = KC.LGUI(KC.Q)
SPOTLIGHT = KC.LGUI(KC.SPACE)
MISSION_CONTROL = KC.LCTRL(KC.UP)
APP_EXPOSE = KC.LCTRL(KC.DOWN)

LAYER_1 = KC.MO(1)
LAYER_2 = KC.MO(2)
LAYER_3 = KC.MO(3)

tapdance.tap_dance_keys = {
    KC.SPACE: [KC.SPACE, QWERTY_LAYER, NUM_LAYER, FUNC_LAYER, MOUSE_LAYER],
    KC.LGUI: [KC.LGUI, COPY, PASTE], 
    KC.Q: [KC.Q, KC.TAB, KC.ESC],
    KC.LALT: [KC.LALT, KC.LSFT(KC.LALT)],
    KC.RALT: [KC.RALT, KC.RSFT(KC.RALT)] 
}

keyboard.keymap = [
    [
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
        KC.LCTRL,LAYER_2, KC.LALT, LAYER_1, KC.SPACE,KC.SPACE,LAYER_1, KC.RALT, LAYER_3, KC.LGUI
    ], 
    [ 
        KC.GRV,  KC.MINS, KC.EQL,  KC.LBRC, KC.RBRC, KC.BSLS, SAVE,    NEW_TAB, CLOSE_TAB,KC.BSPC,
        KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.TAB,  CUT,     COPY,    PASTE,   UNDO,    REDO,    SELECT_ALL,KC.COMM,KC.DOT,  KC.ENT,
        KC.LCTRL,KC.TRNS, KC.LALT, KC.TRNS, KC.SPACE,KC.SPACE,KC.TRNS, KC.RALT, KC.TRNS, KC.LGUI
    ],
    [
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.DEL,
        KC.TAB,  KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.HOME, KC.PGDN, KC.PGUP, KC.END,  SPOTLIGHT,
        KC.CAPS, KC.VOLD, KC.VOLU, KC.MUTE, KC.BRIU, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.QUOT,
        KC.LSFT, KC.MPRV, KC.MPLY, KC.MNXT, KC.BRID, MISSION_CONTROL,APP_EXPOSE,QUIT_APP,KC.INS,KC.RSFT,
        KC.LCTRL,KC.TRNS, KC.LALT, KC.TRNS, KC.SPACE,KC.SPACE,KC.TRNS, KC.RALT, KC.TRNS, KC.LGUI
    ]
]

if __name__ == '__main__':
    keyboard.go()