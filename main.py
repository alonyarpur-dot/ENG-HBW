import pyperclip
import keyboard
import time

ENG_TO_HEB = {
    'a': 'ש', 'b': 'נ', 'c': 'ב', 'd': 'ג', 'e': 'ק',
    'f': 'כ', 'g': 'ע', 'h': 'י', 'i': 'ן', 'j': 'ח',
    'k': 'ל', 'l': 'ך', 'm': 'צ', 'n': 'מ', 'o': 'ם',
    'p': 'פ', 'q': '/', 'r': 'ר', 's': 'ד', 't': 'א',
    'u': 'ו', 'v': 'ה', 'w': "'", 'x': 'ס', 'y': 'ט',
    'z': 'ז', ',': 'ת', '.': 'ץ', ';': 'ף'
}

HEB_TO_ENG = {v: k for k, v in ENG_TO_HEB.items()}


def convert_text(text):
    converted = []
    for char in text:
        lower_char = char.lower()
        if lower_char in ENG_TO_HEB:
            converted.append(ENG_TO_HEB[lower_char])
        elif lower_char in HEB_TO_ENG:
            converted.append(HEB_TO_ENG[lower_char])
        else:
            converted.append(char)
    return "".join(converted)


def fix_selection():
    try:
        time.sleep(0.05)
        text = pyperclip.paste()
        if not text:
            return
        fixed = convert_text(text)
        pyperclip.copy(fixed)
    except Exception:

        pass


keyboard.add_hotkey('ctrl+alt+f', fix_selection)
keyboard.wait()
