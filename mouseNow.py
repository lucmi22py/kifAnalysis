import sys
sys.path.append("c:\\users\\ryota okunishi\\anaconda3\\envs\\kifudownload\\lib\\site-packages")
import pyautogui

print('中断するにはctrl-cを押してください')
try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\n終了。')