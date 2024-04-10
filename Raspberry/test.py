import pyautogui
import time

def search_on_start_menu(query):
    # Mở menu Start bằng cách nhấn phím Windows
    pyautogui.press('win')
    
    # Chờ 1 giây cho menu Start hiển thị hoàn toàn
    time.sleep(1)
    
    # Nhập query tìm kiếm
    pyautogui.write(query)
    
    # Chờ 1 giây cho kết quả tìm kiếm hiển thị
    time.sleep(1)
    
    # Nhấn Enter để thực hiện tìm kiếm
    # pyautogui.press('enter')

search_query = "Notepad"  # Thay "Notepad" bằng từ khóa bạn muốn tìm kiếm trên menu Start

search_on_start_menu(search_query)
