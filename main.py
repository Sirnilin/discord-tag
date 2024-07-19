from window import get_active_window_title, is_discord
import time

def main():
    time.sleep(3)
    title = get_active_window_title()
    print(title)

if __name__ == "__main__":
    main()
    