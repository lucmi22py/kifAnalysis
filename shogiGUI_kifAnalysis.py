import subprocess
import sys
import pyautogui
from time import sleep
from pyscreeze import ImageNotFoundException
from msvcrt import getch
import kfkfilemove
import kfkfiling
import glob
import os
import pathlib
import re
import shutil
import kif_handle


pyautogui.moveTo(45, 50)
sleep(1)
pyautogui.click(45, 50)
pyautogui.click(45, 50)
pyautogui.moveTo(45, 107)
pyautogui.click(45, 107)
sleep(1)
pyautogui.moveTo(483, 241)
sleep(1)
pyautogui.click(483, 241)
pyautogui.moveTo(728, 749)
sleep(1)
pyautogui.click(728, 749)
sleep(2)
# 「棋譜を開く」ここまで

pyautogui.moveTo(317, 47)
pyautogui.click(317, 47)
pyautogui.moveTo(317, 234)
pyautogui.click(317, 234)
sleep(1)
pyautogui.moveTo(755, 897)
pyautogui.click(755, 897)
# 「棋譜解析を行う」ここまで

# 終了判定
while True:
    try:
        d = pyautogui.locateCenterOnScreen('OK.png', grayscale=True)
        if not d ==None:
            x, y = pyautogui.locateCenterOnScreen('OK.png', grayscale=True)
            pyautogui.moveTo(x, y)
            pyautogui.click(x, y)
            break
    except ImageNotFoundException:
        sleep(10)

# ファイル保存
pyautogui.moveTo(45, 50, duration=0.01)
pyautogui.click(45, 50)
sleep(1)
pyautogui.moveTo(62, 184, duration=0.01)
pyautogui.click(62, 184)
sleep(1)
pyautogui.moveTo(810, 642, duration=0.01)
pyautogui.click(810, 644)
sleep(1)
pyautogui.hotkey('fn','end')
pyautogui.typewrite(['backspace', 'backspace', 'backspace', 'backspace', '_', 'a', 'n', 'a'],0.04)
pyautogui.moveTo(735, 748, duration=0.01)
pyautogui.click(735, 748)
sleep(5)

# 同名kifファイル移動判定

path = 'C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu'
A1 = glob.glob(os.path.join(path,'*_ana.*'))    # 対象1
A1_list_str = A1[0]
B = pathlib.Path(A1_list_str)
Target1_deana = B.stem.rstrip("_ana")
A2 = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\*.kif')    # 対象2
for A2_element in A2:
    if Target1_deana in A2_element:
        if __name__ == '__main__':
            kfkfilemove.move_glob(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2',
                                  A2_element)
        break


# kfkfilingによるkfk化は最後にすること
# pyファイルのあるディレクトリへ対象ファイルを移動させるため
# *_ana.kifファイルのkfk化
f = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\*_ana.kif')
try:
    f1 = f[0]
    if __name__ == '__main__':
        kfkfiling.change_suffix(f1, '.kif', '.kfk')
    else:
        print("file is not exist")
except IndexError:
    print("*_ana.kifファイルは存在しません")
except NameError:
    print("*_ana.kifファイルが見つからないので、f1は存在しません")


# kfkファイル移動
try:
    if __name__ == '__main__':
        kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis','C:\\Users\\Ryota Okunishi\\PycharmProjects\\kifAnalysis\\*_ana.kfk')
except IndexError:
    print("kfkファイルは存在しません")


import subprocess

subprocess.Popen('C:\\Program Files (x86)\\ShogiGUI\\ShogiGUI.exe')