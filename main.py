from window import get_active_window_title, is_discord
import keyboard
import pyautogui
import time
import pyperclip
from phrase import get_phrase



def on_enter():
    text = get_phrase()
    time.sleep(0.1)
    pyperclip.copy(text)
    
    pyautogui.hotkey('shift', 'enter')
    pyautogui.hotkey('shift', 'enter')
    
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    
def main():

    while True:
        if not is_discord(get_active_window_title()): 
            continue
        keyboard.add_hotkey('enter', on_enter, suppress=True)
        keyboard.wait('enter')

if __name__ == "__main__":
    main()
    