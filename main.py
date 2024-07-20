from window import get_active_window_title, is_discord
import keyboard
import pyautogui
import time
import pyperclip
from phrase import get_phrase

enter_pressed = False

def on_enter():
    global enter_pressed
    enter_pressed = True
    
def main():
    global enter_pressed
    
    keyboard.add_hotkey('enter', on_enter, suppress=True)
    
    while True:
        if not is_discord(get_active_window_title()): 
            continue
        
        keyboard.wait('enter')
        
        text = get_phrase()
        time.sleep(0.1)
        pyperclip.copy(text)
        
        pyautogui.hotkey('shift', 'enter')
        pyautogui.hotkey('shift', 'enter')
        
        pyautogui.hotkey('ctrl', 'v')
        
        pyautogui.press('enter')

        enter_pressed = False

if __name__ == "__main__":
    main()
    