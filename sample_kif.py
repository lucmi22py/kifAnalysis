# -*- coding: utf-8 -*-
# -*- 役割: 試作、例外処理実装 -*-

# -*- ライブラリ -*-
from pyautogui import locateCenterOnScreen, typewrite, hotkey, click, moveTo, press, write
from pyscreeze import ImageNotFoundException
import glob
import os
import pathlib
import re
import kfkfilemove
import subprocess
from selenium import webdriver
import chromedriver_binary
import bs4
import requests
import pyperclip
from time import sleep
import shutil
import kfkfiling

# -*- 処理部 -*-
# 動作チェック


class KifHandle2:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def open_kif(target_path):
        moveTo(1224, 26)
        click(1224, 26)
        sleep(1)
        # ファイル(クリック)
        moveTo(45, 50)
        click(45, 50)
        # 開く(クリック)
        moveTo(45, 107)
        click(45, 107)
        sleep(1)
        # target_pathをボックス内に貼り付け
        moveTo(503, 113)
        click(503, 113)
        press('delete')
        pyperclip.copy(target_path)
        hotkey('ctrl', 'v')
        press('enter')
        sleep(1)
        # 一番上のファイルをクリック
        moveTo(483, 241)
        sleep(1)
        click(483, 241)
        # ファイル指定ウインドウの開く(クリック)
        moveTo(728, 749)
        sleep(1)
        click(728, 749)
        sleep(2)
        return target_path

    @staticmethod
    # 棋譜解析を行う
    def anakif():
        moveTo(1224, 26)
        click(1224, 26)
        sleep(3)
        moveTo(317, 47)
        click(317, 47)
        moveTo(317, 234)
        click(317, 234)
        sleep(1)
        moveTo(755, 897)
        click(755, 897)

    # 棋譜解析終了判定
    @staticmethod
    def finana():
        while True:
            try:
                d = locateCenterOnScreen('OK.png', grayscale=True)
                if d is not None:
                    x, y = locateCenterOnScreen('OK.png', grayscale=True)
                    moveTo(x, y)
                    click(x, y)
                    break
            except ImageNotFoundException:
                sleep(10)

    @staticmethod
    # 解析済みファイル保存(.kif)
    def savekif():
        moveTo(1224, 26)
        click(1224, 26)
        moveTo(45, 50, duration=0.01)
        click(45, 50)
        sleep(1)
        moveTo(62, 184, duration=0.01)
        click(62, 184)
        sleep(1)
        moveTo(810, 642, duration=0.01)
        click(810, 644)
        sleep(1)
        hotkey('fn', 'end')
        typewrite(['backspace', 'backspace', 'backspace', 'backspace', '_', 'a', 'n', 'a'], 0.04)
        moveTo(735, 748, duration=0.01)
        click(735, 748)
        sleep(5)

    @staticmethod
    def arrangement(src_path: str,
                    dst_path=r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2',
                    ana_dst_path=r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\analysis'):
        # 同名kifファイル移動
        # 比較元ファイル(複数)
        t_src_path = os.path.join(src_path, '*.kif')
        compare_file = glob.glob(t_src_path)
        # 比較対象ファイル(1つ)
        tana_src_path = os.path.join(src_path, '*_ana.*')
        analyzed_kif = glob.glob(tana_src_path)[0]
        pathlib_analyzed_kif = pathlib.Path(analyzed_kif)
        analyzed_kif_prename = pathlib_analyzed_kif.stem.rstrip('_ana')
        for file_num in range(len(compare_file)):
            pathlib_compare_file = pathlib.Path(compare_file[file_num])
            if analyzed_kif_prename == pathlib_compare_file.stem:
                shutil.move(compare_file[file_num], dst_path)
                break

        # kfkfilingによるkfk化は最後にすること
        # pyファイルのあるディレクトリへ対象ファイルを移動させるため
        # *_ana.kifファイルのkfk化
        try:
            kfkfiling.change_suffix(analyzed_kif, ana_dst_path, '.kif', '.kfk')
        except IndexError:
            print("*_ana.kifファイルは存在しません")
        except NameError:
            print("*_ana.kifファイルが見つからないので、f1は存在しません")

        # kfkファイル移動
        kfk_file = glob.glob(src_path + r'\*_ana.kfk')
        try:
            shutil.move(kfk_file[0], ana_dst_path)
        except IndexError:
            print("kfkファイルは存在しません")
        except shutil.Error:
            kfk_file_name = pathlib.Path(kfk_file[0]).name
            resave_path = ana_dst_path + r'\\' + kfk_file_name
            shutil.move(kfk_file[0], resave_path)


dataset = KifHandle2('luc22')
dataset.open_kif(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu1101')
dataset.anakif()
dataset.finana()
dataset.savekif()
dataset.arrangement(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu1101')

# -*- End of file -*-
