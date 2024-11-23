# Key Logger
> ***FOR EDUCATIONAL PURPOSES ONLY***

> A simple key logger that logs all the keys pressed by the user and saves them in a text file.

## Link demo:
[📌 D E M O 🔗](web/download.html)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/TienNHM/key_logger.git
```

### 2. Install the required packages
```bash
pip install pynput
pip install pyinstaller
```

### 3. Build the executable file
```bash
pyinstaller --onefile --windowed --icon=unikey.ico --name=unikey --manifest=app.manifest key_logger.py
```

### 4. Run the executable file
```bash
dist/unikey.exe
```

## Usage
- The key logger will start logging all the keys pressed by the user and save them in a text file named `keylog.txt`.
- To stop the key logger, open the task manager and end the process `key_logger.exe`.

## Imortant
- The key logger is for educational purposes only, should not be used for malicious purposes.
- The key logger is detected by most antivirus software, so it is recommended to run it on a virtual machine or disable the antivirus software (at your own risk).
- When running the key logger, the user should be aware that all the keys pressed will be logged and saved in a text file. Key logger program can be found in the task manager and stopped at any time.