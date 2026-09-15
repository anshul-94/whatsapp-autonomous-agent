import pyautogui
import pyperclip
import time


# =========================
# CHAT AREA
# =========================

CHAT_START_X = 654
CHAT_START_Y = 226

CHAT_END_X = 1417
CHAT_END_Y = 1009


# =========================
# MESSAGE BOX
# =========================

# IMPORTANT:
# Put your mouse on the WhatsApp
# "Type a message" box and get
# its coordinates using cursor.py.

INPUT_X = 739
INPUT_Y = 1008


def read_chat():

    pyperclip.copy("")

    pyautogui.moveTo(
        CHAT_START_X,
        CHAT_START_Y
    )

    pyautogui.dragTo(
        CHAT_END_X,
        CHAT_END_Y,
        duration=1,
        button="left"
    )

    time.sleep(1)

    pyautogui.hotkey(
        "command",
        "c"
    )

    time.sleep(2)

    chat_history = pyperclip.paste()

    return chat_history


def get_last_message(chat_history):

    if not chat_history:
        return ""

    lines = [
        line.strip()
        for line in chat_history.splitlines()
        if line.strip()
    ]

    if not lines:
        return ""

    return lines[-1]


def send_message(message):

    print("Sending:", message)

    pyperclip.copy(message)

    pyautogui.click(
        INPUT_X,
        INPUT_Y
    )

    time.sleep(0.5)

    pyautogui.hotkey(
        "command",
        "v"
    )

    time.sleep(0.5)

    pyautogui.press("enter")

    print("Message sent!")
