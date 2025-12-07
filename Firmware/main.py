# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

#Add layer extension
keyboard.modules.append(Layers())

#Add encoder extension
encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

#Add rgb extension
rgb = RGB(pixel_pin=board.GPIO6, num_pixels=4)
keyboard.extensions.append(rgb)

# Define your pins here!
PINS = [board.GPIO7, board.GPIO0, board.GPIO1, board.GPIO2, board.GPIO4, board.GPIO3]

#Define Encoder pins
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GPIO29, board.GPIO28, board.GPIO27)
    )

#Define Macros
WIN_TAB = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.TAB),
    Release(KC.LGUI)
)
WIN_CTRL_LEFT = KC.MACRO(
    Press(KC.LGUI),
    Press(KC.LCTRL),
    Tap(KC.LEFT),
    Release(KC.LCTRL),
    Release(KC.LGUI)
)
WIN_CTRL_RIGHT = KC.MACRO(
    Press(KC.LGUI),
    Press(KC.LCTRL),
    Tap(KC.RIGHT),
    Release(KC.LCTRL),
    Release(KC.LGUI)
)
WIN_CTRL_D = KC.MACRO(
    Press(KC.LGUI),
    Press(KC.LCTRL),
    Tap(KC.D),
    Release(KC.LCTRL),
    Release(KC.LGUI)
)
SHIFT_TAB = KC.MACRO(
    Press(KC.LSHIFT),
    Tap(KC.TAB),
    Release(KC.LSHIFT)
)
CTRL_ALT_DEL = KC.MACRO(
    Press(KC.LCTRL),
    Press(KC.LALT),
    Tap(KC.DELETE),
    Release(KC.LCTRL),
    Release(KC.LALT)
)
WIN_PRINT = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.PSCREEN),
    Release(KC.LGUI)
)
STRG_Z = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Z),
    Release(KC.LCTL)
)
STRG_Y = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Y),
    Release(KC.LCTL)
)
RED = KC.MACRO(rgb.set_hsv_fill(0, 100, 255))
GREEN = KC.MACRO(rgb.set_hsv_fill(100, 100, 255))
BLUE = KC.MACRO(rgb.set_hsv_fill(240, 100, 255))
PURPLE = KC.MACRO(rgb.set_hsv_fill(340, 100, 255))
WHITE = KC.MACRO(rgb.set_hsv_fill(0, 0, 255))
OFF = KC.MACRO(rgb.off())


# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
keyboard.keymap = [
    [WIN_PRINT, WIN_TAB, WIN_CTRL_LEFT, WIN_CTRL_D, CTRL_ALT_DEL, WIN_CTRL_RIGHT]
    [RED, GREEN, BLUE, PURPLE, WHITE, OFF]
]

encoder_handler.map = [ (( KC.TAB, SHIFT_TAB, KC.MO(2))), # Layer 1
                        ((STRG_Z, STRG_Y, KC.TRNS) ) # Layer 2
                      ]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
