from pynput import keyboard
import pyautogui
import time
from pynput.keyboard import Key, Controller

# Текст, который будет добавлен
text_to_type = "-# Пользователь находится в международном розыске Украины"

def press_shift_enter():
    # Press Shift + Enter
    with keyboard.pressed(Key.shift):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

def on_press(key):
    if key == keyboard.Key.enter:
        # Остановить обработку Enter
        return False

def main():
    while True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

        # Вставить текст и отправить
        pyautogui.typewrite(append_text)
        time.sleep(0.1)  # Небольшая задержка
        pyautogui.press('enter')

def main():
    # Настраиваем слушатель
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
