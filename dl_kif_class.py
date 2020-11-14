# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
from time import sleep
import re
import os
import glob
import pathlib
import shutil
import datetime
from pyautogui import locateCenterOnScreen, typewrite, hotkey, click, moveTo, press
from pyscreeze import ImageNotFoundException
import pyperclip

# from kif_handle import KifHandle as KH
import kif_handle
import kfkfiling


class DLKifClass:
    url = r'https://www.shogi-extend.com/?per=50&query='

    def __init__(self, user_name):
        self.name = user_name
        self.dl_url = r'https://www.shogi-extend.com/w?per=50&query=' + self.name
        self.g_gpd = int()

    def dl_kif(self, save_path=r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu', loop_num=50):
        # google chromeで将棋ウォーズ棋譜検索を開く
        browser = webdriver.Chrome(executable_path=r'C:\Users\Ryota Okunishi\pycharm_projects\kifAnalysis\venv\Lib\site-packages\chromedriver_binary\chromedriver.exe')
        browser.get(self.dl_url)
        sleep(5)  # 5秒待ち(chromeが開いてからでないと以降のコードが受け付られない)

        for num in range(1, loop_num + 1):
            # コピーから取得する方法
            elem_copy = browser.find_element_by_xpath(
                '//tr[' + str(int(num)) + ']/td[4]/div/button[1]'
            )
            elem_copy.click()
            sleep(2.5)

            # ファイル名整形
            pre_paste = pyperclip.paste()
            sp = pre_paste.split('\r\n')
            sente_pick = [s for s in sp if "先手：" in s]
            gote_pick = [s for s in sp if "後手：" in s]
            start_date_pick = [s for s in sp if "開始日時：" in s]

            pre_sp1 = sente_pick[0].split(' ')
            prep_sp1 = pre_sp1[0]
            sp1 = re.sub(r'先手：', '', prep_sp1)
            pre_sp2 = gote_pick[0].split(' ')
            prep_sp2 = pre_sp2[0]
            sp2 = re.sub(r'後手：', '', prep_sp2)
            pre_sp3 = re.sub(r'開始日時：|/|:', '', start_date_pick[0])
            sp3 = re.sub(r' ', '_', pre_sp3)
            title_kif = str(sp1 + '-' + sp2 + '-' + sp3 + '.kif')

            # ファイル保存
            new_kif_file = os.path.abspath(save_path)
            file_kif = open(new_kif_file + r'\\' + title_kif, 'w')
            file_kif.write(pre_paste)
            file_kif.close()
            print("ファイル作成完了。title: " + title_kif)
        print("すべての処理は終了しました")
        browser.quit()

    @staticmethod
    def kifana(src_path: str,
               dst_path: str,
               loop_num: int,
               ana_dst_path=r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\analysis'):
        # 対象ファイルコピー
        if loop_num is None:
            print('ループ回数を入力してください\n')
            loop_num = int(input())
        for num in range(1, loop_num + 1):
            '''
            KH.open_kif()
            KH.ana_kif()
            KH.fin_ana()
            KH.save_kif()
            '''
            # '''
            kif_handle.openkif()
            kif_handle.anakif()
            kif_handle.finana()
            kif_handle.savekif()
            # '''

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
            kfk_file = glob.glob(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu\*_ana.kfk')
            try:
                shutil.move(kfk_file[0], ana_dst_path)
            except IndexError:
                print("kfkファイルは存在しません")
            except shutil.Error:
                kfk_file_name = pathlib.Path(kfk_file[0]).name
                resave_path = ana_dst_path + r'\\' + kfk_file_name
                shutil.move(kfk_file[0], resave_path)

            print('棋譜解析完了しました。:' + str(int(num)) + '局目')

    def daily_kifana_log(self):
        dt_now = datetime.datetime.now()
        path_w = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\daily_kifana_log.txt'
        with open(path_w, mode='w') as f:
            f.write('///daily_kifana実行ログ///' + '\n' +
                    'check date: \t' + str(dt_now) + '\n' +
                    '取得棋譜数: \t' + str(self.g_gpd) + '\n')


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

        # kfkfilingによるkfk化は最後にすること.
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

    @staticmethod
    def kifana2(src_path: str,
                loop_num: int):
        for num in range(1, loop_num + 1):
            KifHandle2.open_kif(src_path)
            KifHandle2.anakif()
            KifHandle2.finana()
            KifHandle2.savekif()
            KifHandle2.arrangement(src_path)
            print('棋譜解析完了しました。:' + str(int(num)) + '局目')
