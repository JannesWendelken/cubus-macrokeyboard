#main.py by jayjay
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
keyboard.modules.append(Macros())

PINS = [
    board.D3,
    board.D4,
    board.D2,
    board.D1,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        # Key 1: Strg+C, Strg+V
        KC.Macro(
            Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD),
            Tap(KC.NO),  # slight spacer
            Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)
        ),

        # Key 2:Cmd + Shift + 4
        KC.Macro(
            Press(KC.LCMD), Press(KC.LSHIFT),
            Tap(KC.KC_4),
            Release(KC.LSHIFT), Release(KC.LCMD)
        ),

        # Key 3: Cmd + S
        KC.Macro(
            Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)
        ),

        # Key 4: Mute and Play and Pause
        KC.MACRO(
            Press(KC.MUTE), Release(KC.MUTE),
            Tap(KC.MEDIA_PLAY_PAUSE)
        ),
    ]
]

if __name__ == '__main__':
    keyboard.go()
