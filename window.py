import pygetwindow as gw

def get_active_window_title():
    # Получаем заголовок активного окна
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else None

def is_discord(title: str) -> bool:
    parse_title = title.split()
    
    if parse_title[-1] == "Discord":
        return True
    
    return False
